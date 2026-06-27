# Playbook Outline: AI-Powered SEO Content Production

_A practitioner-sourced framework for content visibility in AI search (2026)_
_Research by Titash Sinha | Built from 25 expert sources (LinkedIn posts + YouTube transcripts)_

---

> This outline maps a complete playbook structure for AI-powered SEO content production. Every chapter is grounded in specific practitioner sources from this research. The outline is designed so that each section can be written directly from the supporting evidence — no additional research required for core chapters.

---

## Who This Playbook Is For

**Primary audience:** Content strategists, SEO leads, and marketing managers at B2B SaaS companies with an existing content function who need to adapt their strategy for AI search.

**Secondary audience:** Content ops professionals building or rebuilding content systems for AI-era visibility.

**Not for:** Complete beginners to SEO or content marketing. This playbook assumes foundational knowledge and focuses on adaptation, not fundamentals.

---

## Playbook Structure

### Introduction: The Search Shift No One Is Ready For

**Core argument:** Traditional SEO optimized for one outcome — a blue-link click from Google. That outcome is collapsing. 68% of searches end without a click. AI Overviews reduce CTR by ~60%. The goal has shifted from earning a click to being the answer the machine trusts.

**What this means:** Content teams that built for traffic will need to rebuild for visibility, citation, and entity authority. The skills transfer — but the orientation does not.

**Key data to open with:**

- 68% of Google searches end without a click (SparkToro, 2026)
- AI Overviews cut CTR by ~60%
- AI traffic converts 34% better than organic (49% in B2B) — lower volume, higher quality
- 182% increase in branded search within one week of an LLM recommendation

**Tone:** Direct. Not alarmist — the fundamentals still matter. But the framing has to shift.

**Supporting sources:** Amanda Natividad, Ross Hudgens, Eli Schwartz, Bernard Huang

---

### Chapter 1: Understand How AI Search Works

**Why this chapter exists:** Most content teams are optimizing for AI search without understanding how AI actually retrieves and generates answers. This creates blind spots — tactics applied in the wrong context, metrics that measure the wrong things.

**What to cover:**

**1.1 How AI retrieves information (Grounding)**
AI models do not just use training data. They retrieve real-time information from the web to verify and supplement internal knowledge before generating a response. This process — grounding — is where content strategy intersects with AI output.
_Sources: Aleyda Solis (LinkedIn), Clearscope panel_

**1.2 How AI reasons across fan-out queries**
A single user prompt triggers multiple sub-queries. AI breaks complex questions into components, researches each, and synthesizes an answer. Pages that appear across multiple fan-out queries are 161% more likely to be cited.
_Sources: Cyrus Shepard, Bernard Huang, Chima Mmeje_

**1.3 The entity model — how AI thinks about brands**
AI does not see your brand as a domain. It sees it as an entity — a node in a knowledge graph with associations to topics, concepts, and other entities. These associations are built from what the broader web says about you, not what you say about yourself.
_Sources: Lily Ray, Chima Mmeje, Aleyda Solis_

**1.4 Citation vs. recommendation — why the difference matters**
Being cited as a source and being recommended to a user are two different outcomes. Lily Ray's research shows that self-promotional listicles get cited as sources while competitors get the actual recommendation 69% of the time.
_Sources: Lily Ray (LinkedIn, June 2026)_

**1.5 What AI crawlers can and cannot see**
US AI assistants (ChatGPT, Gemini, Claude, Perplexity, Copilot) read raw HTML only — JavaScript-rendered content is invisible. Content in accordions, tabs, or lazy-loaded sections effectively does not exist for these crawlers.
_Sources: Aleyda Solis (LinkedIn, June 2026)_

---

### Chapter 2: Audit Your Current AI Visibility

**Why this chapter exists:** Before changing anything, teams need a baseline. Most have no idea how AI currently represents their brand — which queries trigger citations, what competitive set AI places them in, and where the gaps are.

**What to cover:**

**2.1 Run an AI visibility diagnostic**
Use HubSpot's AEO Grader as a free starting point. Record: how AI describes the brand, which competitors AI groups you with, which queries you appear in, which you don't.
_Tool: HubSpot AEO Grader_
_Sources: Amanda Natividad (LinkedIn + Zero Click Marketing podcast)_

**2.2 Test across platforms**
Run the same brand query through ChatGPT, Gemini, Perplexity, and Claude separately. Results differ significantly by platform. SparkToro had 24% share of voice in ChatGPT/Perplexity but only 12.5% in Gemini.
_Sources: Amanda Natividad_

**2.3 Set up Bing Webmaster Tools AI Performance**
Only platform currently providing structured citation data to publishers. Track: grounding queries, citation share, intent classification, topic clusters.
_Tool: Bing Webmaster Tools_
_Sources: Aleyda Solis (LinkedIn, June 2026)_

**2.4 Establish proxy metrics in Google Search Console**
Branded impressions and branded search lift in GSC are the most accessible proxy for AI mention activity — since LLM recommendations typically manifest as branded searches.
_Tool: Google Search Console_
_Sources: Chima Mmeje, Aleyda Solis_

**2.5 Add self-attribution to your conversion flow**
Add a "How did you hear about us?" field to every form. This is the only reliable method for capturing AI-referred conversions that appear as direct traffic in GA4.
_Sources: Ross Hudgens, Eli Schwartz, Amanda Natividad, Aleyda Solis_

---

### Chapter 3: Build Your Entity Foundation

**Why this chapter exists:** AI visibility starts with entity recognition. If AI does not have a clear, consistent understanding of what your brand is, who it serves, and what it is authoritative about, it cannot reliably cite you — regardless of content volume or quality.

**What to cover:**

**3.1 Define your entity**
Choose a specific, ownable concept to associate your brand with. Not "marketing software" — something narrower and more defensible. FreshBooks owns "invoicing for small businesses." Exploding Topics owns "early trend detection."
_Sources: Semrush GEO video, Ahrefs GEO panel_

**3.2 Build entity surfaces on your own site**
Create 7–8 dedicated pages for AI training: About page, Team page, Careers page, Awards page, Press page, Customer Reviews page. These pages tell AI what your brand is, who is behind it, and why it should be trusted.
_Sources: Cyrus Shepard (LLM Mastery podcast)_

**3.3 Standardize your brand narrative across all channels**
Ensure core brand facts — what you do, who you serve, your key differentiators — are identical across your website, LinkedIn, YouTube, and any other indexed channel. Inconsistency confuses AI's entity model.
_Sources: Chima Mmeje (Moz Whiteboard Friday)_

**3.4 Seed your entity on third-party sources**
AI builds entity associations from what the broader web says — not what you say. Prioritize: podcast mentions, analyst citations, YouTube collaborations, industry publication features, and community references. Each independent mention reinforces the entity association.
_Sources: Kevin Indig, Nathan Gotch, Lily Ray_

**3.5 Analyze the reasoning chain**
Use Google AI Studio to prompt your core topic, fold down the thinking component, and identify the sub-themes AI uses to research the question. Build content for the sub-themes that appear most frequently.
_Tool: Google AI Studio_
_Sources: Bernard Huang (Siege Media podcast)_

---

### Chapter 4: Structure Content for AI Extraction

**Why this chapter exists:** Content that AI cannot extract cannot be cited. Structure is a prerequisite for visibility — before voice, depth, or keyword strategy matter.

**What to cover:**

**4.1 Answer first, explain second**
Place the direct answer to the page's primary question in the first 1–2 sentences. Do not warm up. Do not preamble. AI retrieves from the top of the page first.
_Sources: Cyrus Shepard, Chima Mmeje, Kevin Indig, Brian Dean_

**4.2 Write passage-ready content**
Structure each section so that a single passage can be extracted and restated accurately without surrounding context. Every H2 and H3 should be independently understandable.
_Sources: Chima Mmeje, Bernard Huang_

**4.3 Use plain visible text for critical information**
No accordions. No tabs. No JavaScript-rendered content for anything you want AI to find. Product data, pricing, FAQs, and key facts must be in raw HTML.
_Sources: Aleyda Solis, Chima Mmeje, Kevin Indig_

**4.4 Implement schema for clarity, not as a shortcut**
Structured data helps AI understand the meaning and relationships of content — particularly for product, pricing, availability, and entity data. It does not substitute for genuine authority.
_Sources: Chima Mmeje, Bernard Huang, Eli Schwartz_

**4.5 Map content to intent at a granular level**
Build entity clusters mapped to specific intents: Awareness, Comparison, Evaluation, Decision. Each intent requires a different content structure. Use pillar-spoke internal linking with bidirectional links between pillar and spoke pages.
_Sources: Chima Mmeje (Moz Whiteboard Friday)_

**4.6 Optimize for fan-out queries**
Identify the sub-queries AI generates around your primary topic. Use Cyrus Shepard's 5-step fan-out framework: identify a keyword you rank for → find fan-out queries → determine the most important → optimize or create pages for them → measure citation results.
_Sources: Cyrus Shepard (LinkedIn + LLM Mastery podcast)_

---

### Chapter 5: Build Off-Property Authority

**Why this chapter exists:** On-page optimization is the floor, not the ceiling. The brands winning in AI search — Nike, Apple, HubSpot — are winning because of what the broader web says about them, not because of what their own pages say. Third-party validation is the new backlink.

**What to cover:**

**5.1 Identify your citation sources**
Run AI answer reports over 2–3 months to find the 5–7 URLs that AI consistently cites for your target queries. These are your priority targets for brand inclusion.
_Sources: Nathan Gotch_

**5.2 Get into the sources that already rank**
Contact the owners of consistently-cited third-party URLs — listicles, review sites, comparison pages, directories — and work to get your brand included. This is more efficient than creating new content.
_Sources: Nathan Gotch, Kevin Indig_

**5.3 Build YouTube presence**
YouTube transcripts are the highest-leverage single investment for AI visibility across all sources. A 10-minute video functions like a 2,000-word naturally-worded article for AI training purposes. Prioritize: brand mentions in transcripts, consistent terminology, video about the brand's core entity.
_Sources: Kevin Indig, Ahrefs GEO panel, Cyrus Shepard_

**5.4 Engage authentically on Reddit**
Reddit threads rank for target keywords and AI models index them heavily. Participate in relevant discussions helpfully — not to seed links, but to establish brand presence in the conversations AI uses for grounding.
_Sources: Kevin Indig, Bernard Huang, Cyrus Shepard_

**5.5 Use reactive and proactive PR for citations**
Prepare expert quotes in advance for predictable news events. Be the first to respond when journalists need expert comment. Each publication feature adds an independent citation that reinforces entity authority.
_Sources: Lily Ray (BuzzStream podcast)_

**5.6 Publish original data — the Data Flywheel**
Proprietary research generates the citations that AI cannot synthesize from anywhere else. Recurly's 1,200-business dataset, NerdWallet's rate data, Serious Eats' original product testing — these create reference assets that become permanent citation sources.
_Sources: Lily Ray, Recurly case study, Surfer Academy_

---

### Chapter 6: Produce Non-Commodity Content

**Why this chapter exists:** AI can synthesize any information that already exists on the web. Content that merely restates known information is structurally expendable. The content that survives is the content AI cannot produce from existing sources.

**What to cover:**

**6.1 Identify what makes content non-commodity**
Five signals: first-person experience, proprietary data, original testing with documentation, genuine expert opinion, and interactive tools that require user presence. Any content with at least one of these signals is harder for AI to replace.
_Sources: Ryan Law, Cyrus Shepard, Surfer Academy_

**6.2 Document E-E-A-T with proof**
Photographs of products being tested. Video of the team at work. Named authors with verifiable credentials. Specific dates on which testing occurred. These signals cannot be fabricated at scale — which is exactly why they matter.
_Sources: Lily Ray, Surfer Academy, RickSteves.com case study_

**6.3 Generate proprietary data**
Survey a minimum of 50 people from your email list or customer base to create original data sets. Publish the findings. Run it as a recurring report. The data you own exclusively is the most defensible AI-era content asset.
_Sources: Surfer Academy, Recurly case study_

**6.4 Build interactive tools into content**
Calculators, scorecards, checklists, click-through demos, and product configurators convert informational pages into destinations. Users stay. Engagement signals strengthen. AI cannot replace a functioning tool with a text summary.
_Sources: Walnut.io case study, Surfer Academy_

**6.5 Create niche comparison content**
"[Product] alternative for [specific user type]" content performs significantly better in AI retrieval than generic comparisons. FreshBooks' invoicing content for specific professions, not general accounting.
_Sources: FreshBooks case study, Ahrefs GEO panel_

**6.6 Use vibe-writing for human voice**
Ryan Law's process at Ahrefs: speak or write loosely and conversationally to an AI agent, let it impose structure and identify gaps, then edit hard for voice and accuracy. The output carries genuine human perspective while benefiting from AI's structural capabilities. Keyword idea to published article in 91 minutes.
_Sources: Ryan Law (LinkedIn, June 2026)_

---

### Chapter 7: Maintain and Refresh Existing Content

**Why this chapter exists:** For established sites, content maintenance delivers higher ROI than new content production. AI models favor fresh content — but "fresh" means substantively updated, not just redated.

**What to cover:**

**7.1 Establish a 6-month audit cadence**
Use an SEO tool to audit your top 3–5 trafficked pages every six months. If a page has not been updated in that period, update it now.
_Sources: Surfer Academy (NerdWallet case study)_

**7.2 What counts as a substantive update**
New data. Updated rates, statistics, or product information. Additional expert commentary. Expanded sections covering new subtopics. New original photography or testing. Changing the date without changing the content is not a substantive update — and AI models are increasingly good at detecting it.
_Sources: Kevin Indig, Lily Ray, Bernard Huang_

**7.3 Automate the drudgery**
Ryan Law's Ahrefs pipeline: automated tasks pull fresh data from API endpoints monthly, generate updated charts and tables, insert updates into WordPress drafts, and email the team for review. The human reviews and approves — the machine handles the mechanical refresh.
_Tool: Claude + Ahrefs API + WordPress_
_Sources: Ryan Law (LinkedIn, June 2026)_

**7.4 Build internal linking pyramids**
Structure: a "best of" pillar article at the top, supported by individual review or detail pages for every item mentioned. Bidirectional links between pillar and spokes. Each update to the pyramid strengthens the whole structure.
_Sources: Serious Eats case study, Surfer Academy_

---

### Chapter 8: Measure What Actually Matters

**Why this chapter exists:** Standard analytics platforms systematically undercount AI search impact. AI referrals appear as direct or organic traffic. Branded search lifts go unattributed. Teams conclude AI search is not working when it is — they just cannot see it.

**What to cover:**

**8.1 Aleyda Solis's 4-layer attribution model**
Split AI impact metrics by confidence layer:

- **Observed:** Direct AI referrals and conversion paths you can measure
- **Own proxy:** Branded search lift, direct demand increase, surfaced-page demand
- **Third-party proxy:** AI traffic share estimates, prompt samples, competitive benchmarks
- **Modelled:** Pipeline or revenue estimates influenced by AI — useful for planning, not proof

Never report AI impact as a single blended number. Each layer tells a different story.
_Sources: Aleyda Solis (LinkedIn, June 2026)_

**8.2 Replace traffic as north star**
Traffic is declining structurally — not because strategy is failing but because AI is answering more queries directly. Replace traffic as the primary KPI with a correlation dashboard: branded search lift + direct traffic trends + self-attribution data + AI citation share.
_Sources: Ross Hudgens, Chima Mmeje, Amanda Natividad_

**8.3 Track citation share in Bing Webmaster Tools**
The only platform providing structured citation data. Monitor which grounding queries trigger your site, your citation share per query, and how intent classification maps to your content structure.
_Tool: Bing Webmaster Tools_
_Sources: Aleyda Solis_

**8.4 Run the same brand query across platforms monthly**
Manual check: ChatGPT, Gemini, Perplexity, Claude. How is the brand described? What competitive set does AI place you in? Has the description improved since last month? Has the competitive set changed?
_Sources: Amanda Natividad, SparkToro case study_

**8.5 Price the value of a citation**
HubSpot built a methodology to price what a single AI citation is worth and plugged it into their affiliate bidding strategy. Most teams do not know what a citation is worth to them — which makes prioritization arbitrary.
_Sources: Ross Hudgens (Content and Conversation, June 2026)_

---

### Chapter 9: Segmentation — Strategy by Company Type

**Why this chapter exists:** AI search behaves differently across business models. B2B content marketing drives significantly more LLM clicks than B2C. Local businesses need GBP more than blog content. Publishers face a structural threat that product companies do not.

**What to cover:**

**9.1 B2B SaaS**
Editorial and blog sections drive 25%+ of LLM clicks in B2B. BOFU content — alternatives, comparisons, "best X software" — is cited most frequently. Organize teams around product LLM visibility, not website sections. Price citation value into affiliate and PR strategy.
_Case studies: HubSpot, FreshBooks, Coinbase, Tinder, Recurly_
_Data: Ross Hudgens (77-site study — B2B LLM clicks 25%+ of total)_

**9.2 E-Commerce and D2C**
Editorial content drives only 7% of LLM clicks for B2C. Influence comes from affiliate sites, product pages, and third-party reviews — not brand blogs. Prioritize: Amazon presence, YouTube brand mentions, Reddit review threads, influencer coverage.
_Case studies: Nike, Apple, True Beauty_
_Data: Ross Hudgens (B2C editorial LLM clicks = 7%)_

**9.3 Local Business**
Google Business Profile and review volume are the primary drivers of AI visibility for local queries. Traditional website SEO plays a secondary role. For queries that go beyond Google (ChatGPT, Perplexity), third-party directory optimization becomes the primary visibility lever.
_Case studies: Kanner Injury Law_
_Sources: Nathan Gotch_

**9.4 Content Publishers and Media**
Structurally most exposed to AI traffic collapse. Bernard Huang's anonymous publisher site went from thousands of daily readers to near-zero. Survival requires: owned audience channels (newsletter, community), proprietary data that cannot be synthesized, and interactive tools that require user presence.
_Case studies: RickSteves.com (success), NerdWallet, Serious Eats, Bernard Huang site (cautionary)_

---

### Chapter 10: Avoid the Traps

**Why this chapter exists:** Several tactics are working now that practitioners expect will be penalized. Teams that build on these tactics face a Penguin-style correction. The playbook should help readers distinguish between durable strategies and short-term hacks.

**What to cover:**

**10.1 The self-promotional listicle trap**
Publishing "best [category]" content naming yourself #1 gets you cited as a source 69% of the time — while your competitors get the recommendation. You have published the case for your competition and paid for the content.
_Sources: Lily Ray (LinkedIn, June 2026)_

**10.2 Scaling commodity AI content**
Pumping out AI-generated content at volume without editorial standards creates "slop" — content that looks right but carries no genuine value. Google and AI systems are increasingly penalizing commodity content at scale. The May 2026 core update hit sites running this strategy.
_Sources: Ryan Law, Cyrus Shepard, Nathan Gotch_

**10.3 Artificial content freshness**
Changing a date on a page without changing the content is detectable. AI models have signals for genuine freshness vs. cosmetic freshness. NerdWallet's strategy works because they update actual data — not because they update timestamps.
_Sources: Kevin Indig, Lily Ray_

**10.4 JavaScript-dependent content strategy**
If critical content requires JavaScript rendering to be visible, it does not exist for US AI crawlers. Teams investing in dynamic content experiences without ensuring HTML fallbacks are building visibility that AI cannot see.
_Sources: Aleyda Solis_

**10.5 Waiting for AI attribution to appear in GA**
AI referrals appear as direct or organic traffic in GA4. Teams that conclude "AI search isn't sending us traffic" based on GA4 data are measuring the wrong thing. Without self-attribution and Bing Webmaster Tools data, the impact is invisible.
_Sources: Ross Hudgens, Eli Schwartz, Aleyda Solis_

---

### Appendix A: Quick-Start Checklist

For teams starting from zero — the minimum viable implementation in priority order:

- [ ] Run HubSpot AEO Grader audit and document baseline
- [ ] Add self-attribution field to all conversion forms
- [ ] Set up Bing Webmaster Tools and enable AI Performance report
- [ ] Audit top 5 pages for JavaScript-rendered content — move critical content to HTML
- [ ] Add direct answer in first 1–2 sentences of every page
- [ ] Create or update: About, Team, Press, and Reviews pages
- [ ] Identify 3–5 consistently-cited third-party URLs for your target queries
- [ ] Publish one piece of proprietary data (survey 50 customers minimum)
- [ ] Standardize brand narrative across website, LinkedIn, and YouTube
- [ ] Start a YouTube presence or secure one brand mention on an existing channel

---

### Appendix B: Measurement Dashboard Template

| Metric                              | Source                | Frequency | Baseline | Current |
| ----------------------------------- | --------------------- | --------- | -------- | ------- |
| Branded search impressions          | Google Search Console | Monthly   | —        | —       |
| Direct traffic trend                | GA4                   | Monthly   | —        | —       |
| Self-attribution: AI mentions       | Conversion forms      | Monthly   | —        | —       |
| AI citation share (primary queries) | Bing Webmaster Tools  | Monthly   | —        | —       |
| Brand description accuracy          | Manual AI query       | Monthly   | —        | —       |
| AI competitive set                  | Manual AI query       | Quarterly | —        | —       |
| Share of voice by platform          | HubSpot AEO Grader    | Quarterly | —        | —       |

---

### Appendix C: Supporting Research Files

All claims in this playbook are traceable to primary source material in this repository:

- `/research/sources.md` — Expert list with annotations and rationale
- `/research/linkedin-posts/` — 30 posts from 10 experts (3 per expert)
- `/research/youtube-transcripts/` — 15 video transcripts (438–12,871 words each)
- `/research/other/key-insights.md` — 7-section synthesis across all 25 sources
- `/research/other/glossary.md` — 20 practitioner terms defined
- `/research/other/case-studies.md` — 20 brand case studies with approaches and outcomes
- `/research/other/tool-stack.md` — 30+ tools categorized by function

---

_Playbook outline compiled by Titash Sinha. Built from 25 practitioner sources (2025–2026). Synthesized using NotebookLM, structured and refined with Claude._
