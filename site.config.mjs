// Publication is explicit and separate from navigation. No confidential records belong here.
export const site = 'https://venuss1337.github.io';
export const base = '/erlc-organization';
export const repository = 'https://github.com/Venuss1337/erlc-organization';
export const published = [
  'docs/governance/office-of-the-coo.md', 'docs/governance/current-authority.md',
  'docs/operations/function-map.md',
  'docs/index.md', 'docs/start-here/staff-guide.md',
  'docs/operations/everyday-work.md', 'docs/oversight/get-help.md',
  'docs/governance/structure.md', 'docs/governance/governance-council.md',
  'docs/personnel/ranks-and-appointments.md', 'docs/personnel/assignments.md',
  'docs/personnel/recruitment.md', 'docs/personnel/management-and-development.md',
  'docs/directorates/trust-and-safety.md', 'docs/directorates/live-operations.md',
  'docs/directorates/roleplay-programs.md', 'docs/directorates/community-experience.md',
  'docs/directorates/people-and-culture.md', 'docs/directorates/technology-and-systems.md',
  'docs/oversight/independent-oversight.md', 'docs/oversight/case-handling.md',
  'docs/operations/authority-and-escalation.md', 'docs/operations/incident-response.md',
  'docs/operations/continuity.md', 'docs/operations/discord-permissions.md',
  'docs/operations/operating-practices.md',
];
// Repository-only is a publication distinction, never a confidentiality guarantee.
export const repositoryOnly = [
  'docs/proposals/v1-4-ratification.md', 'docs/executive-readiness-v1-4.md', 'docs/executive-workload.json',
  'docs/proposals/v1-3-reform.md', 'docs/reform-evidence.md', 'docs/structure-model.json',
  'docs/proposals/review-register.md', 'docs/proposals/v1-1-ratification.md',
  'docs/readiness-v1-1.md', 'docs/usability-v1-2.md',
  'docs/migration-report.md', 'docs/source-map.json',
];
export const groups = [
  { label: 'Start Here', items: [
    { source: 'docs/index.md', label: 'Organization handbook' },
    { source: 'docs/start-here/staff-guide.md', label: 'Find your role' },
    { source: 'docs/oversight/get-help.md', label: 'Get help, report or appeal' },
  ] },
  { label: 'Everyday Operations', items: [
    { source: 'docs/operations/everyday-work.md', label: 'Everyday staff tasks' },
  ] },
  { label: 'Roles & Ranks', collapsed: true, items: [
    { source: 'docs/personnel/ranks-and-appointments.md' },
    { source: 'docs/personnel/assignments.md' },
  ] },
  { label: 'Divisions & Technology', collapsed: true, items: [
    { source: 'docs/directorates/trust-and-safety.md' },
    { source: 'docs/directorates/live-operations.md' },
    { source: 'docs/directorates/roleplay-programs.md' },
    { source: 'docs/directorates/community-experience.md' },
    { source: 'docs/directorates/people-and-culture.md' },
    { source: 'docs/directorates/technology-and-systems.md' },
  ] },
  { label: 'Leadership & Governance', collapsed: true, items: [
    { source: 'docs/governance/current-authority.md', label: 'Current authority before cutover' },
    { source: 'docs/governance/office-of-the-coo.md' },
    { source: 'docs/governance/structure.md' },
    { source: 'docs/governance/governance-council.md' },
  ] },
  { label: 'Independent Oversight', collapsed: true, items: [
    { source: 'docs/oversight/independent-oversight.md' },
    { source: 'docs/oversight/case-handling.md' },
  ] },
  { label: 'Policies & Procedures', collapsed: true, items: [
    { source: 'docs/operations/function-map.md' },
    { source: 'docs/personnel/recruitment.md' },
    { source: 'docs/personnel/management-and-development.md' },
    { source: 'docs/operations/authority-and-escalation.md' },
    { source: 'docs/operations/operating-practices.md' },
    { source: 'docs/operations/incident-response.md' },
    { source: 'docs/operations/continuity.md' },
    { source: 'docs/operations/discord-permissions.md' },
  ] },
  { label: 'Proposals & Implementation', collapsed: true, items: [
    { label: 'Approval register (repository)', link: `${repository}/blob/main/docs/proposals/review-register.md` },
    { label: 'Pending ratification (repository)', link: `${repository}/blob/main/docs/proposals/v1-4-ratification.md` },
    { label: 'Walkthrough evidence (repository)', link: `${repository}/blob/main/docs/executive-readiness-v1-4.md` },
  ] },
];
export const sidebar = groups.map(({ items, ...group }) => ({
  ...group,
  items: items.map(({ source, ...item }) => source
    ? { ...item, slug: source === 'docs/index.md' ? '' : source.replace(/^docs\//, '').replace(/\.md$/, '') }
    : item),
}));
export function route(source) {
  if (source === 'docs/index.md' || source === 'README.md') return `${base}/`;
  if (source === 'LICENSE') return `${base}/license/`;
  return `${base}/${source.replace(/^docs\//, '').replace(/\.md$/, '')}/`;
}
