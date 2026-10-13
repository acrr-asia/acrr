import { defineCollection, reference } from 'astro:content';
import { glob, file } from 'astro/loaders';
import { z } from 'astro/zod';

export const CATEGORIES = [
  'Research Notes',
  'Technical Tutorials',
  'Engineering',
  'AI and Machine Learning',
  'Robotics and Control',
  'Computing Systems',
  'Mathematical Foundations',
] as const;

const blog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    category: z.enum(CATEGORIES),
    tags: z.array(z.string()).default([]),
    /** Unfinished content: never listed, never routed in production. */
    draft: z.boolean().default(false),
    /** Sample content, labelled as such in the UI. */
    example: z.boolean().default(false),
    series: reference('series').optional(),
    seriesOrder: z.number().int().positive().optional(),
  }),
});

const series = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/series' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    category: z.enum(CATEGORIES),
    objectives: z.array(z.string()).default([]),
    status: z.enum(['planned', 'in-progress', 'published']).default('planned'),
    /** Entries not yet written; shown as planned, with no link. */
    plannedEntries: z
      .array(z.object({ title: z.string(), description: z.string().optional() }))
      .default([]),
    example: z.boolean().default(false),
  }),
});

const insights = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/insights' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishedAt: z.coerce.date(),
    kind: z.enum([
      'Concept explanation',
      'Engineering observation',
      'Comparison',
      'Research question',
      'Methodological note',
      'Emerging idea',
    ]),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    example: z.boolean().default(false),
  }),
});

const learning = defineCollection({
  loader: file('./src/data/learning.json'),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    topic: z.string(),
    type: z.enum(['Study notes', 'Course', 'Book', 'External reference', 'Learning path']),
    /** Only real URLs. Omit until the resource exists. */
    url: z.url().optional(),
    status: z.enum(['planned', 'in-progress', 'published']).default('planned'),
    /** Vietnamese text of the entry (docs/translation-vi.md); the English text is used without it. */
    vi: z.object({ title: z.string(), description: z.string(), topic: z.string() }).optional(),
  }),
});

export const collections = { blog, series, insights, learning };
