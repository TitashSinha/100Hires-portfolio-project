# Scripts

## fetch-transcripts.ps1

Fetches YouTube transcripts via the [Supadata API](https://supadata.ai) and saves them as markdown files in `research/youtube-transcripts/`.

### Requirements

- Windows PowerShell 5.1+ (pre-installed on Windows 10/11)
- A Supadata API key (free tier available)

### Getting a Supadata API key

1. Go to [supadata.ai](https://supadata.ai) and create a free account
2. In your dashboard, navigate to **API Keys**
3. Create a new key and copy it
4. Open `fetch-transcripts.ps1` and replace the value of `$apiKey` on line 5 with your key

### Running the script

Open PowerShell in the project root and run:

```powershell
.\scripts\fetch-transcripts.ps1
```

If you get an execution policy error, run this first (once per machine):

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### Adding new videos

In `fetch-transcripts.ps1`, add a new entry to the `$videos` array:

```powershell
@{ num="16"; slug="channel-name"; title="Video Title"; channel="Channel Name"; url="https://www.youtube.com/watch?v=XXXXX" }
```

The script will skip files that already exist — re-running it only fetches new entries.

> **Note:** If a video has no transcript available (private video, auto-captions disabled), the script creates the file with the text `Transcript unavailable via Supadata.` so the gap is visible in the folder.
