import getReadingTime from 'reading-time';
import { toString } from 'mdast-util-to-string';

/** Adds `minutesRead` to frontmatter, computed from the actual article text. */
export function remarkReadingTime() {
  return function (tree, { data }) {
    const text = toString(tree);
    const { minutes } = getReadingTime(text);
    data.astro.frontmatter.minutesRead = Math.max(1, Math.round(minutes));
  };
}
