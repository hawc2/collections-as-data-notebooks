"""Fetch genre/subgenre data from Worlds Without End for volumes with WWEnd IDs.
Run standalone: python fetch_genres.py
Saves to data/wwend_genres.json with incremental checkpoints.
"""
import requests
import pandas as pd
import json
import time
import re
import os
import sys

WORKSET_FILE = "data/sf-hathitrust-volumes.tsv"
GENRE_CACHE = "data/wwend_genres.json"
HEADERS = {'User-Agent': 'Mozilla/5.0 (academic research; Temple University DH)'}

def fetch_wwend_genre(wwend_id):
    """Fetch genre and sub-genre tags from a WWEnd novel page."""
    url = f"https://www.worldswithoutend.com/novel.asp?ID={int(wwend_id)}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code != 200:
            return None
    except requests.RequestException:
        return None

    text = resp.text
    result = {}

    # Extract genre
    idx = text.find('Genre:')
    if idx >= 0:
        chunk = text[idx:idx+300]
        clean = re.sub(r'<[^>]+>', '|', chunk)
        parts = [p.strip() for p in clean.split('|') if p.strip() and p.strip() != 'Genre:']
        if parts:
            result['genre'] = parts[0]

    # Extract sub-genre tags
    idx = text.find('Sub-Genre Tags')
    if idx >= 0:
        chunk = text[idx:idx+500]
        clean = re.sub(r'<[^>]+>', '|', chunk)
        parts = [p.strip() for p in clean.split('|')
                 if p.strip() and p.strip() not in ('Sub-Genre Tags', ':', 'Sub-Genre Tags :')]
        result['subgenres'] = parts

    # Extract awards
    idx = text.find('Awards:')
    if idx >= 0:
        chunk = text[idx:idx+500]
        clean = re.sub(r'<[^>]+>', '|', chunk)
        parts = [p.strip() for p in clean.split('|')
                 if p.strip() and p.strip() != 'Awards:'
                 and any(kw in p for kw in ['Winner', 'Nominee', 'Shortlist', 'Award'])]
        result['awards'] = parts

    return result if result else None


def main():
    scifi = pd.read_csv(WORKSET_FILE, sep='\t')

    # Get unique WWEnd IDs
    wwend_ids = scifi['WWEnd ID'].dropna().unique()
    print(f"Unique WWEnd IDs: {len(wwend_ids)}")

    if os.path.exists(GENRE_CACHE):
        with open(GENRE_CACHE) as f:
            all_genres = json.load(f)
    else:
        all_genres = {}

    missing = [int(wid) for wid in wwend_ids if str(int(wid)) not in all_genres]
    print(f"Cached: {len(all_genres)}, Missing: {len(missing)}")

    if not missing:
        print("All genre data already cached.")
        return

    errors = 0
    for i, wid in enumerate(missing):
        genre_data = fetch_wwend_genre(wid)
        if genre_data:
            all_genres[str(wid)] = genre_data
        else:
            errors += 1

        if (i + 1) % 25 == 0:
            with open(GENRE_CACHE, 'w') as f:
                json.dump(all_genres, f, indent=1)
            print(f"  {i + 1}/{len(missing)} ({(i+1)/len(missing)*100:.1f}%) -- {errors} errors")
            sys.stdout.flush()

        time.sleep(1.5)  # be respectful to WWEnd

    with open(GENRE_CACHE, 'w') as f:
        json.dump(all_genres, f, indent=1)

    print(f"\nDone. Cached: {len(all_genres)}, Errors: {errors}")


if __name__ == '__main__':
    main()
