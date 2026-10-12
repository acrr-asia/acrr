/**
 * Public route for a pathname.
 *
 * With `build.format: 'file'`, `Astro.url.pathname` is "/blog.html" or "/blog/<slug>.html" (and
 * "/index.html" for the home page) while the site is being built, but "/blog" under `astro dev`.
 * Public routes are extensionless with no trailing slash, so anything that compares or reports
 * `Astro.url.pathname` (active navigation, canonical URLs, Open Graph type) must normalise it here
 * first, otherwise it works in dev and silently fails in the production build.
 *
 *   "/index.html"          -> "/"
 *   "/blog.html"           -> "/blog"
 *   "/blog/index.html"     -> "/blog"
 *   "/blog/a.html"         -> "/blog/a"
 *   "/blog/"               -> "/blog"
 */
export function publicPath(pathname: string): string {
  let path = pathname.replace(/(^|\/)index\.html$/, '$1').replace(/\.html$/, '');
  if (!path.startsWith('/')) path = `/${path}`;
  if (path.length > 1) path = path.replace(/\/+$/, '');
  return path || '/';
}
