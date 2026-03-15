"""Fetch EF API metadata for all volumes in the expanded workset.
Run standalone: python fetch_metadata.py
Saves incremental checkpoints to data/scifi_metadata.json
"""
import requests
import pandas as pd
import json
import time
import os
import sys

EF_API = "https://data.htrc.illinois.edu/ef-api/volumes"
METADATA_CACHE = "data/scifi_metadata.json"
WORKSET_FILE = "data/sf-hathitrust-volumes.tsv"

def clean_htid(htid):
    return htid.replace(':', '+').replace('/', '=')

def fetch_metadata(htid):
    url = f"{EF_API}/{clean_htid(htid)}?fields=metadata"
    try:
        resp = requests.get(url, headers={'Accept': 'application/json'}, timeout=30)
        if resp.status_code == 200:
            return resp.json().get('data', {}).get('metadata', {})
    except requests.RequestException as e:
        print(f"  Error fetching {htid}: {e}", file=sys.stderr)
    return None

def main():
    scifi = pd.read_csv(WORKSET_FILE, sep='\t')
    print(f"Workset: {len(scifi)} volumes")

    if os.path.exists(METADATA_CACHE):
        with open(METADATA_CACHE) as f:
            all_metadata = json.load(f)
    else:
        all_metadata = {}

    missing = [htid for htid in scifi['htid'] if htid not in all_metadata]
    print(f"Cached: {len(all_metadata)}, Missing: {len(missing)}")

    if not missing:
        print("All metadata already cached.")
        return

    errors = []
    for i, htid in enumerate(missing):
        meta = fetch_metadata(htid)
        if meta:
            all_metadata[htid] = meta
        else:
            errors.append(htid)

        if (i + 1) % 50 == 0:
            with open(METADATA_CACHE, 'w') as f:
                json.dump(all_metadata, f)
            elapsed_pct = (i + 1) / len(missing) * 100
            print(f"  {i + 1}/{len(missing)} ({elapsed_pct:.1f}%) -- {len(errors)} errors")
            sys.stdout.flush()

        time.sleep(0.5)

    # Final save
    with open(METADATA_CACHE, 'w') as f:
        json.dump(all_metadata, f)

    print(f"\nDone. Total: {len(all_metadata)}, New: {len(missing) - len(errors)}, Errors: {len(errors)}")
    if errors:
        with open('data/fetch_errors.txt', 'w') as f:
            f.write('\n'.join(errors))
        print(f"Failed IDs saved to data/fetch_errors.txt")

if __name__ == '__main__':
    main()
