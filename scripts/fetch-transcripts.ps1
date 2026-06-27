# fetch-transcripts.ps1
# Fetches YouTube transcripts via Supadata API and saves them as markdown files.
# Usage: see scripts/README.md

param(
  [string]$ApiKey = $env:SUPADATA_API_KEY,
  [string]$OutputDir = "$PSScriptRoot\..\research\youtube-transcripts"
)

if (-not $ApiKey) {
  Write-Error "No API key provided. Pass -ApiKey or set SUPADATA_API_KEY environment variable."
  exit 1
}

$videos = @(
  @{ num="01"; slug="semrush-seo-playbook";               title="The SEO Playbook: A NEW System for 2026";                   channel="Semrush";                                          url="https://www.youtube.com/watch?v=oxkykvTcN_Y" },
  @{ num="02"; slug="semrush-seo-framework";              title="The SEO Framework Everyone Gets Wrong in 2026";             channel="Semrush";                                          url="https://www.youtube.com/watch?v=eF5VYjZAjfE" },
  @{ num="03"; slug="llm-mastery-cyrus-shepard";          title="How to Rank in LLMs";                                       channel="LLM Mastery (Cyrus Shepard)";                      url="https://www.youtube.com/watch?v=cunYZ_Fp61s" },
  @{ num="04"; slug="content-and-conversation";           title="Google's GEO Advice";                                       channel="Content and Conversation (Eli Schwartz)";          url="https://www.youtube.com/watch?v=DSU67DOqljY" },
  @{ num="05"; slug="ahrefs";                             title="Top SEO Experts Build Me an AI Search Strategy";            channel="Ahrefs";                                           url="https://www.youtube.com/watch?v=RwKKLnyXCig" },
  @{ num="06"; slug="moz-chima-mmeje";                    title="Top SEO Tips For 2026";                                     channel="Moz (Chima Mmeje)";                                url="https://www.youtube.com/watch?v=iTttoPGAJoY" },
  @{ num="07"; slug="moz-jamie-indigo";                   title="Defensive SEO Strategy for AI Search";                      channel="Moz (Jamie Indigo)";                               url="https://www.youtube.com/watch?v=wO_Fz9LzC3Y" },
  @{ num="08"; slug="clearscope";                         title="Future of Search";                                          channel="Clearscope (Lily Ray, Kevin Indig, Ross Hudgens)"; url="https://www.youtube.com/watch?v=c-VtgjXWsK4" },
  @{ num="09"; slug="buzzstream-lily-ray";                title="AI Search Tactics That Will Bite You Later";                channel="BuzzStream (Lily Ray)";                            url="https://www.youtube.com/watch?v=i5bj1pgQLhA" },
  @{ num="10"; slug="zero-click-marketing-ai-visibility"; title="AI Visibility Is a Mirror";                                 channel="Zero Click Marketing (Amanda Natividad)";          url="https://www.youtube.com/watch?v=amYcMSNTZAs" },
  @{ num="11"; slug="zero-click-marketing-zero-click";    title="Zero Click Search Is Now the Norm";                         channel="Zero Click Marketing (Amanda Natividad)";          url="https://www.youtube.com/watch?v=yepb95llLro" },
  @{ num="12"; slug="siege-media-bernard-huang";          title="How GEO Actually Works";                                    channel="Siege Media (Bernard Huang)";                      url="https://www.youtube.com/watch?v=4KyYqe1s_XY" },
  @{ num="13"; slug="futurepedia";                        title="How to Get AI to Recommend Your Business";                  channel="Futurepedia";                                      url="https://www.youtube.com/watch?v=-5Drsq6ve7w" },
  @{ num="14"; slug="nathan-gotch";                       title="June 2026 Google Spam Update + AI Overviews";               channel="Nathan Gotch";                                     url="https://www.youtube.com/watch?v=kMsVDnFphRA" },
  @{ num="15"; slug="surfer-academy";                     title="The SEO Playbook That's Working in 2026";                   channel="Surfer Academy";                                   url="https://www.youtube.com/watch?v=A2oodPYUw_4" }
)

$headers = @{ "x-api-key" = $ApiKey }
$outputDir = [System.IO.Path]::GetFullPath($OutputDir)

if (-not (Test-Path $outputDir)) {
  New-Item -ItemType Directory -Force $outputDir | Out-Null
}

$succeeded = 0
$failed    = 0

foreach ($v in $videos) {
  $filename = "$($v.num)-$($v.slug).md"
  $filepath = Join-Path $outputDir $filename
  $apiUrl   = "https://api.supadata.ai/v1/youtube/transcript?url=$([uri]::EscapeDataString($v.url))&text=true"

  Write-Host "[$($v.num)/15] $($v.title)..." -NoNewline

  try {
    $resp       = Invoke-WebRequest -Uri $apiUrl -Headers $headers -UseBasicParsing -TimeoutSec 30
    $json       = $resp.Content | ConvertFrom-Json
    $transcript = if ($json.content) { $json.content }
                  elseif ($json.text) { $json.text }
                  elseif ($json.transcript) { ($json.transcript | ForEach-Object { $_.text }) -join " " }
                  else { "Transcript unavailable via Supadata." }
    $succeeded++
    Write-Host " OK"
  } catch {
    $transcript = "Transcript unavailable via Supadata."
    $failed++
    Write-Host " FAILED ($($_.Exception.Message))"
  }

  @"
# $($v.title)

**Channel:** $($v.channel)
**YouTube URL:** $($v.url)

---

$transcript
"@ | Out-File -FilePath $filepath -Encoding utf8
}

Write-Host ""
Write-Host "Done. $succeeded succeeded, $failed failed."
Write-Host "Files saved to: $outputDir"
