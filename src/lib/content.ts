import { getCollection, type CollectionEntry } from 'astro:content';
import { formatDate, localizePath, type Lang } from '../i18n/ui';

/** Drafts are visible only in `astro dev`; production builds exclude them everywhere. */
const showDrafts = import.meta.env.DEV;

/**
 * Astro's `reference('series')` only logs an error (and the build still exits 0) when a `series:`
 * id does not exist. Fail the build instead, so a typo cannot ship an article that silently
 * drops out of its series. Checks every article, drafts included.
 */
async function assertSeriesReferencesExist(): Promise<void> {
  const [allPosts, allSeries] = await Promise.all([getCollection('blog'), getCollection('series')]);
  const known = new Set(allSeries.filter((s) => !s.id.startsWith('vi/')).map((s) => s.id));
  const broken = allPosts.filter((p) => p.data.series && !known.has(p.data.series.id));
  if (broken.length > 0) {
    const lines = broken.map((p) => `  - src/content/blog/${p.id}: series "${p.data.series?.id}"`);
    throw new Error(
      `Unknown series id in article frontmatter. Create the series in src/content/series/ or fix the id:\n${lines.join('\n')}\nKnown series ids: ${[...known].join(', ') || '(none)'}`,
    );
  }
}

/** Language of an entry: translations live in a `vi/` subdirectory of their collection. */
export function entryLang(entry: { id: string }): Lang {
  return entry.id.startsWith('vi/') ? 'vi' : 'en';
}

/** The id an entry shares with its original (the translation's file name without `vi/`). */
export function baseId(entry: { id: string }): string {
  return entry.id.replace(/^vi\//, '');
}

export const postHref = (post: CollectionEntry<'blog'>) => localizePath(`/blog/${baseId(post)}`, entryLang(post));
export const insightHref = (item: CollectionEntry<'insights'>) => localizePath(`/insights/${baseId(item)}`, entryLang(item));
export const seriesHref = (series: CollectionEntry<'series'>) => localizePath(`/series/${baseId(series)}`, entryLang(series));

const sameDate = (a?: Date, b?: Date) => (a?.valueOf() ?? null) === (b?.valueOf() ?? null);
const sameList = (a: string[], b: string[]) => a.length === b.length && a.every((x, i) => x === b[i]);

/**
 * Pairs each original with its Vietnamese translation. A translation without an original, or one
 * whose shared frontmatter has drifted from the original's, fails the build: those fields are
 * copied, not translated (docs/translation-vi.md), so a mismatch means one file was edited and the
 * other forgotten.
 */
function pairTranslations<E extends { id: string; data: Record<string, unknown> }>(
  collection: string,
  entries: E[],
  shared: (original: E, translation: E) => string | null,
): { originals: E[]; translations: Map<string, E> } {
  const originals = entries.filter((e) => entryLang(e) === 'en');
  const byId = new Map(originals.map((e) => [e.id, e]));
  const translations = new Map<string, E>();
  const problems: string[] = [];
  for (const tr of entries.filter((e) => entryLang(e) === 'vi')) {
    const original = byId.get(baseId(tr));
    if (!original) {
      problems.push(`  - src/content/${collection}/${tr.id}: no original "${baseId(tr)}"`);
      continue;
    }
    const mismatch = shared(original, tr);
    if (mismatch) problems.push(`  - src/content/${collection}/${tr.id}: ${mismatch} differs from the original`);
    translations.set(original.id, tr);
  }
  if (problems.length > 0) {
    throw new Error(`Invalid translations (see docs/translation-vi.md):\n${problems.join('\n')}`);
  }
  return { originals, translations };
}

async function blogEntries() {
  await assertSeriesReferencesExist();
  const all = await getCollection('blog');
  return pairTranslations('blog', all, (o, t) => {
    const a = o.data, b = t.data;
    if (!sameDate(a.publishedAt, b.publishedAt)) return 'publishedAt';
    if (!sameDate(a.updatedAt, b.updatedAt)) return 'updatedAt';
    if (a.category !== b.category) return 'category';
    if (!sameList(a.tags, b.tags)) return 'tags';
    if (a.series?.id !== b.series?.id) return 'series';
    if (a.seriesOrder !== b.seriesOrder) return 'seriesOrder';
    if (a.draft !== b.draft) return 'draft';
    if (a.example !== b.example) return 'example';
    return null;
  });
}

/** Newest first. On the same date a later series entry counts as newer, then the id breaks ties. */
const byDate = (a: CollectionEntry<'blog'>, b: CollectionEntry<'blog'>) =>
  b.data.publishedAt.valueOf() - a.data.publishedAt.valueOf() ||
  (b.data.seriesOrder ?? 0) - (a.data.seriesOrder ?? 0) ||
  baseId(a).localeCompare(baseId(b));

/**
 * Listed articles in `lang`: every original article, replaced by its translation where one
 * exists. In Vietnamese, untranslated articles are therefore listed in English (entryLang() tells
 * which), and link to the English page.
 */
export async function getPosts(lang: Lang = 'en'): Promise<CollectionEntry<'blog'>[]> {
  const { originals, translations } = await blogEntries();
  return originals
    .filter(({ data }) => showDrafts || !data.draft)
    .map((p) => (lang === 'vi' ? (translations.get(p.id) ?? p) : p))
    .sort(byDate);
}

/** Translations only (they get their own routes, and the Vietnamese RSS feed lists them). */
export async function getTranslatedPosts(lang: Exclude<Lang, 'en'>): Promise<CollectionEntry<'blog'>[]> {
  return (await getPosts(lang)).filter((p) => entryLang(p) === lang);
}

/** The translation of an article (or insight, or series) into `lang`, if there is one. */
export async function hasTranslation(collection: 'blog' | 'insights' | 'series', id: string): Promise<boolean> {
  return (await getCollection(collection)).some((e) => e.id === `vi/${id}`);
}

async function insightEntries() {
  const all = await getCollection('insights');
  return pairTranslations('insights', all, (o, t) => {
    const a = o.data, b = t.data;
    if (!sameDate(a.publishedAt, b.publishedAt)) return 'publishedAt';
    if (a.kind !== b.kind) return 'kind';
    if (!sameList(a.tags, b.tags)) return 'tags';
    if (a.draft !== b.draft) return 'draft';
    if (a.example !== b.example) return 'example';
    return null;
  });
}

export async function getInsights(lang: Lang = 'en'): Promise<CollectionEntry<'insights'>[]> {
  const { originals, translations } = await insightEntries();
  return originals
    .filter(({ data }) => showDrafts || !data.draft)
    .map((i) => (lang === 'vi' ? (translations.get(i.id) ?? i) : i))
    .sort((a, b) => b.data.publishedAt.valueOf() - a.data.publishedAt.valueOf() || baseId(a).localeCompare(baseId(b)));
}

async function seriesEntries() {
  const all = await getCollection('series');
  return pairTranslations('series', all, (o, t) => {
    const a = o.data, b = t.data;
    if (a.category !== b.category) return 'category';
    if (a.status !== b.status) return 'status';
    if (a.example !== b.example) return 'example';
    if (a.plannedEntries.length !== b.plannedEntries.length) return 'the number of plannedEntries';
    return null;
  });
}

/** Series in `lang` (translated where a translation exists), sorted by their displayed title. */
export async function getSeriesList(lang: Lang = 'en'): Promise<CollectionEntry<'series'>[]> {
  const { originals, translations } = await seriesEntries();
  return originals
    .map((s) => (lang === 'vi' ? (translations.get(s.id) ?? s) : s))
    .sort((a, b) => a.data.title.localeCompare(b.data.title, lang));
}

/** The series entry for `id` in `lang` (its translation if there is one, else the original). */
export async function getSeries(id: string, lang: Lang = 'en'): Promise<CollectionEntry<'series'> | undefined> {
  return (await getSeriesList(lang)).find((s) => baseId(s) === id);
}

/** Published articles belonging to a series, in reading order. */
export async function getSeriesPosts(seriesId: string, lang: Lang = 'en'): Promise<CollectionEntry<'blog'>[]> {
  const posts = await getPosts(lang);
  return posts
    .filter((p) => p.data.series?.id === seriesId)
    .sort((a, b) => (a.data.seriesOrder ?? 999) - (b.data.seriesOrder ?? 999));
}

/** Related by shared tags (weight 2) and category (weight 1); excludes the post itself. */
export async function getRelatedPosts(post: CollectionEntry<'blog'>, limit = 3, lang: Lang = entryLang(post)) {
  const posts = await getPosts(lang);
  return posts
    .filter((p) => baseId(p) !== baseId(post))
    .map((p) => ({
      p,
      score:
        p.data.tags.filter((t) => post.data.tags.includes(t)).length * 2 +
        (p.data.category === post.data.category ? 1 : 0),
    }))
    .filter((x) => x.score > 0)
    .sort((a, b) => b.score - a.score || b.p.data.publishedAt.valueOf() - a.p.data.publishedAt.valueOf())
    .slice(0, limit)
    .map((x) => x.p);
}

export { formatDate };

export const slugify = (s: string) =>
  s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');

/** Short, stable hash used when a tag has no ASCII letters or digits to build a slug from. */
const shortHash = (s: string) => {
  let h = 5381;
  for (const ch of s) h = ((h << 5) + h + (ch.codePointAt(0) ?? 0)) >>> 0;
  return h.toString(36);
};

/**
 * URL slug for a tag: accents are stripped (Kálmán -> kalman), "+" becomes "plus" and "#" becomes
 * "sharp" (C++ -> cplusplus, C# -> csharp), everything else non-alphanumeric becomes "-". A tag
 * with nothing left (non-Latin script, punctuation only) gets "tag-<hash>", so a slug is always a
 * plain ASCII file name. "index" is reserved for the /tags page itself.
 */
export const tagSlug = (tag: string) => {
  const slug = tag
    .normalize('NFKD')
    .replace(/[̀-ͯ]/g, '')
    .toLowerCase()
    .replace(/\+/g, 'plus')
    .replace(/#/g, 'sharp')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
  if (!slug) return `tag-${shortHash(tag.trim().toLowerCase())}`;
  return slug === 'index' ? 'tag-index' : slug;
};

export interface TagEntry {
  slug: string;
  /** Display name: the spelling of the first article or insight that used the tag. */
  name: string;
  posts: CollectionEntry<'blog'>[];
  insights: CollectionEntry<'insights'>[];
  /** Number of listed articles plus insights. */
  count: number;
}

/**
 * Every tag used by a listed article or insight, with its entries. Built from getPosts() and
 * getInsights(), so a tag that only appears on a draft has no page in production. Sorted by
 * count (descending), then name.
 */
export async function getTagIndex(lang: Lang = 'en'): Promise<TagEntry[]> {
  const [posts, insights] = await Promise.all([getPosts(lang), getInsights(lang)]);
  const index = new Map<string, TagEntry>();
  // Spelling variants that differ only in case or spacing share a page on purpose ("Control Theory"
  // and "control-theory"). Anything else that lands on one slug is a collision: fail the build
  // rather than silently merging unrelated tags.
  const spellingKey = (tag: string) => tag.trim().toLowerCase().replace(/\s+/g, '-');
  const keys = new Map<string, string>();
  const entryFor = (tag: string): TagEntry => {
    const slug = tagSlug(tag);
    const key = spellingKey(tag);
    const seen = keys.get(slug);
    if (seen !== undefined && seen !== key) {
      throw new Error(
        `Tags "${seen}" and "${key}" both map to the URL /tags/${slug}. Rename one of them in the frontmatter so they stay distinct.`,
      );
    }
    keys.set(slug, key);
    let entry = index.get(slug);
    if (!entry) {
      entry = { slug, name: tag.trim(), posts: [], insights: [], count: 0 };
      index.set(slug, entry);
    }
    return entry;
  };
  for (const post of posts) {
    for (const tag of new Set(post.data.tags.map((t) => t.trim()).filter(Boolean))) {
      const entry = entryFor(tag);
      if (!entry.posts.includes(post)) entry.posts.push(post);
    }
  }
  for (const insight of insights) {
    for (const tag of new Set(insight.data.tags.map((t) => t.trim()).filter(Boolean))) {
      const entry = entryFor(tag);
      if (!entry.insights.includes(insight)) entry.insights.push(insight);
    }
  }
  for (const entry of index.values()) entry.count = entry.posts.length + entry.insights.length;
  return [...index.values()].sort((a, b) => b.count - a.count || a.name.localeCompare(b.name));
}
