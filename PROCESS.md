# Process Log — 100Hires Portfolio Project

A transparent record of key decisions, approaches, and course corrections made during this research project. Written to show thinking in motion, not just final outputs.

---

## Expert Selection

**Decision:** Build a list of 10 practitioners rather than a list of 10 influencers.

The first instinct was to search "top SEO experts 2026" and work from there. That search returns Neil Patel, Zeeshan Yaseen, and India-focused generalists — recognizable names but not necessarily the people actively doing AI search work in 2026. Instead, the list was built from a three-point vetting framework: active practitioner role, recent content specifically covering AI search or GEO/AEO, and peer citation by others in the field.

The peer citation criterion turned out to be the most useful filter. When I found that Chima Mmeje cites Lily Ray directly in her Moz content, that Eli Schwartz and Kevin Indig co-host a podcast, and that Eli and Ross Hudgens appeared together in May 2026, the list stopped being 10 individual choices and became a coherent peer cluster. That's a stronger signal than any individual follower count.

Bernard Huang was initially flagged as a risk — he left Clearscope in May 2026 and was pivoting to autonomous AI businesses. Decision to keep him: his exit from a content optimization product _toward_ AI-native tooling makes his current thinking more forward-looking than most on the list, not less relevant.

All 10 experts confirmed active and publishing in 2026 before finalizing the list.

---

## LinkedIn Post Collection

**Decision:** Use Perplexity web search rather than direct scraping.

LinkedIn prohibits automated data extraction under its Terms of Service. Scraping was not a viable option. Perplexity's web search was used to locate recent posts from each expert's LinkedIn profile. Every post collected was then manually opened, verified, and copied verbatim — not summarized or paraphrased. Posts were vetted individually for relevance: only posts directly covering AI search, GEO, AEO, content strategy, or AI content production were kept. Personal news, event announcements, and generic marketing posts were discarded.

One expert (Amanda Natividad) initially returned only one strong relevant post. Two additional relevant posts were sourced on a second pass before including her in the final set.

---

## YouTube Video Selection and Verification

**Decision:** Expand beyond the 10 LinkedIn experts to include channel-level sources for YouTube.

Several experts on the LinkedIn list (Kevin Indig, Eli Schwartz, Cyrus Shepard) do not have dedicated YouTube channels. Rather than chase scattered guest appearances, the decision was made to include high-authority channels — Ahrefs, Moz, Siege Media, Semrush — where these practitioners regularly appear, and to supplement with dedicated channels (Lily Ray, Amanda Natividad's Zero Click Marketing, Aleyda Solis's Crawling Mondays).

Every YouTube URL was manually verified before transcript collection — clicked, confirmed the video existed and matched the described title. Two initial batches of Perplexity-sourced URLs were returned with formatting artifacts ("youtube" appended to the end of URLs) and one duplicate that had been counted twice. Both issues were caught during manual verification.

The Contrarian Marketing podcast (Kevin Indig + Eli Schwartz) was initially targeted as a YouTube source. Perplexity confirmed no YouTube uploads exist for that show — episodes live on Substack and audio platforms only. Rather than fabricate or approximate, those two slots were replaced with verified alternatives (Semrush and LLM Mastery channels).

Final result: 15 videos, all URLs confirmed, all transcripts successfully retrieved.

---

## Transcript Collection

**Decision:** Use Supadata API via a Python script for programmatic retrieval.

The Supadata YouTube Transcript API was used rather than manual transcript copying because at 15 videos — some over an hour long — manual copying would introduce errors and was not a realistic option. A Python script was written to loop through all 15 URLs, call the API, and save each transcript as a structured .md file with metadata (title, channel, date, URL) at the top.

15/15 transcripts retrieved successfully. None required fallback handling. Word counts ranged from ~438 words (Moz Whiteboard Friday format) to ~12,871 words (Eli Schwartz long-form podcast interview). Full text preserved without summarization.

The script was used during the research process and added to the `/scripts/` folder in the repo as a reproducible artifact.

---

## Synthesis Approach

**Decision:** Use NotebookLM for cross-source synthesis, then refine with Claude.

With 25 sources (10 LinkedIn post collections + 15 YouTube transcripts), manual synthesis across all sources simultaneously was not practical. All files were loaded into NotebookLM for structured cross-source analysis. Two separate prompts were used:

1. A broad synthesis prompt covering themes, consensus, contradictions, tactics frequency, statistics, vocabulary, principles, and open questions
2. A targeted extraction prompt focused specifically on implementation steps and how-to sequences from the YouTube transcripts

The raw NotebookLM output was then refined using Claude — attribution was tightened, loose source references were corrected, one unverifiable statistic was removed, terminology was standardized, and the language was elevated from synthesis notes to publication-quality analysis.

Case studies, tool stack, and playbook outline were built directly from the extracted material without an additional NotebookLM pass.

---

## What Didn't Work

**Contrarian Marketing YouTube channel:** Targeted as a source, confirmed unavailable on YouTube. Replaced.

**First LinkedIn batch for Amanda Natividad:** Initial Perplexity results returned mostly personal brand content and one sponsored post. Required a second targeted pass to find relevant AI visibility material.

**Initial YouTube URL batch:** Perplexity returned two Crawling Mondays news roundup videos (#SEOFOMO format) that looked relevant by title but were shallow weekly digests with no substantive educational content. Both were dropped and replaced with a single deeper tutorial from the same channel.

---

_Process log written by Titash Sinha. Dates omitted from entries as the log was compiled at the close of the research phase rather than maintained as a running diary — but the sequence of decisions above reflects the actual order in which they were made._
