import { getCollection, type CollectionEntry } from 'astro:content';

/** Drafts are visible only in `astro dev`; production builds exclude them everywhere. */
const showDrafts = import.meta.env.DEV;

/**
 * Astro's `reference('series')` only logs an error (and the build still exits 0) when a `series:`
 * id does not exist. Fail the build instead, so a typo cannot ship an article that silently
 * drops out of its series. Checks every article, drafts included.
 */
async function assertSeriesReferencesExist(): Promise<void> {
  const [allPosts, allSeries] = await Promise.all([getCollection('blog'), getCollection('series')]);
  const known = new Set(allSeries.map((s) => s.id));
  const broken = allPosts.filter((p) => p.data.series && !known.has(p.data.series.id));
  if (broken.length > 0) {
    const lines = broken.map((p) => `  - src/content/blog/${p.id}: series "${p.data.series?.id}"`);
    throw new Error(
      `Unknown series id in article frontmatter. Create the series in src/content/series/ or fix the id:\n${lines.join('\n')}\nKnown series ids: ${[...known].join(', ') || '(none)'}`,
    );
  }
}

export async function getPosts(): Promise<CollectionEntry<'blog'>[]> {
  await assertSeriesReferencesExist();
  const posts = await getCollection('blog', ({ data }) => showDrafts || !data.draft);
  // Newest first; the id breaks ties so list and pager order never depend on load order.
  return posts.sort((a, b) => b.data.publishedAt.valueOf() - a.data.publishedAt.valueOf() || a.id.localeCompare(b.id));
}

export async function getInsights(): Promise<CollectionEntry<'insights'>[]> {
  const items = await getCollection('insights', ({ data }) => showDrafts || !data.draft);
  return items.sort((a, b) => b.data.publishedAt.valueOf() - a.data.publishedAt.valueOf() || a.id.localeCompare(b.id));
}

export async function getSeriesList(): Promise<CollectionEntry<'series'>[]> {
  return (await getCollection('series')).sort((a, b) => a.data.title.localeCompare(b.data.title));
}

/** Published articles belonging to a series, in reading order. */
export async function getSeriesPosts(seriesId: string): Promise<CollectionEntry<'blog'>[]> {
  const posts = await getPosts();
  return posts
    .filter((p) => p.data.series?.id === seriesId)
    .sort((a, b) => (a.data.seriesOrder ?? 999) - (b.data.seriesOrder ?? 999));
}

/** Related by shared tags (weight 2) and category (weight 1); excludes the post itself. */
export async function getRelatedPosts(post: CollectionEntry<'blog'>, limit = 3) {
  const posts = await getPosts();
  return posts
    .filter((p) => p.id !== post.id)
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

export function formatDate(d: Date): string {
  return d.toLocaleDateString('en-GB', { year: 'numeric', month: 'short', day: 'numeric', timeZone: 'UTC' });
}

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
export async function getTagIndex(): Promise<TagEntry[]> {
  const [posts, insights] = await Promise.all([getPosts(), getInsights()]);
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
