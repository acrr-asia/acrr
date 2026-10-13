/**
 * getStaticPaths() for the dynamic routes, shared by the English pages (src/pages/...) and their
 * Vietnamese twins (src/pages/vi/...). Both render the same view from src/views; only the language
 * differs. An article, insight or series gets a Vietnamese route only when it has a translation;
 * listings (categories, tags) exist in both languages and list untranslated entries in English.
 */
import { baseId, entryLang, getInsights, getPosts, getSeriesList, getTagIndex, slugify } from './content';
import type { Lang } from '../i18n/ui';

export async function blogPaths(lang: Lang) {
  const posts = (await getPosts(lang)).filter((p) => entryLang(p) === lang);
  return posts.map((post) => ({ params: { slug: baseId(post) }, props: { post } }));
}

export async function categoryPaths(lang: Lang) {
  const posts = await getPosts(lang);
  const categories = [...new Set(posts.map((p) => p.data.category))];
  return categories.map((category) => ({
    params: { category: slugify(category) },
    props: { category, posts: posts.filter((p) => p.data.category === category) },
  }));
}

export async function seriesPaths(lang: Lang) {
  const seriesList = (await getSeriesList(lang)).filter((s) => entryLang(s) === lang);
  return seriesList.map((series) => ({ params: { id: baseId(series) }, props: { series } }));
}

export async function insightPaths(lang: Lang) {
  const insights = (await getInsights(lang)).filter((i) => entryLang(i) === lang);
  return insights.map((insight) => ({ params: { id: baseId(insight) }, props: { insight } }));
}

export async function tagPaths(lang: Lang) {
  const tags = await getTagIndex(lang);
  return tags.map((entry) => ({ params: { tag: entry.slug }, props: { entry } }));
}
