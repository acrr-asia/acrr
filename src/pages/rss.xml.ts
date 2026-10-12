import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import { getPosts } from '../lib/content';

/**
 * RSS 2.0 feed of published articles (drafts are already excluded by getPosts() in production).
 * Item links are built from `site`, so set SITE_URL at build time to get real absolute URLs.
 * Without it the feed falls back to the localhost placeholder from astro.config.mjs; scripts/
 * check-site-url.mjs then warns on a local build and fails a build in a deploy environment.
 *
 * Sample articles are labelled in the item title as well as the description, because feed readers
 * show titles on their own and a sample article must never be mistaken for real research.
 */
export async function GET(context: APIContext) {
  const site = context.site;
  if (!site) {
    throw new Error('rss.xml requires `site` to be set in astro.config.mjs.');
  }

  const posts = await getPosts();
  const hasExamples = posts.some((post) => post.data.example);

  return rss({
    title: 'ACRR — Advanced Computing & Robotics Research',
    description:
      'Technical articles and research notes from ACRR, an independent research and technical publishing platform.' +
      (hasExamples
        ? ' Items titled [Example] are sample content that illustrates the format; they are not original research.'
        : ''),
    site,
    // Routes have no trailing slash (trailingSlash: 'never').
    trailingSlash: false,
    customData: '<language>en</language>',
    items: posts.map((post) => ({
      title: post.data.example ? `[Example] ${post.data.title}` : post.data.title,
      description: post.data.example
        ? `Example article. ${post.data.description}`
        : post.data.description,
      pubDate: post.data.publishedAt,
      link: `/blog/${post.id}`,
      categories: [post.data.category, ...post.data.tags],
    })),
  });
}
