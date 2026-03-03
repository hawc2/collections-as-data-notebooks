# Collections-as-Data Notebooks (V2.0)

A curated list of Jupyter notebooks for querying and analyzing library collections as data, updated March 2026. [Collections as data](https://collectionsasdata.github.io/) is a movement to mediate library collections in computational formats. Jupyter notebooks provide an ideal way to introduce data-based explorations of library collections. Much of this work occurs under the umbrella of [GLAMLabs](https://glamlabs.io/).

This is an update of the [V1.0 list](../V1.0/README.md), which was originally compiled in 2020-2021. Each entry below includes a status indicator:

- **Active** -- Maintained with recent commits (within the last year)
- **Stable** -- Functional but not actively developed
- **Archival** -- Historical reference; may not run without fixes

For comprehensive collections-as-data notebook coverage, the [GLAM Workbench](https://glam-workbench.net/) is the single best starting point.

## Table of Contents

* [General Resources](#general-resources)
* [Metadata](#metadata)
* [Text](#text)
* [Images](#images)
* [Spatial](#spatial)
* [OCR Correction](#ocr-correction)

---

## General Resources

* [GLAM Workbench](https://glam-workbench.net/) | [GitHub](https://github.com/GLAM-Workbench) -- **Active**. The most comprehensive collections-as-data notebook resource available, maintained by Tim Sherratt. 93+ repos covering Trove, web archives, Wikidata, Australian and New Zealand GLAM institutions, and more. Version 2.0 (2025) introduced JupyterLite support for in-browser notebook execution. Updated through 2026.

* [Quinn Dombrowski's DH Jupyter](https://github.com/quinnanya/dh-jupyter) -- **Stable**. A crowdsourced index of Digital Humanities Jupyter notebooks organized by language (English, German, Spanish, French). 137 stars. Contains links rather than notebooks themselves. Last updated June 2023; many linked notebooks may have link rot.

* [GLAM Workbench Data List](https://github.com/GLAM-Workbench/glam-data-list) -- **Active**. A curated list of openly available GLAM data resources, maintained as part of the GLAM Workbench project. Updated May 2025.

---

## Metadata

* [British Library Jupyter Notebooks](https://github.com/BL-Labs/Jupyter-notebooks-projects-using-BL-Sources) -- **Stable**. Notebooks for querying British Library catalog records, SPARQL/LOD endpoints, and newspaper collections. Most content dates to 2016-2019; a newspaper mapping notebook was added in August 2024. Low community adoption (8 stars).

* [Zenodo REST API](https://developers.zenodo.org/) -- **Active** (documentation). The original notebook for Zenodo (from [awesome-jupyter-glam](https://github.com/LibraryCarpentry/awesome-jupyter-glam), 2018) is outdated. Zenodo migrated to InvenioRDM and the API has changed substantially. Use the [current Zenodo REST API documentation](https://developers.zenodo.org/) and the [InvenioRDM docs](https://inveniordm.docs.cern.ch/reference/rest_api_index/) instead.

---

## Text

* [National Library of Scotland Text Mining Notebooks](https://data.nls.uk/tools/jupyter-notebooks/) | [GitHub](https://github.com/NLS-Digital-Scholarship/collections-as-data) -- **Stable**. Six notebooks for text mining NLS corpora (Medical History of British India, National Bibliography of Scotland, Edinburgh Ladies' Debating Society, and others). Each has a DOI and Binder link. Stable since 2022. The NLS's 2024-25 National Librarian's Research Fellowship in Digital Scholarship is producing new NLP-focused notebooks that may appear here.

* [HTRC Feature Reader](https://github.com/htrc/htrc-feature-reader/tree/master/examples) -- **Stable**. The HathiTrust Research Center's Feature Reader for parsing page-level parts-of-speech and word frequencies across HathiTrust collections. The library received a maintenance fix in December 2024, and the Extracted Features 2.5 dataset (18.7 million volumes) was released recently. Example notebooks date to 2016-2018. **Note:** HathiTrust announced HTRC will be [suspended at end of December 2026](https://www.hathitrust.org/about/research-center/htrc-transition-faq/) as resources are reallocated. The [TORCHLITE](https://htrc.github.io/torchlite/) project provides a newer lightweight interface to extracted features data.

---

## Images

IIIF (International Image Interoperability Framework) standardizes the library curation of digital images, making scripts for querying IIIF data adaptable across different digital collections.

* [Library of Congress Data Exploration](https://github.com/LibraryOfCongress/data-exploration) | [Jupyter Book](https://libraryofcongress.github.io/data-exploration/) -- **Active**. The strongest resource on this list. A Jupyter Book covering the loc.gov JSON API, IIIF API, Chronicling America, sitemaps, and data packages. 223 stars, actively maintained (last update July 2025). **Note:** The legacy `chroniclingamerica.loc.gov` API was retired in August 2025; the collection now uses the `loc.gov` API exclusively.

* [Smithsonian IIIF Notebooks](https://github.com/hibernator11/notebook-iiif-images) -- **Stable**. Three notebooks for querying IIIF manifests from the Smithsonian, Europeana, and Ghent University Library. Last update November 2023. Author Gustavo Candela remains active in GLAM/IIIF/Wikidata work via other repos. The [Smithsonian Open Access](https://www.si.edu/openaccess/devtools) API remains live.

* [ContentDM and IIIF API](https://github.com/hawc2/contentdm-iiif-api) -- **Active**. Notebooks for querying Temple University Libraries' digital collections, including metadata and IIIF image files from ContentDM. Actively developed (last update February 2026), with recent additions for metadata spreadsheet generation alongside image downloads.

---

## Spatial

* [Digital Archaeology Notebooks (Shawn Graham / O-DATE)](https://electricarchaeology.ca/2018/08/21/jupyter-notebooks-for-digital-archaeology-and-history-too/) | [GitHub](https://github.com/o-date/notebooks) -- **Archival**. A collection of 16+ notebooks for digital archaeology methods, including accessing the Chronicling America API. Frozen since August 2018. MyBinder links are fragile. The [O-DATE textbook](https://o-date.github.io/) acknowledges it needs a revamp. Graham's current work has shifted toward LLM and embedding-based methods.

---

## OCR Correction

The V1.0 list included a BERT-based OCR correction notebook using the now-abandoned `pytorch-pretrained-bert` library. The field has evolved substantially. Current best-practice resources:

* [llm_aided_ocr](https://github.com/Dicklesworthstone/llm_aided_ocr) -- **Active**. Tesseract + LLM post-correction using API-based or local models. 2.9k stars, last updated February 2026. The most practical production-ready option for OCR correction.

* [PreP-OCR](https://github.com/NikoGuan/PreP-OCR) -- **Active**. A two-stage pipeline (image restoration + ByT5 post-correction) from ACL 2025. Tested on 13,831 pages in English, French, and Spanish, achieving 63-70% character error rate reduction.

* [HuggingFace Transformers fill-mask pipeline](https://huggingface.co/docs/transformers/main/en/task_summary#masked-language-modeling) -- For the BERT mask-and-predict approach, use the `transformers` library (which replaced `pytorch-pretrained-bert`) with `BertForMaskedLM` or the newer [ModernBERT](https://huggingface.co/blog/modernbert) (8K token context, faster inference).

---

## Deprecated from V1.0

The following entries from V1.0 have been removed:

* **LibCrowds Notebooks** ([GitHub](https://github.com/LibCrowds/notebooks)) -- The LibCrowds crowdsourcing platform is defunct. Notebooks depend on API endpoints that are no longer available. Last commit July 2018.

* **Awesome Jupyter GLAM** ([GitHub](https://github.com/LibraryCarpentry/awesome-jupyter-glam)) -- Never populated beyond a few stub entries. Dormant since May 2019. Superseded by the GLAM Workbench and this list.

---

## Project Folders

This version includes downloaded notebooks from each source repo, with per-folder READMEs documenting status, fixes applied, and what else is available. Each folder contains a representative notebook selected for its relevance to working with library collections as data.

| Folder | Source | Notebook | Status |
| --- | --- | --- | --- |
| [01-british-library](01-british-library/) | BL-Labs | BNB SPARQL subject search | Broken -- BNB endpoint offline, migrating to bl.natbib-lod.org |
| [02-nls-scotland](02-nls-scotland/) | NLS Digital Scholarship | National Bibliography of Scotland | Fixed -- `getchildren()` replaced for Python 3.9+ |
| [03-htrc-feature-reader](03-htrc-feature-reader/) | HTRC | Within-Book Sentiment Trends | Works -- standalone with bundled data, `afinn` package |
| [04-iiif-images](04-iiif-images/) | hibernator11 | Smithsonian IIIF images | Fixed -- API key placeholder, updated requirements |
| [05-library-of-congress](05-library-of-congress/) | Library of Congress | JSON API + IIIF tutorials | Fixed -- HTTPS URLs; works as-is |
| [06-contentdm-iiif](06-contentdm-iiif/) | hawc2 | ContentDM IIIF image download | Works -- verify IIIF v2 vs v3 manifest format |
| [07-digital-archaeology](07-digital-archaeology/) | O-DATE | Welcome/orientation | Fixed -- git branch name, requirements |
| [08-htrc-scifi](08-htrc-scifi/) | HTRC EF API + Thompson & Mimno | Sci-fi corpus builder + analysis | Works -- 5,811 volumes (expanded workset), EF API live |

See each folder's README for detailed assessments, known issues, and the full inventory of what's available in each source repo.

For a comprehensive inventory of every API endpoint, collection, and data access protocol identified across all source repos, see [COLLECTION_ACCESS_INVENTORY.md](COLLECTION_ACCESS_INVENTORY.md).
