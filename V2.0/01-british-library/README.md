# British Library -- BNB SPARQL Subject Search

**Source:** [BL-Labs/Jupyter-notebooks-projects-using-BL-Sources](https://github.com/BL-Labs/Jupyter-notebooks-projects-using-BL-Sources)
**Status:** Stable (sporadic updates, last Aug 2024)
**Selected notebook:** `BNB_SPARQL_subject_search.ipynb` -- SPARQL query for books by LCSH subject

## What it does

Queries the British National Bibliography's SPARQL endpoint for books indexed under a given Library of Congress Subject Heading. Saves results to CSV, then visualizes book counts by author and year, and generates a word cloud from titles.

## Known issues

**The BNB SPARQL endpoint (`bnb.data.bl.uk`) is offline.** The British Library migrated the BNB to a new linked data platform. The replacement is at `https://bl.natbib-lod.org/` (beta, resumed November 2024). The old SPARQL endpoint URL, query structure, and subject URI patterns will not transfer unchanged to the new system.

### V2.0 fixes applied

- Removed unused `from pandas.io.json import json_normalize` (removed from pandas in 1.x+)

### Still needed

- Repoint all SPARQL queries to the new `bl.natbib-lod.org` endpoint once it stabilizes
- Verify ontology prefixes (`schema:`, `bibo:`, `dct:`) against the new platform
- Test query syntax against the replacement SPARQL service

## Requirements

```
requests
pandas
matplotlib
wordcloud
```

## What else is in the source repo

The BL-Labs repo contains 13 notebooks across 4 directories:

- **LOD_SPARQL/** (3 notebooks) -- SPARQL queries against BNB linked data: books by LCSH subject, comparing publication years across subjects, interactive map from LOD extraction
- **Microsoft19thCenturyBooks/** (8 notebooks) -- Loading and exploring JSON metadata from BL's 19th-century book collections, Flickr photo maps
- **blnewspapermaps/** (1 notebook) -- Mapping BL newspaper collections (newest addition, Aug 2024)
- **IRO/** (1 notebook) -- Loading BL institutional repository datasets
