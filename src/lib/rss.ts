import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import { entryLang, getPosts, postHref } from './content';
import { t, type Lang } from '../i18n/ui';

/**
 * RSS 2.0 feed of published articles in `lang`. The English feed lists every article; the
 * Vietnamese feed lists translated articles only, so that a Vietnamese reader gets Vietnamese items.
 * Drafts are already excluded by getPosts() in production.
 * Item links are built from `site`, so set SITE_URL at build time to get real absolute URLs.
 * Without it the feed falls back to the localhost placeholder from astro.config.mjs; scripts/
 * check-site-url.mjs then warns on a local build and fails a build in a deploy environment.
 *
 * Sample articles are labelled in the item title as well as the description, because feed readers
 * show titles on their own and a sample article must never be mistaken for real research.
 */
export async function rssFeed(context: APIContext, lang: Lang) {
  const site = context.site;
  if (!site) {
    throw new Error('rss.xml requires `site` to be set in astro.config.mjs.');
  }

  const posts = (await getPosts(lang)).filter((p) => entryLang(p) === lang);
  const ui = t(lang);
  const hasExamples = posts.some((post) => post.data.example);

  return rss({
    title: ui.siteName,
    description:
      (lang === 'vi'
        ? 'Bản dịch tiếng Việt các bài viết kỹ thuật và ghi chú nghiên cứu của ACRR, một nền tảng độc lập về nghiên cứu và xuất bản kỹ thuật.'
        : 'Technical articles and research notes from ACRR, an independent research and technical publishing platform.') +
      (hasExamples
        ? lang === 'vi'
          ? ' Các mục có tiêu đề [Ví dụ] là nội dung mẫu minh họa định dạng, không phải nghiên cứu gốc.'
          : ' Items titled [Example] are sample content that illustrates the format; they are not original research.'
        : ''),
    site,
    // Routes have no trailing slash (trailingSlash: 'never').
    trailingSlash: false,
    customData: `<language>${lang}</language>`,
    items: posts.map((post) => ({
      title: post.data.example ? `${ui.exampleTitlePrefix} ${post.data.title}` : post.data.title,
      description: post.data.example ? ui.exampleDescription('article', post.data.description) : post.data.description,
      pubDate: post.data.publishedAt,
      link: postHref(post),
      categories: [post.data.category, ...post.data.tags],
    })),
  });
}
