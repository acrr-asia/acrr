/**
 * Runs after rehype-mermaid (strategy 'inline-svg'). Wraps every rendered Mermaid <svg> in the
 * same frame as the hand-made diagrams (`figure.diagram > .diagram-frame`, styled in prose.css),
 * marks it `mermaid-svg` so prose.css can recolour it with the site's tokens (light and dark),
 * and keeps the diagram's labels out of Pagefind search excerpts.
 *
 * A diagram that fails to render is a build error (see `errorFallback` in astro.config.mjs), so a
 * broken diagram is never published as an empty space.
 */
export function rehypeMermaidFigure() {
  return (tree) => visit(tree);
}

function visit(node) {
  if (!node.children) return;
  node.children = node.children.map((child) => {
    if (isMermaidSvg(child)) return wrap(child);
    visit(child);
    return child;
  });
}

function isMermaidSvg(node) {
  return (
    node.type === 'element' &&
    node.tagName === 'svg' &&
    typeof node.properties?.id === 'string' &&
    node.properties.id.startsWith('mermaid')
  );
}

function wrap(svg) {
  const className = [].concat(svg.properties.className ?? []);
  svg.properties.className = [...className, 'mermaid-svg'];
  // Mermaid sets an inline max-width equal to the diagram's natural width. Add a min-width of
  // 65% of it, so the diagram never shrinks below about 10px text: on a narrow screen the frame
  // scrolls sideways instead (same behaviour as the hand-made diagrams).
  const style = String(svg.properties.style ?? '');
  const natural = /max-width:\s*([\d.]+)px/.exec(style);
  if (natural) {
    const min = Math.round(Number(natural[1]) * 0.65);
    svg.properties.style = `${style.replace(/;?\s*$/, '')};min-width:${min}px`;
  }
  return {
    type: 'element',
    tagName: 'figure',
    properties: { className: ['diagram', 'mermaid-diagram'], dataPagefindIgnore: '' },
    children: [
      { type: 'element', tagName: 'div', properties: { className: ['diagram-frame'] }, children: [svg] },
    ],
  };
}
