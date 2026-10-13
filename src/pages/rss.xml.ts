import type { APIContext } from 'astro';
import { rssFeed } from '../lib/rss';

export const GET = (context: APIContext) => rssFeed(context, 'en');
