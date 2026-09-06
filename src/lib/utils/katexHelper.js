import katex from 'katex';
import 'katex/dist/katex.min.css';

/**
 * Parses text containing $ ... $ (inline) and $$ ... $$ (display)
 * and replaces math expressions with KaTeX rendered HTML strings.
 */
export function formatMathText(text) {
  if (!text || typeof text !== 'string') return text || "";

  // Escape HTML tags to prevent XSS except for our own generated tags
  let safeText = text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");

  // Replace $$ display math $$
  let result = safeText.replace(/\$\$(.*?)\$\$/gs, (match, formula) => {
    try {
      const cleanFormula = formula.replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&amp;/g, "&");
      return `<div class="katex-display-wrapper">${katex.renderToString(cleanFormula.trim(), { displayMode: true, throwOnError: false })}</div>`;
    } catch (e) {
      return match;
    }
  });

  // Replace $ inline math $
  result = result.replace(/\$(.*?)\$/g, (match, formula) => {
    try {
      const cleanFormula = formula.replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&amp;/g, "&");
      return katex.renderToString(cleanFormula.trim(), { displayMode: false, throwOnError: false });
    } catch (e) {
      return match;
    }
  });

  // Convert newlines to <br/>
  return result.replace(/\n/g, '<br/>');
}
