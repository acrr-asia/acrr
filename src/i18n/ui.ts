/**
 * Languages and interface text. English is the original language of the site and lives at the
 * root (/blog/...); Vietnamese is a translation and lives under /vi (/vi/blog/...). Page copy that
 * is more than a label (home, about, learning) is kept beside its view in src/views; everything
 * that several components share is here. See docs/translation-vi.md for the translation rules.
 */
import { publicPath } from '../lib/path';

export const LANGS = ['en', 'vi'] as const;
export type Lang = (typeof LANGS)[number];
export const DEFAULT_LANG: Lang = 'en';

/** Name of each language in that language, for the language switcher. */
export const LANG_NAMES: Record<Lang, string> = { en: 'English', vi: 'Tiếng Việt' };
/** BCP 47 tags for <html lang>, hreflang and date formatting. */
export const LANG_TAGS: Record<Lang, string> = { en: 'en', vi: 'vi' };

/** Language of a page, from its URL: everything under /vi is Vietnamese. */
export function langFromUrl(url: URL): Lang {
  const path = publicPath(url.pathname);
  return path === '/vi' || path.startsWith('/vi/') ? 'vi' : 'en';
}

/** The public path of `path` (an English, root-relative route) in `lang`. */
export function localizePath(path: string, lang: Lang): string {
  if (lang === 'en') return path;
  return path === '/' ? '/vi' : `/vi${path}`;
}

/** Strips the /vi prefix: the English route that corresponds to a public path. */
export function unlocalizePath(path: string): string {
  if (path === '/vi') return '/';
  return path.startsWith('/vi/') ? path.slice(3) : path;
}

const plural = (n: number, one: string, many: string) => `${n} ${n === 1 ? one : many}`;

const en = {
  siteName: 'ACRR — Advanced Computing & Robotics Research',
  skip: 'Skip to content',
  homeLabel: 'ACRR home',
  nav: { blog: 'Blog', series: 'Series', learning: 'Learning', insights: 'Insights', about: 'About', tags: 'Tags', rss: 'RSS' },
  primaryNav: 'Primary',
  footerNav: 'Footer',
  footerAbout: 'Advanced Computing & Robotics Research. An independent research and technical publishing platform.',
  search: 'Search',
  searchAria: 'Search (Ctrl+K)',
  language: 'Language',
  /** Shown by the switcher when the current page has no version in the other language. */
  noTranslation: 'not translated',
  example: 'Example',
  draft: 'Draft',
  draftDev: 'Draft (dev only)',
  exampleTitlePrefix: '[Example]',
  exampleDescription: (kind: 'article' | 'insight' | 'series', d: string) => `Example ${kind}: ${d}`,
  minRead: (n: number) => `${n} min read`,
  readArticle: 'Read article →',
  readInsight: 'Read insight',
  viewSeries: 'View series',
  /** Badge on an English entry listed in another language. */
  inEnglish: 'English',
  status: { planned: 'Planned', 'in-progress': 'In progress', published: 'Published' },
  entriesPublished: (count: number, total: number) =>
    total === 0 ? 'No entries yet' : `${count} of ${total} ${total === 1 ? 'entry' : 'entries'} published`,
  articles: (n: number) => plural(n, 'article', 'articles'),
  insights: (n: number) => plural(n, 'insight', 'insights'),
  // Article page
  backToBlog: '← Blog',
  backToAll: '← Back to all articles',
  articleEyebrow: 'article',
  partOf: (n: number | undefined, title: string) => (n ? `part ${n} · ${title}` : title),
  updated: 'Updated',
  exampleArticleNotice: 'This is illustrative sample content that shows how the site presents an article. It is not original research.',
  exampleArticle: 'Example article',
  draftNotice: 'This article is unfinished. It is shown only in development and is not published.',
  tags: 'Tags',
  seriesEyebrow: 'series',
  partNOf: (n: number | undefined) => (n ? `Part ${n} of ` : 'Part of '),
  prevInSeries: '← Previous in series',
  nextInSeries: 'Next in series →',
  fullSeries: 'View the full series',
  moreArticles: 'More articles',
  olderArticle: '← Older article',
  newerArticle: 'Newer article →',
  keepReading: 'keep reading',
  relatedArticles: 'Related articles',
  contents: 'Contents',
  tableOfContents: 'Table of contents',
  /** Note on a translated page, followed by a link to the original. */
  translationNote: '',
  translationLink: '',
  // Listings
  noArticles: 'No articles have been published yet.',
  exampleListNote: 'Articles marked Example are illustrative samples that show how the site works. They are not original research.',
  categories: 'Article categories',
  all: 'All',
  browseByTag: 'Browse by tag',
  allTags: (hidden: number) => (hidden > 0 ? `All tags (+${hidden})` : 'All tags'),
  untranslatedNote: '',
};

type Dict = typeof en;

const vi: Dict = {
  siteName: 'ACRR — Nghiên cứu Điện toán Tiên tiến & Robot',
  skip: 'Chuyển đến nội dung',
  homeLabel: 'Trang chủ ACRR',
  nav: { blog: 'Bài viết', series: 'Loạt bài', learning: 'Học tập', insights: 'Góc nhìn', about: 'Giới thiệu', tags: 'Thẻ', rss: 'RSS' },
  primaryNav: 'Điều hướng chính',
  footerNav: 'Chân trang',
  footerAbout: 'Nghiên cứu Điện toán Tiên tiến & Robot. Một nền tảng độc lập về nghiên cứu và xuất bản kỹ thuật.',
  search: 'Tìm kiếm',
  searchAria: 'Tìm kiếm (Ctrl+K)',
  language: 'Ngôn ngữ',
  noTranslation: 'chưa có bản dịch',
  example: 'Ví dụ',
  draft: 'Bản nháp',
  draftDev: 'Bản nháp (chỉ khi phát triển)',
  exampleTitlePrefix: '[Ví dụ]',
  exampleDescription: (kind, d) =>
    `${{ article: 'Bài viết ví dụ', insight: 'Góc nhìn ví dụ', series: 'Loạt bài ví dụ' }[kind]}: ${d}`,
  minRead: (n) => `${n} phút đọc`,
  readArticle: 'Đọc bài →',
  readInsight: 'Đọc bài',
  viewSeries: 'Xem loạt bài',
  inEnglish: 'Tiếng Anh',
  status: { planned: 'Dự kiến', 'in-progress': 'Đang viết', published: 'Đã hoàn thành' },
  entriesPublished: (count, total) => (total === 0 ? 'Chưa có bài nào' : `Đã đăng ${count}/${total} bài`),
  articles: (n) => `${n} bài viết`,
  insights: (n) => `${n} góc nhìn`,
  backToBlog: '← Bài viết',
  backToAll: '← Tất cả bài viết',
  articleEyebrow: 'bài viết',
  partOf: (n, title) => (n ? `bài ${n} · ${title}` : title),
  updated: 'Cập nhật',
  exampleArticleNotice: 'Đây là nội dung mẫu minh họa cách trang web trình bày một bài viết, không phải nghiên cứu gốc.',
  exampleArticle: 'Bài viết ví dụ',
  draftNotice: 'Bài viết này chưa hoàn thành. Bài chỉ hiển thị khi phát triển và chưa được xuất bản.',
  tags: 'Thẻ',
  seriesEyebrow: 'loạt bài',
  partNOf: (n) => (n ? `Bài ${n} của loạt ` : 'Thuộc loạt '),
  prevInSeries: '← Bài trước trong loạt',
  nextInSeries: 'Bài tiếp theo trong loạt →',
  fullSeries: 'Xem toàn bộ loạt bài',
  moreArticles: 'Các bài viết khác',
  olderArticle: '← Bài cũ hơn',
  newerArticle: 'Bài mới hơn →',
  keepReading: 'đọc tiếp',
  relatedArticles: 'Bài viết liên quan',
  contents: 'Mục lục',
  tableOfContents: 'Mục lục',
  translationNote: 'Đây là bản dịch tiếng Việt; nếu có khác biệt, bản gốc tiếng Anh là bản chuẩn.',
  translationLink: 'Đọc bản gốc',
  noArticles: 'Chưa có bài viết nào được đăng.',
  exampleListNote: 'Các bài đánh dấu Ví dụ là nội dung mẫu minh họa cách trang web hoạt động, không phải nghiên cứu gốc.',
  categories: 'Chuyên mục bài viết',
  all: 'Tất cả',
  browseByTag: 'Duyệt theo thẻ',
  allTags: (hidden) => (hidden > 0 ? `Tất cả thẻ (+${hidden})` : 'Tất cả thẻ'),
  untranslatedNote: 'Các bài đánh dấu Tiếng Anh chưa được dịch; liên kết dẫn đến bản tiếng Anh.',
};

const dictionaries: Record<Lang, Dict> = { en, vi };

/** Interface text for `lang`. */
export function t(lang: Lang): Dict {
  return dictionaries[lang];
}

/** Display names of the article categories; the stored value (and URL slug) stays English. */
const CATEGORY_VI: Record<string, string> = {
  'Research Notes': 'Ghi chú nghiên cứu',
  'Technical Tutorials': 'Hướng dẫn kỹ thuật',
  Engineering: 'Kỹ thuật',
  'AI and Machine Learning': 'Trí tuệ nhân tạo và học máy',
  'Robotics and Control': 'Robot và điều khiển',
  'Computing Systems': 'Hệ thống máy tính',
  'Mathematical Foundations': 'Cơ sở toán học',
};
export function categoryLabel(category: string, lang: Lang): string {
  return lang === 'vi' ? (CATEGORY_VI[category] ?? category) : category;
}

/** Display names of the insight kinds; the stored value stays English. */
const KIND_VI: Record<string, string> = {
  'Concept explanation': 'Giải thích khái niệm',
  'Engineering observation': 'Quan sát kỹ thuật',
  Comparison: 'So sánh',
  'Research question': 'Câu hỏi nghiên cứu',
  'Methodological note': 'Ghi chú phương pháp',
  'Emerging idea': 'Ý tưởng mới',
  'Policy analysis': 'Phân tích chính sách',
};
export function kindLabel(kind: string, lang: Lang): string {
  return lang === 'vi' ? (KIND_VI[kind] ?? kind) : kind;
}

export function formatDate(d: Date, lang: Lang = 'en'): string {
  return d.toLocaleDateString(lang === 'vi' ? 'vi-VN' : 'en-GB', {
    year: 'numeric',
    month: lang === 'vi' ? 'long' : 'short',
    day: 'numeric',
    timeZone: 'UTC',
  });
}

/** Text of the search dialog. `script` is passed to the client script; `{x}` marks a value. */
export function searchUi(lang: Lang) {
  return lang === 'vi'
    ? {
        title: 'Tìm kiếm',
        close: 'Đóng',
        placeholder: 'Tìm trong trang',
        hint: 'Dùng phím mũi tên để chuyển giữa các kết quả. Enter mở kết quả đầu tiên.',
        script: {
          hint: 'Nhập ít nhất 2 ký tự để tìm kiếm.',
          unavailable: 'Chỉ mục tìm kiếm được tạo bởi npm run build và dùng được trong npm run preview.',
          searching: 'Đang tìm…',
          none: 'Không có kết quả cho “{query}”.',
          one: '{n} kết quả',
          many: '{n} kết quả',
          showing: ', hiển thị {n} kết quả đầu',
          failed: 'Tìm kiếm thất bại. Hãy đóng và mở lại hộp tìm kiếm để thử lại.',
          example: 'Ví dụ',
        },
      }
    : {
        title: 'Search',
        close: 'Close',
        placeholder: 'Search the site',
        hint: 'Arrow keys move between results. Enter opens the first result.',
        script: {
          hint: 'Type at least 2 characters to search the site.',
          unavailable: 'Search index is built with npm run build and available in npm run preview.',
          searching: 'Searching…',
          none: 'No results for “{query}”.',
          one: '{n} result',
          many: '{n} results',
          showing: ', showing the first {n}',
          failed: 'Search failed. Close and reopen search to try again.',
          example: 'Example',
        },
      };
}
