# Library of Congress -- JSON API and IIIF

**Source:** [LibraryOfCongress/data-exploration](https://github.com/LibraryOfCongress/data-exploration)
**Status:** Active (last commit Jul 2025, 223 stars)
**Selected notebooks:** `LOC_JSON_API.ipynb`, `IIIF.ipynb`

## LOC_JSON_API.ipynb

Demonstrates the loc.gov JSON API: fetches trending content from the LoC homepage, lists all collections with pagination, drills into the WWI Sheet Music collection to display cover images and publisher data, and generates charts of publication locations.

**Status: Works as-is.** No API key needed, no local data required. The loc.gov JSON API is confirmed active. The `?fo=json` parameter and pagination via `pagination.next` are unchanged.

## IIIF.ipynb

Introduces IIIF Image API 2.1 concepts using a LoC newspaper page (1942 Anacostia batch). Demonstrates fetching `info.json`, retrieving images at various sizes, with mirroring, rotation, and percentage-based cropping.

**Status: Works after fix.**

### V2.0 fixes applied

- Changed all 6 `http://tile.loc.gov` URLs to `https://tile.loc.gov` -- the server was already redirecting to HTTPS; plain HTTP may fail with strict security settings

## Notes

- The legacy `chroniclingamerica.loc.gov` API was retired August 2025. These notebooks don't use it, but other LoC notebooks in the source repo do.
- The IIIF spec version (2.1) is current for LoC -- no deprecation to IIIF 3.x at tile.loc.gov.
- The size parameter `full` is correct for IIIF 2.x (in 3.0, `full` was replaced by `max`).

## Requirements

```
requests
pandas
matplotlib
```

## What else is in the source repo

The LoC data-exploration repo is the most comprehensive resource on this list, with 34 notebooks organized as a Jupyter Book at [libraryofcongress.github.io/data-exploration/](https://libraryofcongress.github.io/data-exploration/):

- **loc.gov JSON API/** -- Core API tutorials plus Chronicling America sub-collection (6 ChronAm notebooks, Rosenwald Collection download, geocoding, maps analysis)
- **Chronicling America API/** -- Older API samples (note: legacy API retired Aug 2025)
- **loc.gov IIIF API/** -- IIIF Image API tutorial (selected)
- **loc.gov Sitemaps API/** -- Sitemap-based discovery
- **loc.gov web interface/** -- OpenSearch
- **Data Packages/** -- 11 notebooks for specific datasets (Sanborn maps, stereographs, digitized books, jukebox, telephone directories, elections, etc.)
- **Data Sets/Web Archives/** -- Election dataset walkthrough, meme generators, lo-fi
