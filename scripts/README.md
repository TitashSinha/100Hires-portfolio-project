# Scripts

## fetch-transcripts.py

Fetches YouTube transcripts for all 15 research videos via the [Supadata API](https://supadata.ai) and saves them as markdown files in `research/youtube-transcripts/`.

Works on macOS, Windows, and Linux. No third-party libraries required — uses Python's standard library only.

### Requirements

- Python 3.7+
- A Supadata API key

### Run it

```bash
python scripts/fetch-transcripts.py --api-key "your_api_key_here"
```

Or set the key as an environment variable first:

```bash
# macOS / Linux
export SUPADATA_API_KEY="your_api_key_here"
python scripts/fetch-transcripts.py

# Windows (Command Prompt)
set SUPADATA_API_KEY=your_api_key_here
python scripts/fetch-transcripts.py

# Windows (PowerShell)
$env:SUPADATA_API_KEY = "your_api_key_here"
python scripts/fetch-transcripts.py
```

### Options

| Flag | Default | Description |
|------|---------|-------------|
| `--api-key` | `$SUPADATA_API_KEY` | Supadata API key |
| `--output-dir` | `research/youtube-transcripts/` | Where to write the markdown files |

### What it does

1. Calls `https://api.supadata.ai/v1/youtube/transcript?url={url}&text=true` for each video
2. Saves the full transcript text (no summarization) to `research/youtube-transcripts/NN-slug.md`
3. If a transcript is unavailable, writes `"Transcript unavailable via Supadata."` and continues
4. Prints a success/fail count when done

### To add or change videos

Edit the `VIDEOS` list near the top of `fetch-transcripts.py`. Each entry needs: `num`, `slug`, `title`, `channel`, and `url`.
