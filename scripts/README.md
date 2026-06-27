# Scripts

## fetch-transcripts.ps1

Fetches YouTube transcripts for all 15 research videos via the [Supadata API](https://supadata.ai) and saves them as markdown files in `research/youtube-transcripts/`.

### Requirements

- Windows PowerShell 5.1+ (pre-installed on Windows 10/11)
- A Supadata API key

### Run it

Open a terminal in the project root and run:

```powershell
.\scripts\fetch-transcripts.ps1 -ApiKey "your_api_key_here"
```

Or set the key as an environment variable first, then run without the flag:

```powershell
$env:SUPADATA_API_KEY = "your_api_key_here"
.\scripts\fetch-transcripts.ps1
```

### What it does

1. Calls `https://api.supadata.ai/v1/youtube/transcript?url={url}&text=true` for each video
2. Saves the full transcript text (no summarization) to `research/youtube-transcripts/NN-slug.md`
3. If a transcript is unavailable, writes `"Transcript unavailable via Supadata."` instead and continues
4. Prints a success/fail count when done

### To add or change videos

Edit the `$videos` array near the top of `fetch-transcripts.ps1`. Each entry needs: `num`, `slug`, `title`, `channel`, and `url`.
