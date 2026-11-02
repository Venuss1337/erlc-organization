import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { base, sidebar, repository, site } from './site.config.mjs';

export default defineConfig({
  site,
  base,
  output: 'static',
  trailingSlash: 'always',
  integrations: [starlight({
    title: 'ER:LC Organization',
    description: 'Roles, everyday tasks, governance and independent review for the ER:LC Organization. Documentation v1.2.0; adoption tracked separately.',
    social: [{ icon: 'github', label: 'GitHub repository', href: repository }],
    sidebar,
    customCss: ['./src/styles/custom.css'],
    components: { Footer: './src/components/Footer.astro' },
    editLink: { baseUrl: `${repository}/edit/main/docs/` },
    pagination: true,
    tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
    lastUpdated: false,
  })],
});
