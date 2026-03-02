# Smithsonian IIIF -- Accessing Images

**Source:** [hibernator11/notebook-iiif-images](https://github.com/hibernator11/notebook-iiif-images)
**Status:** Stable (last commit Nov 2023)
**Selected notebook:** `accessing-iiif-smithsonian.ipynb`

## What it does

Searches the Smithsonian Open Access API for items (default: "theodore roosevelt"), retrieves IIIF manifests for each result, saves metadata to CSV, and performs OpenCV-based face detection on downloaded portrait images using a Haar cascade classifier. Demonstrates a complete pipeline from API search through image analysis.

## Prerequisites

- **API key required.** Register at https://api.data.gov/signup/ and replace `YOUR_API_KEY_HERE` in the notebook.
- Create directories: `is-images/` and `opencv/`
- Download OpenCV's Haar cascade file: `opencv/haarcascade_frontalface_default.xml` (ships with `cv2`, or download from [OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades))
- For the face detection demo: provide `smithsonian-example.jpg` in the working directory

## V2.0 fixes applied

- Replaced hardcoded API key with placeholder
- Updated `requirements.txt` (old versions: Pillow 2.6.1, opencv-python 3.4.0.14 -- uninstallable on modern Python)

## Still needed

- Verify IIIF manifest response structure: the code assumes IIIF Presentation API v2 (`label`/`value` keys in metadata). If Smithsonian has migrated to v3, the metadata parsing needs updating.
- The bare `except` clause in cell 10 should catch specific exceptions
- `csv.writer(open(...))` pattern leaks file handles

## Requirements

See `requirements.txt`. Core dependencies:
```
requests
pandas
matplotlib
opencv-python
numpy
Pillow
```

## What else is in the source repo

3 notebooks, each querying a different IIIF source:

- `accessing-iiif-smithsonian.ipynb` (selected) -- Smithsonian Open Access
- `accessing-iiif-europeana.ipynb` -- Europeana collections
- `accessing-iiif-ugent.ipynb` -- Ghent University Library

Author Gustavo Candela remains active in GLAM/IIIF/Wikidata work; his newer repos cover LOD quality, Wikidata queries, and Getty provenance data.
