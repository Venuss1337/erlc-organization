// Publication is opt-in. New Markdown is never published just because it exists.
export const site = 'https://venuss1337.github.io';
export const base = '/erlc-organization';
export const repository = 'https://github.com/Venuss1337/erlc-organization';
export const groups = [
  { label: 'Governance', directory: 'governance', pages: ['structure', 'governance-council'] },
  { label: 'Personnel & Ranks', directory: 'personnel', pages: ['ranks-and-appointments', 'assignments', 'recruitment'] },
  { label: 'Directorates', directory: 'directorates', pages: ['trust-and-safety', 'live-operations', 'roleplay-programs', 'community-experience', 'people-and-culture', 'technology-and-systems'] },
  { label: 'Independent Oversight', directory: 'oversight', pages: ['independent-oversight'] },
  { label: 'Operations', directory: 'operations', pages: ['authority-and-escalation', 'discord-permissions', 'operating-practices'] },
];
export const published = ['docs/index.md', ...groups.flatMap(group =>
  group.pages.map(page => `docs/${group.directory}/${page}.md`))];
export function route(source) {
  if (source === 'docs/index.md' || source === 'README.md') return `${base}/`;
  if (source === 'LICENSE') return `${base}/license/`;
  return `${base}/${source.replace(/^docs\//, '').replace(/\.md$/, '')}/`;
}
