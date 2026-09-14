import { defineConfig } from 'astro/config';
import rehypeExternalLinks from 'rehype-external-links';

export default defineConfig({
  site: 'https://orion8924.github.io',
  base: '/blog',
  trailingSlash: 'always',
  markdown: {
    rehypePlugins: [
      // Los enlaces externos se abren en pestaña nueva para no abandonar el blog.
      [rehypeExternalLinks, { target: '_blank', rel: ['noopener', 'noreferrer'] }],
    ],
  },
});
