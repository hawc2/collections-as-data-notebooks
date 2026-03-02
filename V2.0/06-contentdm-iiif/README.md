# ContentDM IIIF -- Temple University Libraries

**Source:** [hawc2/contentdm-iiif-api](https://github.com/hawc2/contentdm-iiif-api)
**Status:** Active (last commit Feb 2026)
**Selected notebook:** `CDM_IIIF_Image_Download.ipynb`

## What it does

Provides a workflow for interacting with Temple University Libraries' ContentDM instance (`cdm16002.contentdm.oclc.org`) via the IIIF Presentation API. Browses available collections, downloads metadata into CSV, downloads IIIF images at full resolution, and can iterate over all collections for bulk metadata download.

## Notes

- This notebook is scoped to Temple University's ContentDM instance. Collection IDs like `p16002coll9` are Temple-specific. The patterns can be adapted to other ContentDM instances by changing the `BASE_URL`.
- The ContentDM IIIF API is publicly accessible, no authentication required.

## Potential issue

The notebook uses IIIF Presentation API 2.x patterns (`sequences`, `canvases`, `@id`). If the cdm16002 instance has been upgraded to serve IIIF Presentation 3.0 manifests exclusively, the canvas traversal code would silently produce empty output. Check the manifest's `@context` field to verify:
- v2: `http://iiif.io/api/presentation/2/context.json`
- v3: `http://iiif.io/api/presentation/3/context.json`

## Requirements

```
requests
pandas
urllib3
```

## What else is in the source repo

- `CDM_IIIF_Image_Download.ipynb` (selected) -- the main workflow
- `examples/` -- 3 IIIF notebooks adapted from hibernator11 (Smithsonian, Europeana, Ghent)
- `ocr/` -- OCR-related assets
- `manifest.csv` -- sample manifest data
