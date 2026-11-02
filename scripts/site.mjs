import { readFile, mkdir, writeFile, readdir, unlink } from 'node:fs/promises';
import { watch } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { base, published, repository, route } from '../site.config.mjs';

const root = fileURLToPath(new URL('../', import.meta.url));
const generated = path.join(root, 'src/content/docs');
const release = JSON.parse(await readFile(path.join(root, 'docs/source-map.json'), 'utf8'));

async function files(directory) {
  try {
    return (await Promise.all((await readdir(directory, { withFileTypes: true })).map(entry =>
      entry.isDirectory() ? files(path.join(directory, entry.name)) : path.join(directory, entry.name)))).flat();
  } catch (error) { if (error.code === 'ENOENT') return []; throw error; }
}

function webLink(href, source) {
  if (/^(?:[a-z][\w+.-]*:|\/\/|#)/i.test(href)) return href;
  const [pathname, fragment] = href.split('#');
  const target = path.posix.normalize(path.posix.join(path.posix.dirname(source), pathname));
  if (target.startsWith('../')) throw new Error(`Link escapes repository: ${source}: ${href}`);
  const suffix = fragment ? `#${fragment}` : '';
  if (published.includes(target) || target === 'README.md' || target === 'LICENSE') return route(target) + suffix;
  // Drafts and maintenance records are repository references, never public site routes.
  return `${repository}/blob/main/${target}${suffix}`;
}

function render(source, markdown) {
  const title = markdown.match(/^# (.+)$/m)?.[1];
  if (!title) throw new Error(`Missing title: ${source}`);
  let fence = false, removedTitle = false;
  const lines = markdown.split('\n');
  const body = lines.map((line, index) => {
    if (line.startsWith('```')) { fence = !fence; return line; }
    if (fence) return line;
    // Release metadata is displayed once in the notice; canonical source stays intact.
    if (/^\*\*Project version:\*\* .* · \*\*Release date:\*\* .* · \*\*Status:\*\* Official release\.$/.test(line)) return '';
    const anchor = line.match(/^<a id="([^"]+)"><\/a>$/)?.[1];
    const heading = lines[index + 1]?.match(/^#{2,6} (.+)$/)?.[1];
    // Astro supplies heading IDs. Preserve legacy aliases only where the title changed.
    const slug = heading?.toLowerCase().replace(/[^\w\- ]/g, '').replaceAll(' ', '-');
    if (anchor && anchor === slug) return '';
    if (!removedTitle && line === `# ${title}`) { removedTitle = true; return ''; }
    return line.replace(/\[([^\]\n]+)\]\(([^)\n]+)\)/g,
      (_, label, href) => `[${label}](${webLink(href, source)})`);
  }).join('\n');
  const frontmatter = [
    '---', `title: ${JSON.stringify(title)}`,
    `editUrl: ${JSON.stringify(`${repository}/edit/main/${source}`)}`,
    '---', '',
  ].join('\n');
  // Published procedures are specifications, not evidence of formal adoption.
  const adoption = `\n> **Documentation specification v${release.project_version}.** Guidance grants no new powers. [Approval status](${base}/#documentation-and-approval-status) remains separate from release.\n\n`;
  return frontmatter + adoption + body;
}

export async function prepare() {
  await mkdir(generated, { recursive: true });
  const expected = new Set();
  for (const source of published) {
    const output = path.join(generated, source.replace(/^docs\//, ''));
    expected.add(output);
    await mkdir(path.dirname(output), { recursive: true });
    const text = render(source, await readFile(path.join(root, source), 'utf8'));
    if (await readFile(output, 'utf8').catch(() => '') !== text) await writeFile(output, text);
  }
  const licensePath = path.join(generated, 'license.md');
  expected.add(licensePath);
  const license = await readFile(path.join(root, 'LICENSE'), 'utf8');
  if (license.includes('```')) throw new Error('Choose a longer license code fence before building.');
  const notice = `---\ntitle: License & Copyright\nsidebar: { hidden: true }\npagefind: false\neditUrl: false\nprev: false\nnext: false\n---\n\nThe repository license is reproduced below without alteration.\n\n\`\`\`text\n${license}\n\`\`\`\n`;
  if (await readFile(licensePath, 'utf8').catch(() => '') !== notice) await writeFile(licensePath, notice);
  const notFoundPath = path.join(generated, '404.md');
  expected.add(notFoundPath);
  const notFound = `---\ntitle: Page not found\nsidebar: { hidden: true }\npagefind: false\neditUrl: false\nprev: false\nnext: false\n---\n\nThis page could not be found. Return to the [organization handbook](${base}/) or use search to find a policy.\n`;
  if (await readFile(notFoundPath, 'utf8').catch(() => '') !== notFound) await writeFile(notFoundPath, notFound);
  // Delete only stale generated files inside this fixed staging directory.
  for (const file of await files(generated)) if (!expected.has(file)) await unlink(file);
  console.log(`Prepared ${published.length} explicitly published specification pages and the license. Base: ${base}/`);
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  await prepare();
  const command = process.argv[2] || 'prepare';
  if (command !== 'prepare') {
    if (!['dev', 'build'].includes(command)) throw new Error(`Unknown site command: ${command}`);
    if (command === 'dev') {
      // Complete the initial content/config sync before attaching the live dev runner.
      const sync = Bun.spawn(['bun', '--bun', 'astro', 'sync'], { cwd: root, stdout: 'inherit', stderr: 'inherit' });
      const code = await sync.exited;
      if (code !== 0) process.exit(code);
    }
    let watchers = [], timer, preparing = Promise.resolve();
    if (command === 'dev') {
      const refresh = () => {
        clearTimeout(timer);
        timer = setTimeout(() => {
          preparing = preparing.then(prepare).catch(error => console.error(error));
        }, 150);
      };
      watchers = [watch(path.join(root, 'docs'), { recursive: true }, refresh), watch(path.join(root, 'LICENSE'), refresh)];
    }
    const child = Bun.spawn(['bun', '--bun', 'astro', command, ...(command === 'dev' ? ['--host', '0.0.0.0'] : [])],
      { cwd: root, stdin: 'inherit', stdout: 'inherit', stderr: 'inherit' });
    const stop = () => { watchers.forEach(watcher => watcher.close()); clearTimeout(timer); child.kill(); };
    process.on('SIGINT', stop); process.on('SIGTERM', stop);
    const code = await child.exited;
    watchers.forEach(watcher => watcher.close()); clearTimeout(timer);
    if (code === 0 && command === 'build') {
      const verify = Bun.spawn(['bun', 'scripts/verify-site.mjs'], { cwd: root, stdout: 'inherit', stderr: 'inherit' });
      process.exit(await verify.exited);
    }
    process.exit(code);
  }
}
