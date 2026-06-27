# Aleyda Solis — LinkedIn Posts

**Profile:** linkedin.com/in/aleyda

---

## Post 1

**Date:** June 25, 2026
**URL:** https://www.linkedin.com/posts/aleyda_after-sharing-the-3-layer-framework-to-activity-7475635998383652864-Mz8q

After sharing the 3-layer framework to measure AI Search Presence, Readiness and Business Impact, here's the practical breakdown of the business impact metrics I'd recommend tracking.

Don't report "AI impact" as one blended number — split metrics by confidence layer:

- **Observed:** what you can directly measure from known AI referrals and conversion paths.
- **Own proxy:** first-party signals showing downstream influence — branded search, direct demand, surfaced-page demand, surveys, and Bing Webmaster Tools AI Performance data.
- **Third-party proxy:** external estimates that help benchmark AI traffic share, prompt samples, and platform mix vs. competitors.
- **Modelled:** planning estimates for influenced pipeline or revenue; useful, but never positioned as attributed proof.

This separation helps you explain what's directly measurable, what's inferred, what's benchmarked, and what's modelled — without overclaiming or underselling AI Search's contribution.

> **Research note:** Solis introduces a 4-layer attribution model — Observed, Own Proxy, Third-Party Proxy, Modelled — for measuring AI search business impact without overclaiming. Splitting metrics by confidence layer prevents misrepresenting AI's contribution to revenue.
> *Playbook relevance: Chapter 8 — Measure What Actually Matters*

---

## Post 2

**Date:** June 21, 2026
**URL:** https://www.linkedin.com/posts/aleyda_bing-is-releasing-new-ai-visibility-insights-activity-7472684891328040960-Jgj3

Bing is releasing new AI Visibility Insights in Bing Webmaster Tools: Intents, Topics, Citation Share, and a Compare option.

- **Intents:** Grounding queries are now classified into broader categories — Informational, Commercial, Navigational, Learn and Solve, Research, Creation, Local, and more.
- **Topics:** Groups related grounding queries into broader thematic clusters. AI systems reason across concepts and themes rather than isolated keywords.
- **Citation Share:** Shows how much of the citation space your site receives for a specific grounding query — calculated as the percentage of citations attributed to your site out of all citations shown for that query.
- **Compare Changes Over Time:** Allows publishers to overlay a previous time period directly onto the current reporting view.

Thanks to the Bing team for being leaders in providing the AI search data needed by the search community to better understand and optimize for AI search.

> **Research note:** Bing Webmaster Tools now provides Citation Share, Intent classification, and Topic grouping — the first platform offering structured AI citation data directly to publishers. Allows tracking of how AI reasons across conceptual themes rather than isolated keywords.
> *Playbook relevance: Chapter 2 — Audit Your Current AI Visibility*

---

## Post 3

**Date:** June 20, 2026
**URL:** https://www.linkedin.com/posts/aleyda_do-ai-assistants-actually-render-your-activity-7473307747128733697-YIWg

Do AI Assistants Actually Render Your JavaScript when Grounding? The result? It's not good.

- US AI assistants (ChatGPT, Gemini, Claude, Copilot, Perplexity, Meta AI) read raw HTML only
- Chinese assistants (DeepSeek, ERNIE, Qwen, Kimi) and Mistral render JavaScript

The most uncomfortable lesson has nothing to do with rendering. It's about trust.

Self-reports are unreliable. Perplexity told in chat that it "couldn't access" the page — while its own crawler had already fetched that exact page and received an HTTP 200.

When you want to know what an AI actually did with your page, trust the server log, never the chatbot's description of itself.

If your important content is injected by JavaScript — client-side frameworks, lazy-loaded sections, content behind tabs that hydrate on load — then for ChatGPT, Gemini, Claude, Perplexity and Copilot, that content effectively does not exist.

> **Research note:** US AI assistants read raw HTML only — JavaScript-rendered content is invisible during grounding. Server logs are more reliable than chatbot self-reports for understanding how AI actually interacts with a page.
> *Playbook relevance: Chapter 4 — Structure Content for AI Extraction*
