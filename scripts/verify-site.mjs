import { readFile, readdir, stat } from 'node:fs/promises';
import path from 'node:path';
import { base, site, published, repositoryOnly, route, groups } from '../site.config.mjs';

const dist = path.resolve('dist');
const errors = [];
const navigationSources = groups.flatMap(group => group.items.flatMap(item => item.source ? [item.source] : []));
if (new Set(published).size !== published.length || new Set(navigationSources).size !== navigationSources.length)
  errors.push('Duplicate publication or sidebar source');
if (published.some(source => !navigationSources.includes(source)) || navigationSources.some(source => !published.includes(source)))
  errors.push('Every published Markdown source must have exactly one sidebar entry');
if (published.some(source => repositoryOnly.includes(source) || source.startsWith('docs/proposals/')))
  errors.push('Repository-only/proposed material in publication allowlist');
const workflow = Bun.YAML.parse(await readFile('.github/workflows/deploy.yml', 'utf8'));
const pkg = JSON.parse(await readFile('package.json', 'utf8'));
const release = JSON.parse(await readFile('docs/source-map.json', 'utf8'));
if (pkg.version !== release.project_version) errors.push('Package version differs from official project version');
if (!workflow.on?.push?.branches?.includes('main') || !('workflow_dispatch' in workflow.on)) errors.push('Incorrect deployment triggers');
if (workflow.permissions?.contents !== 'read' || Object.keys(workflow.permissions).length !== 1) errors.push('Unexpected default workflow permissions');
const buildSteps = workflow.jobs?.build?.steps || [];
const astroAction = buildSteps.find(step => step.uses === 'withastro/action@v6');
if (!astroAction || astroAction.with?.['package-manager'] !== pkg.packageManager || !astroAction.with?.['build-cmd']?.includes('bun install --frozen-lockfile')) errors.push('Workflow does not build reproducibly with the pinned Bun');
if (!buildSteps.some(step => step.uses === 'actions/checkout@v7' && step.with?.['fetch-depth'] === 0)) errors.push('Workflow must fetch preservation history');
if (workflow.jobs?.deploy?.needs !== 'build' || !workflow.jobs?.deploy?.steps?.some(step => step.uses === 'actions/deploy-pages@v5')) errors.push('Invalid Pages deployment job');
if (workflow.jobs?.deploy?.permissions?.pages !== 'write' || workflow.jobs?.deploy?.permissions?.['id-token'] !== 'write') errors.push('Missing Pages/OIDC deployment permissions');
async function files(directory) {
  return (await Promise.all((await readdir(directory, { withFileTypes: true })).map(entry =>
    entry.isDirectory() ? files(path.join(directory, entry.name)) : path.join(directory, entry.name)))).flat();
}
const htmlFiles = (await files(dist)).filter(file => file.endsWith('.html'));
const pages = new Map();
for (const file of htmlFiles) {
  const relative = path.relative(dist, file).replaceAll('\\', '/');
  const url = `${base}/${relative.replace(/index\.html$/, '')}`;
  const ids = new Set(), links = [], canonical = [];
  const rewriter = new HTMLRewriter()
    .on('[id]', { element(element) {
      const id = element.getAttribute('id');
      if (ids.has(id)) errors.push(`${url}: duplicate ID ${id}`);
      ids.add(id);
    } })
    .on('a[href], link[href], script[src], img[src], source[src]', { element(element) {
      const value = element.getAttribute('href') || element.getAttribute('src');
      if (element.getAttribute('rel') === 'canonical') canonical.push(value);
      else links.push(value);
    } });
  const html = await readFile(file, 'utf8');
  await rewriter.transform(new Response(html)).text();
  pages.set(url, { ids, links, html });
  if (url !== `${base}/404.html` && !canonical.includes(site + url)) errors.push(`${url}: incorrect canonical URL`);
}

const expected = new Set([...published.map(route), route('LICENSE'), `${base}/404.html`]);
for (const url of expected) if (!pages.has(url)) errors.push(`Missing route ${url}`);
for (const url of pages.keys()) if (!expected.has(url)) errors.push(`Unexpected public route ${url}`);

let linkCount = 0;
for (const [url, { links, html }] of pages) {
  for (const href of links) {
    if (!href || /^(?:data:|mailto:|tel:|javascript:)/i.test(href)) continue;
    const target = new URL(href, site + url);
    if (target.origin !== site) continue;
    linkCount++;
    if (!target.pathname.startsWith(`${base}/`)) {
      errors.push(`${url}: missing Pages base in ${href}`); continue;
    }
    const page = pages.get(target.pathname);
    if (page) {
      if (target.hash && !page.ids.has(decodeURIComponent(target.hash.slice(1))))
        errors.push(`${url}: broken fragment ${href}`);
    } else {
      const file = path.resolve(dist, decodeURIComponent(target.pathname.slice(base.length + 1)));
      if (!file.startsWith(dist + path.sep) || !(await stat(file).catch(() => null))?.isFile())
        errors.push(`${url}: missing output ${href}`);
    }
  }
  if (url !== `${base}/404.html`) {
    if (published.some(source => route(source) === url) && !html.includes(`Documentation specification v${release.project_version}`))
      errors.push(`${url}: missing specification/adoption notice`);
    for (const group of groups) if (!html.includes(group.label.replaceAll('&', '&amp;')) && !html.includes(group.label))
      errors.push(`${url}: missing sidebar group ${group.label}`);
    if (!html.includes('Look-But-Don') || !html.includes('Wiktor Fila')) errors.push(`${url}: missing license notice`);
    for (const source of navigationSources) if (!links.includes(route(source)))
      errors.push(`${url}: missing sidebar route ${route(source)}`);
  }
}
const searchFiles = (await files(path.join(dist, 'pagefind'))).map(file => path.basename(file));
if (!searchFiles.includes('pagefind.js')) errors.push('Missing Pagefind search assets');
// Sidebar hiding is not publication exclusion. These sources must have no output route.
for (const excluded of repositoryOnly) {
  if (pages.has(route(excluded))) errors.push(`Repository-only material published: ${excluded}`);
}
const staged = (await files(path.resolve('src/content/docs'))).filter(file => /\.mdx?$/.test(file))
  .map(file => path.relative(path.resolve('src/content/docs'), file).replaceAll('\\', '/'));
const expectedStaged = [...published.map(source => source.replace(/^docs\//, '')), 'license.md', '404.md'];
if (staged.length !== expectedStaged.length || staged.some(file => !expectedStaged.includes(file)))
  errors.push('Unexpected staged Markdown could leak into routes or search');

if (errors.length) throw new Error(errors.join('\n'));
console.log(`PASS: ${pages.size} static routes; ${linkCount} local links/assets/fragments; Pages base ${base}/.`);
console.log('PASS: explicit publication list, sidebar groups, canonical URLs, license notice and search assets.');
console.log('PASS: deployment YAML triggers, actions, Bun lockfile command, minimal permissions and project version.');
