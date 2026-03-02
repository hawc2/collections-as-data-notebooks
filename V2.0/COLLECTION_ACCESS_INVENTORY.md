# Collection Access Inventory

A comprehensive inventory of every library collection, API endpoint, and data access protocol identified across the notebooks and source repos surveyed for V2.0. Compiled March 2026.

This document covers:
- The 7 notebook folders in V2.0
- The full contents of each source repo (not just the selected notebooks)
- The GLAM-Workbench organization (93+ repos, high-level survey)

---

## Table of Contents

* [Summary Table](#summary-table)
* [REST JSON APIs](#rest-json-apis)
* [SPARQL Endpoints](#sparql-endpoints)
* [IIIF Endpoints](#iiif-endpoints)
* [Static Data Downloads](#static-data-downloads)
* [GLAM-Workbench Coverage](#glam-workbench-coverage)
* [Authentication Reference](#authentication-reference)
* [Endpoint Status](#endpoint-status)

---

## Summary Table

| Institution | Protocol | Collections | Auth | Status |
|---|---|---|---|---|
| Library of Congress | REST JSON, IIIF Image 2.1 | 9+ (newspapers, maps, sheet music, rare books, stereographs, directories, elections, digitized books, audio) | None | Live |
| British Library (BNB) | SPARQL | British National Bibliography linked data | None | Dead (migrating) |
| British Library (OAR) | REST JSON | ~150 BL datasets via Open Access Repository | None | Live |
| British Library (19C Books) | Direct download | 49K+ digitized 19th-century books (text, metadata, images) | None | Live |
| British Library (Flickr) | Direct download | 1M+ digitized images with metadata | None | Live |
| British Library (Newspapers) | Direct download | Newspaper title-level holdings list | None | Live |
| National Library of Scotland | Direct download | 5 curated collections (bibliography, medical history, debating society, etc.) | None | Live |
| HathiTrust (Catalog) | REST JSON | Catalog metadata for 17.5M+ volumes | None | Live |
| HathiTrust (Extracted Features) | REST JSON | Page-level word frequencies, POS tags for 18.7M volumes | None (new API) | Live (sunsetting Dec 2026) |
| Smithsonian | REST JSON + IIIF | 19 museums, 9 research centers, libraries, archives | API key (free) | Live |
| Europeana | REST JSON + IIIF 3.0 | Pan-European cultural heritage aggregator (newspapers, images, full text) | API key (free) | Live |
| Ghent University Library | IIIF Presentation 2.x | Digitized periodicals and collections | None | Live |
| Temple University (ContentDM) | IIIF Presentation 2.x | Temple University Libraries digital collections | None | Live |
| Wikidata | SPARQL | Structured data for enrichment (geographic coordinates, identifiers) | None | Live |
| Zenodo | REST JSON (InvenioRDM) | Research outputs, datasets, publications | Token for write; read open | Live |
| Trove (NLA Australia) | REST JSON | Newspapers, books, images, journals, music, maps | API key | Live |
| DigitalNZ | REST JSON | NZ cultural heritage aggregator | TBD | Live |
| Te Papa Tongarewa (NZ) | REST JSON | Museum collections | TBD | Live |
| RecordSearch (Aus. Nat'l Archives) | REST + scraping | Australian government records | None | Live |
| NARA (US) | REST JSON | US National Archives | TBD | Live |
| Library and Archives Canada | REST | Canadian heritage collections | TBD | Live |

---

## REST JSON APIs

### Library of Congress

The strongest resource in this inventory. 34 notebooks in the [data-exploration](https://github.com/LibraryOfCongress/data-exploration) repo cover 9+ distinct collections.

**Base pattern:** `https://www.loc.gov/{path}/?fo=json`

| Endpoint Pattern | Collection | Notebook(s) |
|---|---|---|
| `https://www.loc.gov/collections/?fo=json` | All collections index | loc.gov JSON API tutorial |
| `https://www.loc.gov/search/?q={query}&fo=json` | Full-text search across LoC | loc.gov JSON API tutorial |
| `https://www.loc.gov/collections/world-war-i-sheet-music/?fo=json` | WWI Sheet Music | JSON API tutorial |
| `https://www.loc.gov/collections/rosenwald-collection/?fo=json` | Lessing J. Rosenwald rare books | Rosenwald download notebook |
| `https://www.loc.gov/maps/?fo=json` | Maps (Geography & Map Division) | Maps analysis notebooks |
| `https://www.loc.gov/collections/sanborn-maps/?fo=json` | Sanborn Fire Insurance Maps | Sanborn notebooks |
| `https://www.loc.gov/collections/stereograph-cards/?fo=json` | Stereograph card images | Stereograph notebooks |
| `https://www.loc.gov/collections/digitized-books/?fo=json` | Digitized books | Digitized books notebooks |
| `https://www.loc.gov/collections/national-jukebox/?fo=json` | National Jukebox (audio) | Jukebox notebooks |
| `https://www.loc.gov/collections/telephone-directories/?fo=json` | Telephone directories | Directory notebooks |

**Chronicling America (newspapers):**
- Legacy API `chroniclingamerica.loc.gov` retired August 2025
- Now accessed via `https://www.loc.gov/collections/chronicling-america/?fo=json`
- 6 notebooks in the data-exploration repo cover newspaper queries

**Additional LoC services:**
- Storage: `https://tile.loc.gov/storage-services/` (PDF, TIFF delivery)
- Text/OCR: `https://tile.loc.gov/text-services/word-coordinates-service?format=alto_xml` (ALTO XML)
- Sitemaps: `https://www.loc.gov/sitemap/` (discovery)

### Smithsonian Open Access

**Endpoint:** `https://api.si.edu/openaccess/api/v1.0/search`

Covers all Smithsonian museums and research centers:
- National Museum of American History
- National Museum of Natural History
- National Air and Space Museum
- Smithsonian American Art Museum
- National Portrait Gallery
- Archives of American Art
- And 13+ more units

**Query parameters:** `q` (search), `rows` (results per page), `start` (offset)

**Source notebook:** hibernator11/notebook-iiif-images -- `accessing-iiif-smithsonian.ipynb`

### Europeana

**Search endpoint:** `https://newspapers.eanadev.org/api/v2/search.json`
**IIIF manifests:** `https://iiif.europeana.eu/presentation/{RECORD_ID}/manifest`
**Full text annotations:** `https://iiif.europeana.eu/presentation/{RECORD_ID}/annopage/1`

Pan-European cultural heritage. 50M+ objects from 3,500+ institutions.

**Source notebook:** hibernator11/notebook-iiif-images -- `accessing-iiif-europeana.ipynb`

### British Library Open Access Repository

**Endpoint:** `https://bl.oar.bl.uk/api/v1/tenant/d08baa53-5174-40bb-89ea-9e5f642d2ac1/search`
**Filter:** `f[collection_names_sim][]=British Library Datasets`

~150 datasets including:
- UK Doctoral Thesis Metadata (EThOS)
- Digitised 19th Century collection subsets (theatre, India, Russian language)
- OCR ground truth for training
- Crowdsourcing experiment data

**Source notebook:** BL-Labs -- `IRO/BL_IRO_load_datasets_Info.ipynb`

### HathiTrust

**Catalog API:** `http://catalog.hathitrust.org/api/volumes/full/oclc/{OCLC}.json`
- Bibliographic metadata for 17.5M+ volumes
- No authentication required

**Extracted Features API (new):** `https://data.htrc.illinois.edu/ef-api/volumes/{HTID}`
- Page-level word frequencies, parts of speech, header/body/footer segmentation
- 18.7M volumes, 6.8 billion pages
- No authentication on the new API
- Returns EF Schema 3.0 JSON

**Bulk data (rsync):** `data.analytics.hathitrust.org::features-2025.04/`

**Warning:** HTRC suspending at end of December 2026. The EF API and rsync endpoints are live now but plan accordingly.

**Source notebooks:** htrc/torchlite-notebooks (3 notebooks, modern plain-requests approach)

### Zenodo (InvenioRDM)

**Endpoint:** `https://zenodo.org/api/`

Migrated to InvenioRDM in late 2023. Key sub-endpoints:
- `/api/records/` -- search and retrieve records
- `/api/communities/` -- community collections
- `/api/requests/` -- access requests

Token-based auth for write operations; read is open.

---

## SPARQL Endpoints

### British National Bibliography

**Endpoint:** `https://bnb.data.bl.uk/sparql`
**Status:** Dead as of early 2025. Migrating to `bl.natbib-lod.org` (beta).

Ontologies used in the BL-Labs notebooks:
- `bibo:` (BIBO) -- `http://purl.org/ontology/bibo/`
- `dct:` (Dublin Core Terms) -- `http://purl.org/dc/terms/`
- `schema:` (Schema.org) -- `http://schema.org/`
- `blt:` (BL Terms) -- `http://www.bl.uk/schemas/bibliographic/blterms#`

Three notebooks in BL-Labs use this endpoint:
1. Books by LCSH subject (ISBN, title, date, author)
2. Compare publication years for two subjects
3. LOD extraction with interactive map (crosses to Wikidata for geocoding)

### Wikidata

**Endpoint:** `https://query.wikidata.org/sparql`
**Status:** Live, actively maintained.

Used in BL-Labs notebooks for geographic enrichment (GeoNames ID to coordinates via P1566, P625).

---

## IIIF Endpoints

### Library of Congress IIIF Image API 2.1

**Base:** `https://tile.loc.gov/image-services/iiif/{IDENTIFIER}/`
**Info:** `{base}info.json`
**Image:** `{base}{region}/{size}/{rotation}/{quality}.{format}`

Used across maps, newspapers, stereographs, digitized books. The `full` size parameter is correct for IIIF 2.x (3.0 replaces it with `max`).

### Smithsonian IIIF

**Manifest:** `https://ids.si.edu/ids/manifest/{idsId}`
**Image:** `https://ids.si.edu/ids/iiif/{idsId}/full/full/0/default.jpg`

Requires API key (same key as the REST search API).

### Europeana IIIF Presentation 3.0

**Manifest:** `https://iiif.europeana.eu/presentation/{RECORD_ID}/manifest`
**Annotation pages** contain full-text OCR when available.

### Ghent University Library (UGent)

**Collections:** `https://adore.ugent.be/IIIF/collections/{COLLECTION_ID}`
**Manifests:** Retrieved from collection navigation.

Example collection: La Russie illustree (RUG01-001643403) -- 15 volumes, 748 issues.

### Temple University Libraries (ContentDM)

**Top-level:** `https://cdm16002.contentdm.oclc.org/iiif/manifest.json`
**Collection:** `https://cdm16002.contentdm.oclc.org/iiif/{collectionId}/manifest.json`

IIIF Presentation 2.x. Paginated via `first`/`next` links in manifest. Image service URLs extracted from canvas annotations.

**Adaptable pattern:** Change `cdm16002` to any ContentDM instance identifier to access other institutions' collections.

---

## Static Data Downloads

### National Library of Scotland Data Foundry

**Portal:** `https://data.nls.uk/`

| Collection | Format | Size |
|---|---|---|
| National Bibliography of Scotland (v1) | MARC XML | ~60 MB |
| Medical History of British India | MARC XML, page images | Large |
| Edinburgh Ladies' Debating Society | MARC XML | Small |
| Britain and UK Handbooks (1800-1950) | CSV, JSON | Medium |
| Lewis Grassic Gibbon First Editions | MARC XML | Small |

Each collection has a DOI. Five notebooks in the NLS repo cover these collections.

### British Library Data Downloads

| Dataset | URL Pattern | Format |
|---|---|---|
| 19th Century Books metadata | `data.bl.uk/19cbooks/` | TSV (49K records), JSON (49.5K records) |
| 19th Century Books full text | `cld.pt/dl/download/...` | Nested JSON (1M+ pages) |
| Flickr BL Photos maps metadata | `data.bl.uk/19cbooks/Flickr_BLPhotos*.zip` | JSON (53K+ map images) |
| SherlockNet image tags | S3: `s3.eu-west-2.amazonaws.com/importer.oar.bl.uk/...` | CSV (970K+ tags) |
| Newspaper holdings list | `bl.iro.bl.uk/concern/datasets/...` | Excel (XLSX) |

---

## GLAM-Workbench Coverage

The [GLAM Workbench](https://glam-workbench.net/) (93+ repos) is the most comprehensive collections-as-data resource. High-level coverage by institution:

### Australia (primary focus)
- **Trove (NLA):** Newspapers, books, images, journals, music, maps, web archives, government gazettes, parliamentary press releases. ~15 repos.
- **RecordSearch (National Archives):** Government records. 1 repo.
- **Queensland State Archives:** 1 repo.
- **NSW State Archives:** 1 repo.
- **State Library of South Australia:** 1 repo.
- **State Library of Victoria:** 1 repo.
- **Libraries Tasmania:** 1 repo.
- **ANU Archives:** 1 repo.
- **National Museum of Australia:** 1 repo.
- **Museums Victoria:** 1 repo.
- **Australian Commonwealth Hansard:** Parliamentary transcripts. 1 repo.

### New Zealand
- **DigitalNZ:** Aggregator. 1 repo.
- **Te Papa Tongarewa:** Museum collections. 1 repo.

### International
- **NARA (US National Archives):** 1 repo.
- **Library and Archives Canada:** 1 repo.
- **Wikidata:** SPARQL queries for enrichment. 1 repo.
- **Web archives (general):** 1 repo.

### Infrastructure
- Datasette-lite, RO-Crate scripts, GLAM tools/interfaces. ~5 repos.

---

## Authentication Reference

| Service | Auth Type | How to Get |
|---|---|---|
| Library of Congress | None | -- |
| British Library (all) | None | -- |
| NLS Data Foundry | None | -- |
| HathiTrust Catalog | None | -- |
| HTRC Extracted Features (new API) | None | -- |
| Ghent University IIIF | None | -- |
| Temple ContentDM IIIF | None | -- |
| Wikidata SPARQL | None | -- |
| Smithsonian Open Access | API key | https://api.data.gov/signup/ (free, instant) |
| Europeana | API key | https://pro.europeana.eu/page/get-api (free) |
| Trove | API key | https://trove.nla.gov.au/about/create-something/using-api (free) |
| Zenodo (write) | Token | https://zenodo.org/account/settings/applications/ |

---

## Endpoint Status

**Live and confirmed (March 2026):**
- `https://www.loc.gov/*` -- JSON API, IIIF, storage, text services
- `https://tile.loc.gov/*` -- IIIF Image API, storage services
- `https://api.si.edu/openaccess/*` -- Smithsonian
- `https://iiif.europeana.eu/*` -- Europeana IIIF
- `https://adore.ugent.be/IIIF/*` -- Ghent
- `https://cdm16002.contentdm.oclc.org/iiif/*` -- Temple
- `https://query.wikidata.org/sparql` -- Wikidata
- `https://data.htrc.illinois.edu/ef-api/*` -- HTRC EF (live but sunsetting Dec 2026)
- `http://catalog.hathitrust.org/api/*` -- HathiTrust catalog
- `https://bl.oar.bl.uk/api/*` -- BL Open Access Repository
- `https://data.nls.uk/*` -- NLS Data Foundry
- `https://data.bl.uk/*` -- BL data downloads
- `https://zenodo.org/api/*` -- Zenodo

**Dead or migrating:**
- `https://bnb.data.bl.uk/sparql` -- Dead. Migrating to `bl.natbib-lod.org`
- `http://chroniclingamerica.loc.gov/*` -- Retired August 2025. Use `loc.gov` API.
- `https://data.analytics.hathitrust.org/features/` -- Dead (404). Use EF API instead.
- `https://data.htrc.illinois.edu/htrc-ef-access/get` -- Dead (503). Use EF API instead.

**Sunsetting:**
- All HTRC services -- HTRC suspending end of December 2026. Bulk data via rsync while available: `data.analytics.hathitrust.org::features-2025.04/`
