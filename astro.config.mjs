import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { base, groups, repository, site } from './site.config.mjs';

export default defineConfig({
  site,
  base,
  output: 'static',
  trailingSlash: 'always',
  integrations: [starlight({
    title: 'ER:LC Organization',
    description: 'Governance, personnel and operating policies for the ER:LC Organization. Released specification v1.1.0; governance adoption tracked separately.',
    social: [{ icon: 'github', label: 'GitHub repository', href: repository }],
    sidebar: [
      { label: 'Overview', items: [{ label: 'Organization handbook', slug: '' }] },
      ...groups.map(({ label, directory }) => ({ label, items: [{ autogenerate: { directory } }] })),
    ],
    customCss: ['./src/styles/custom.css'],
    components: { Footer: './src/components/Footer.astro' },
    editLink: { baseUrl: `${repository}/edit/main/docs/` },
    pagination: true,
    tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
    lastUpdated: false,
  })],
});
