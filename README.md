# 100Hires Portfolio Project

## Step 1 - Environment Setup

### Tools Installed

- **Cursor IDE** - Already installed and in active daily use for content workflow and automation projects.
- **Claude Code** - Installed via Cursor Extensions (searched "Claude Code", installed, logged in).
- **Codex** - Installed via Cursor Extensions (searched "Codex", installed, logged in).
- **GitHub** - Existing account: [github.com/TitashSinha](https://github.com/TitashSinha). Multiple public repos including a full-stack content operations dashboard.

### Steps Completed

1. Confirmed Cursor IDE was installed and up to date
2. Added Claude Code extension via Cursor Extensions panel - logged in successfully
3. Added Codex extension via Cursor Extensions panel - logged in successfully
4. Created a public GitHub repository: `100hires-portfolio-project`
5. Cloned the repository locally via terminal (`git clone`)
6. Opened the folder in Cursor
7. Created this README.md file
8. Committed and pushed to GitHub

### Issues I Ran Into

No issues encountered. All steps completed as described.

---

## Step 2 - Research Project: AI-Powered SEO Content Production

### Topic Chosen

**Option 3 - AI-Powered SEO Content Production**

### Why This Topic

This maps directly to my active work - GEO, AEO, AI-assisted editorial workflows, and SEO content strategy. Choosing a topic I work in daily means I can evaluate sources with genuine judgment, not just collect them.

### Expert Selection Process

Identified 10 practitioners (not commentators) actively publishing on AI + SEO in 2025-2026. Each was vetted against three criteria:

1. Active practitioner role - agency, product, consultancy, or in-house
2. Recent content specifically covering AI search, GEO, AEO, or AI content production
3. Peer citation - referenced or collaborated with others in the field

The final list has strong internal citation density: Kevin Indig and Eli Schwartz co-host a podcast, Eli Schwartz and Ross Hudgens appeared together on a podcast episode in May 2026, Chima Mmeje cites Lily Ray's work directly, and Aleyda Solis and Lily Ray both contribute to Moz Whiteboard Friday. This is a peer cluster, not 10 isolated voices.

### Research Methodology

#### LinkedIn Posts

LinkedIn posts were collected using Perplexity's web search capabilities to locate recent posts from each expert's LinkedIn profile. Every post was then manually opened, verified, and copied verbatim — not summarized or paraphrased. Direct scraping was avoided as LinkedIn prohibits automated data extraction under its Terms of Service. Posts were then manually vetted for relevance — only posts directly covering AI search, GEO, AEO, content strategy, or AI content production workflows were retained. Off-topic posts (personal news, generic marketing advice, product launches unrelated to SEO) were discarded. Each post file includes a research note annotation explaining what specific insight the post contributes and which playbook chapter it supports.

#### YouTube Transcripts

YouTube videos were identified using Perplexity's web search capabilities. Each URL was manually verified before transcript collection. Transcripts were collected programmatically using the Supadata YouTube Transcript API via a Python script (`/scripts/fetch-transcripts.py`). All 15 videos returned transcripts successfully — none required fallback handling. Transcripts range from ~438 words (short Whiteboard Friday format) to ~12,871 words (long-form podcast interview). Full transcript text is preserved without summarization.

#### Synthesis

All 25 sources (10 LinkedIn post collections and 15 YouTube transcripts) were loaded into NotebookLM for cross-source synthesis. NotebookLM was used to identify dominant themes, surface expert consensus and contradiction, map recurring tactics, and extract key statistics. The raw synthesis output was then refined using Claude to improve accuracy, fix attribution, and elevate the quality of analysis. The resulting documents are in `/research/other/`.

### Repository Structure

/PROCESS.md - process log documenting key decisions, approaches, and course corrections

/scripts/fetch-transcripts.py - Python script used to collect YouTube transcripts via Supadata API

/research/sources.md - expert list with links, dates, annotations, and selection rationale

/research/linkedin-posts/ - 30 posts organized by author (3 per expert), manually vetted for relevance

/research/youtube-transcripts/ - 15 transcripts organized by video (438–12,871 words each)

/research/other/key-insights.md - 7-section synthesis: themes, consensus, tactics, data, principles, open questions

/research/other/glossary.md - 20 practitioner terms defined in active use as of mid-2026

/research/other/case-studies.md - 20 real-world brand examples with approaches, outcomes, and metrics

/research/other/tool-stack.md - 30+ tools categorized by function, with practitioner context

/research/other/playbook-outline.md - 10-chapter playbook outline with sources mapped to every section (outline only — full playbook not yet written)

### Experts Researched

1. Kevin Indig - Growth advisor (Hims, Toast, Reddit); co-host, Contrarian Marketing
2. Lily Ray - VP SEO Strategy, Amsive; founder, Algorythmic
3. Ross Hudgens - CEO, Siege Media; author of upcoming Wiley GEO book
4. Chima Mmeje - Freelance content strategist; Moz Whiteboard Friday contributor
5. Amanda Natividad - VP Marketing, SparkToro; coined "zero-click content"
6. Bernard Huang - Co-founder, Clearscope (exited May 2026); building autonomous AI businesses
7. Eli Schwartz - Independent SEO strategist; author, Product-Led SEO
8. Ryan Law - Head of Content, Ahrefs
9. Cyrus Shepard - Founder, Zyppy
10. Aleyda Solis - Founder, Orainti; Crawling Mondays YouTube series
