# HTRC Feature Reader -- Within-Book Sentiment Trends

**Source:** [htrc/ef-workshop](https://github.com/htrc/ef-workshop) (improved version of the notebook from [htrc/htrc-feature-reader/examples](https://github.com/htrc/htrc-feature-reader/tree/master/examples))
**Status:** Stable -- runs standalone with bundled data
**Selected notebook:** `Within_Book_Sentiment_Trends.ipynb`

## What it does

Applies page-level sentiment analysis to James Joyce's *Portrait of the Artist as a Young Man* (1918 Egoist Press edition, OSU scan) using HathiTrust Extracted Features data. Uses the AFINN-111 word list to assign sentiment scores to each page's tokens, then plots emotional valence arcs using rolling means and LOWESS smoothing. Based on Matthew Jockers' syuzhet/sentiment arc methodology.

## Data included

The bundled data file (`data/osu.32435018220335.basic.json.bz2`, 134 KB) is the HathiTrust Extracted Features file for the Joyce novel. No network access is needed to run this notebook.

## V2.0 fixes applied

- Swapped in the `ef-workshop` version of the notebook (already has modern pandas `rolling().mean()` instead of removed `pd.rolling_mean()`)
- Replaced manual AFINN-111.txt download with `afinn` pip package (builds the same DataFrame programmatically)
- Bundled the EF data file so the notebook runs standalone

## Setup

```bash
pip install htrc-feature-reader statsmodels seaborn matplotlib afinn
```

Then run the notebook from this directory.

## HTRC infrastructure notes

**HTRC is being suspended at end of December 2026.** This notebook runs entirely on local data, so it is unaffected. For anyone wanting to access other HathiTrust volumes:

- The old HTTP endpoints (`data.analytics.hathitrust.org/features/` and `data.htrc.illinois.edu/htrc-ef-access/get`) are **dead** (404/503)
- The EF API at `https://data.htrc.illinois.edu/ef-api/volumes/{id}` is **live** and returns EF Schema 3.0 JSON
- The rsync endpoint for EF 2.5 bulk data is live: `data.analytics.hathitrust.org::features-2025.04/`
- [TORCHLITE](https://htrc.github.io/torchlite/) provides a newer lightweight interface
- The `htrc/torchlite-notebooks` repo shows how to access the EF API with plain `requests` (no library needed)

## What else is in the HTRC ecosystem

**htrc-feature-reader examples/** (9 notebooks):
- `Accessing volumes by ids.ipynb` -- data access patterns (requires library source tree, not standalone)
- `Naive+Bayes+Classification.ipynb` -- text classification (requires HTRC Python SDK)
- `GetAllProperNouns.ipynb` / `-Parallel.ipynb` -- proper noun extraction (requires bundled data)
- `Multi Processing Example.ipynb` -- parallel processing patterns
- `ID_to_Rsync_Link.ipynb` -- pairtree path encoding (standalone, but purely utilitarian)
- `ExtractedFeatures2Changes.ipynb` -- EF v2 format changes
- `Test chunking.ipynb` -- algorithmic test

**htrc/torchlite-notebooks** -- Newer examples using the EF API directly with plain HTTP requests. No library dependency. Best current starting point for new HTRC work.

The Extracted Features 2.5 dataset covers 18.7 million volumes and 6.8 billion pages.
