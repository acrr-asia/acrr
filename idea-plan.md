# acrr

# ACRR — Website Specification

## 1. Project overview

ACRR (Advanced Computing & Robotics Research) is an independent research and technical publishing platform focused on advanced computing, robotics, and related engineering disciplines.

The website should initially serve as a personal research platform and gradually evolve into a research lab ecosystem. It should support publishing technical articles, organizing research into series, curating learning resources, and sharing research insights.

The website is written in English, and is published in two languages: English (the original, at the domain root) and Vietnamese (translations, under `/vi`). Every article, series and insight is written in English first; Vietnamese translations follow and are labelled as translations, with the English original authoritative where they differ. Interface text exists in both languages. Translation rules: `docs/translation-vi.md`.

### Core objectives

- Establish a credible online presence for ACRR.
- Publish technical articles, research notes, and engineering insights.
- Organize related articles into coherent learning and research series.
- Provide an index of learning resources, including future Notion pages.
- Build a foundation that can later support research projects, collaborators, and a formal laboratory.
- Make the platform deployable immediately without requiring a backend or database.

### Design reference

Use [tieukhoimai.me](https://tieukhoimai.me/) as a reference for information architecture, editorial presentation, content organization, and the overall experience of an independent technical website.

The objective is to adopt a similarly coherent publishing experience, not to copy its content or identity.

## 2. Information architecture

The website should contain six primary sections.

Home

Introduce ACRR, its research interests, featured publications, and current areas of exploration.

Blog

A chronological archive of technical articles, research notes, tutorials, and engineering write-ups.

Series

Structured collections of articles that form a sequence or explore a subject in depth.

Learning

An index of learning paths, study notes, external resources, and future Notion pages.

Insights

Research observations, conceptual explanations, technical perspectives, and emerging ideas.

About

Explain the mission, research scope, principles, and long-term direction of ACRR.

## 3. Detailed page requirements

### 3.1 Home

The homepage should communicate what ACRR is, what it studies, and what readers can find on the platform.

Recommended content:

1. Hero section
    - Full name: Advanced Computing & Robotics Research.
    - Short description of the platform.
    - Primary actions: Explore Research and Browse Learning Resources.
2. Research areas
    - Advanced Computing.
    - Artificial Intelligence and Machine Learning.
    - Robotics and Autonomous Systems.
    - Control Systems and Intelligent Systems.
    - Computational Methods and Engineering.
    
    These are proposed areas of interest, not claims that ACRR already has active projects or a staffed laboratory in every area.
    
3. Featured publications
    - Display selected articles with titles, summaries, publication dates, and categories.
    - Link to the complete article.
4. Research series
    - Highlight structured learning or research sequences.
5. Learning resources
    - Introduce curated learning paths and external resources.
6. Platform direction
    - Explain that ACRR is intended to develop from an independent publishing platform into a broader research ecosystem.

The homepage should be informative without exaggerating the platform's current size, achievements, or research activity.

### 3.2 Blog / Archive

The Blog is the main publishing area.

It should support:

- A chronological article archive.
- Individual article pages.
- Article titles, summaries, publication dates, and categories.
- Reading time where it can be calculated reliably.
- Tags and links to related articles.
- Navigation between the archive and individual posts.
- Responsive typography suitable for long-form technical content.

Recommended article categories include:

- Research Notes
- Technical Tutorials
- Engineering
- AI and Machine Learning
- Robotics and Control
- Computing Systems
- Mathematical Foundations

The archive should be generated from structured content files rather than manually maintaining separate HTML pages for every article.

Any demonstration articles must be clearly identified as examples or drafts. They should not be presented as completed original research if they are only sample content.

### 3.3 Series

Series should organize multiple articles into a coherent sequence.

Each series page should include:

- Series title.
- Short introduction and learning objectives.
- Subject area or category.
- Ordered list of articles.
- Brief descriptions of individual entries.
- Reading progress or completion indicators if useful.
- Links to the corresponding articles.

Potential example series:

- Foundations of Control Systems
- Mathematical Methods for Engineering
- Introduction to Robotics
- Machine Learning Fundamentals
- Computational Methods and Simulation

These are suggested structures. They should be presented as planned or illustrative series until their actual content is available.

### 3.4 Learning

Learning should function as a resource index rather than a duplicate of Notion.

Each resource entry should support:

- Resource title.
- Short description.
- Topic or category.
- Resource type, such as study notes, course, book, or external reference.
- External URL when available.
- Optional status, such as planned, in progress, or published.

Important constraint: no Notion pages have been supplied yet. Therefore, the initial website must not invent Notion URLs or pretend that resources already exist.

Until real links are available, the page can display a concise explanation that learning resources are being organized, together with genuinely available public references. Alternatively, planned collections can be marked as “Coming soon.”

Once actual Notion pages are created, their URLs can be added through the content configuration without redesigning the page.

### 3.5 Insights

Insights should contain shorter, focused pieces of technical writing that do not necessarily need the structure of a full tutorial or research paper.

Possible formats:

- Concept explanations.
- Engineering observations.
- Comparisons of technical approaches.
- Research questions.
- Short methodological notes.
- Emerging ideas and hypotheses.

Each entry should distinguish clearly between established facts, interpretations, and open questions.

If the page displays statistics—such as publication counts, project counts, or research activity—those values must come from actual content or verifiable data. Do not invent readership figures, citations, project milestones, or research metrics.

### 3.6 About

The About page should explain the identity and purpose of ACRR.

Recommended sections:

Mission

To explore advanced computing and robotics through rigorous technical study, experimentation, and research-oriented publishing.

Research scope

Describe the fields that ACRR intends to investigate, without implying that every field already has an active project.

Working principles

- Technical accuracy.
- Reproducibility where applicable.
- Clear explanations of assumptions and limitations.
- Evidence-based conclusions.
- Continuous learning and iteration.
- Open differentiation between established results and exploratory ideas.

Long-term direction

Explain the intention to develop ACRR into a more comprehensive research environment that may eventually support projects, collaboration, and laboratory activities.

Do not fabricate the founder's biography, academic credentials, employment history, publications, collaborators, institutional affiliations, or contact details. Personal information should be added only when explicitly supplied.

## 4. Visual design and user experience

The design should feel like an independent technical publication rather than a generic corporate landing page.

Recommended principles:

- Editorial, restrained visual style.
- Clear typographic hierarchy.
- Comfortable line lengths for long articles.
- Consistent spacing and page margins.
- Subtle borders and separators.
- Limited decorative effects.
- Strong readability on both desktop and mobile.
- Consistent navigation across all pages.
- Distinct visual treatment for code blocks, equations, quotations, and diagrams.
- Accessible color contrast and keyboard navigation.

The interface should prioritize reading and content discovery. Animations and decorative components should not interfere with technical content.

## 5. Technical architecture

For a static website that can be published quickly and expanded over time, a suitable implementation is Astro with Markdown/MDX content collections.

This is a conceptual structure. File extensions and route-generation details depend on the actual implementation.

### Content management

Articles should be stored separately from layout and presentation code. Each article should have validated metadata, for example:

```
title: "Introduction to Control Systems"
description: "An introductory overview of feedback and system behavior."
publishedAt: 2026-10-11
category: "Control Systems"
tags:
  - control-theory
  - engineering
draft: true
```

The example is a content-schema illustration, not a claim that an article has been published. The `draft` field should prevent unfinished content from appearing as a published article.

For learning resources, store actual external URLs in configuration or content files. Missing URLs should remain missing rather than being replaced with invented links.

## 6. MVP scope

The first release should prioritize a complete, usable publishing experience over advanced functionality.

Required for the initial release:

- All six primary sections.
- Consistent site-wide navigation and footer.
- Blog archive and individual article pages.
- Series index and series detail pages.
- Learning resource index.
- Insights archive or listing.
- About page.
- Responsive layouts.
- Clear handling of draft and placeholder content.
- Functional internal links.
- Page titles, descriptions, and basic SEO metadata.
- A 404 page.
- A README with installation, local development, content authoring, and build instructions.

Useful enhancements if time permits:

- RSS feed.
- Sitemap.
- Search or category filtering.
- Related articles.
- Reading time.
- Dark mode.
- Interactive simulations or research visualizations.

Advanced features should not delay the publication of a clean, working first version.

## 7. Acceptance criteria

The website should be considered ready for the initial release when the following checks pass.

| Area | Acceptance criterion |
| --- | --- |
| Navigation | Every primary section is accessible and links work. |
| Content | Articles, series, learning resources, and insights have consistent structures. |
| Accuracy | No fabricated biography, credentials, research results, statistics, or external URLs. |
| Draft handling | Sample or unfinished content is clearly marked and excluded from published listings where appropriate. |
| Responsive design | Pages remain readable and usable on mobile, tablet, and desktop. |
| Accessibility | Semantic headings, keyboard-accessible navigation, and suitable contrast. |
| SEO | Appropriate titles, descriptions, canonical URLs where configured, and sitemap support. |
| Build | Production build completes without errors. |
| Documentation | README explains how to install, run, build, and add content. |
| Deployment | The static output can be deployed to a supported hosting provider. |

## 8. Recommended implementation order

1. Establish the design system, global layout, header, and footer.
2. Implement the Home, About, and Learning pages.
3. Set up structured content and build the Blog archive and article layout.
4. Implement Series and Insights.
5. Add SEO, sitemap, RSS, and 404 handling.
6. Test all routes, links, responsive breakpoints, and the production build.
7. Document deployment and content maintenance.

The first milestone is a coherent, deployable website. More sophisticated research features can be introduced incrementally after the publishing foundation is stable.

Scope boundary: This specification defines the intended content, architecture, and quality criteria. It is not confirmation that a new website build has been completed or tested. The actual source files and production build must be checked separately before the site can be considered release-ready.