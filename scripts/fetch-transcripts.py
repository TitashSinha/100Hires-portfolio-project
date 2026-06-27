#!/usr/bin/env python3
"""
fetch-transcripts.py
Fetches YouTube transcripts via the Supadata API and saves them as markdown
files in research/youtube-transcripts/.

Usage: see scripts/README.md
"""

import argparse
import os
import sys
import urllib.parse
import urllib.request
import json
from pathlib import Path

VIDEOS = [
    {"num": "01", "slug": "semrush-seo-playbook",               "title": "The SEO Playbook: A NEW System for 2026",                   "channel": "Semrush",                                          "url": "https://www.youtube.com/watch?v=oxkykvTcN_Y"},
    {"num": "02", "slug": "semrush-seo-framework",              "title": "The SEO Framework Everyone Gets Wrong in 2026",             "channel": "Semrush",                                          "url": "https://www.youtube.com/watch?v=eF5VYjZAjfE"},
    {"num": "03", "slug": "llm-mastery-cyrus-shepard",          "title": "How to Rank in LLMs",                                       "channel": "LLM Mastery (Cyrus Shepard)",                      "url": "https://www.youtube.com/watch?v=cunYZ_Fp61s"},
    {"num": "04", "slug": "content-and-conversation",           "title": "Google's GEO Advice",                                       "channel": "Content and Conversation (Eli Schwartz)",          "url": "https://www.youtube.com/watch?v=DSU67DOqljY"},
    {"num": "05", "slug": "ahrefs",                             "title": "Top SEO Experts Build Me an AI Search Strategy",            "channel": "Ahrefs",                                           "url": "https://www.youtube.com/watch?v=RwKKLnyXCig"},
    {"num": "06", "slug": "moz-chima-mmeje",                    "title": "Top SEO Tips For 2026",                                     "channel": "Moz (Chima Mmeje)",                                "url": "https://www.youtube.com/watch?v=iTttoPGAJoY"},
    {"num": "07", "slug": "moz-jamie-indigo",                   "title": "Defensive SEO Strategy for AI Search",                      "channel": "Moz (Jamie Indigo)",                               "url": "https://www.youtube.com/watch?v=wO_Fz9LzC3Y"},
    {"num": "08", "slug": "clearscope",                         "title": "Future of Search",                                          "channel": "Clearscope (Lily Ray, Kevin Indig, Ross Hudgens)", "url": "https://www.youtube.com/watch?v=c-VtgjXWsK4"},
    {"num": "09", "slug": "buzzstream-lily-ray",                "title": "AI Search Tactics That Will Bite You Later",                "channel": "BuzzStream (Lily Ray)",                            "url": "https://www.youtube.com/watch?v=i5bj1pgQLhA"},
    {"num": "10", "slug": "zero-click-marketing-ai-visibility", "title": "AI Visibility Is a Mirror",                                 "channel": "Zero Click Marketing (Amanda Natividad)",          "url": "https://www.youtube.com/watch?v=amYcMSNTZAs"},
    {"num": "11", "slug": "zero-click-marketing-zero-click",    "title": "Zero Click Search Is Now the Norm",                         "channel": "Zero Click Marketing (Amanda Natividad)",          "url": "https://www.youtube.com/watch?v=yepb95llLro"},
    {"num": "12", "slug": "siege-media-bernard-huang",          "title": "How GEO Actually Works",                                    "channel": "Siege Media (Bernard Huang)",                      "url": "https://www.youtube.com/watch?v=4KyYqe1s_XY"},
    {"num": "13", "slug": "futurepedia",                        "title": "How to Get AI to Recommend Your Business",                  "channel": "Futurepedia",                                      "url": "https://www.youtube.com/watch?v=-5Drsq6ve7w"},
    {"num": "14", "slug": "nathan-gotch",                       "title": "June 2026 Google Spam Update + AI Overviews",               "channel": "Nathan Gotch",                                     "url": "https://www.youtube.com/watch?v=kMsVDnFphRA"},
    {"num": "15", "slug": "surfer-academy",                     "title": "The SEO Playbook That's Working in 2026",                   "channel": "Surfer Academy",                                   "url": "https://www.youtube.com/watch?v=A2oodPYUw_4"},
]


def fetch_transcript(video_url: str, api_key: str) -> str:
    encoded = urllib.parse.quote(video_url, safe="")
    api_url = f"https://api.supadata.ai/v1/youtube/transcript?url={encoded}&text=true"
    req = urllib.request.Request(api_url, headers={"x-api-key": api_key})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode())
    if data.get("content"):
        return data["content"]
    if data.get("text"):
        return data["text"]
    if data.get("transcript"):
        return " ".join(seg.get("text", "") for seg in data["transcript"])
    return "Transcript unavailable via Supadata."


def build_markdown(video: dict, transcript: str) -> str:
    return (
        f"# {video['title']}\n\n"
        f"**Channel:** {video['channel']}\n"
        f"**YouTube URL:** {video['url']}\n\n"
        f"---\n\n"
        f"{transcript}\n"
    )


def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube transcripts via Supadata API.")
    parser.add_argument("--api-key", default=os.environ.get("SUPADATA_API_KEY"), help="Supadata API key (or set SUPADATA_API_KEY env var)")
    parser.add_argument("--output-dir", default=None, help="Directory to write markdown files (default: research/youtube-transcripts/ relative to project root)")
    args = parser.parse_args()

    if not args.api_key:
        print("Error: no API key provided. Use --api-key or set SUPADATA_API_KEY.", file=sys.stderr)
        sys.exit(1)

    script_dir = Path(__file__).resolve().parent
    output_dir = Path(args.output_dir) if args.output_dir else script_dir.parent / "research" / "youtube-transcripts"
    output_dir.mkdir(parents=True, exist_ok=True)

    succeeded, failed = 0, 0

    for v in VIDEOS:
        filename = f"{v['num']}-{v['slug']}.md"
        filepath = output_dir / filename
        print(f"[{v['num']}/15] {v['title']}...", end=" ", flush=True)

        try:
            transcript = fetch_transcript(v["url"], args.api_key)
            succeeded += 1
            print("OK")
        except Exception as e:
            transcript = "Transcript unavailable via Supadata."
            failed += 1
            print(f"FAILED ({e})")

        filepath.write_text(build_markdown(v, transcript), encoding="utf-8")

    print(f"\nDone. {succeeded} succeeded, {failed} failed.")
    print(f"Files saved to: {output_dir}")


if __name__ == "__main__":
    main()
