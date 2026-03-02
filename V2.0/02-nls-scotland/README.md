# National Library of Scotland -- National Bibliography

**Source:** [NLS-Digital-Scholarship/collections-as-data](https://github.com/NLS-Digital-Scholarship/collections-as-data)
**Status:** Stable (last commit Oct 2022)
**Selected notebook:** `Exploring_National_Bibliography_Scotland.ipynb`

## What it does

Loads a large MARC XML file from the NLS Data Foundry, parses it with Python's `xml.etree.ElementTree`, extracts bibliographic fields (author, title, subject, publication date/place) into a pandas DataFrame, cleans and normalizes the data, and generates summary statistics. Covers ~369,000 records of books published in Scotland, in Scots, or in Scottish Gaelic.

## Data required

Download the MARC XML dataset from the [NLS Data Foundry](https://data.nls.uk/data/metadata-collections/national-bibliography-of-scotland/) and place it at `data/National-Bibliography-of-Scotland-v1-dataset-MARC.xml`. The file is large.

For the Binder-friendly path (sections 1-2), pre-generated CSVs (`NBSv1_subset_messy.csv`, `NBSv1_subset.csv`) must exist.

## V2.0 fixes applied

- Replaced 3 uses of `Element.getchildren()` with `list(elem)` -- `getchildren()` was removed in Python 3.9

## Still needed

- The bundled `requirements.txt` pins 2020-era versions (altair via git commit, pandas 1.0.4, spacy 2.3.2). A fresh `pip install altair pandas matplotlib` is recommended instead.
- Altair visualization calls should be verified against Altair 5.x (API changes from 2.x)
- The SSL certificate bypass at the top is functional but a security anti-pattern

## Requirements

```
pandas
numpy
altair
matplotlib
```

## What else is in the source repo

The NLS repo contains 5 notebooks, all similar in structure:

- `Exploring_National_Bibliography_Scotland.ipynb` (selected)
- `Exploring_Medical_History_of_British_India.ipynb`
- `Exploring_Lewis_Grassic_Gibbon.ipynb` (first editions)
- `Exploring_Britain_and_UK_Handbooks.ipynb`
- `Exploring_Ladies_Edinburgh_Debating_Society.ipynb`

Each targets a different NLS Data Foundry dataset. The NLS 2024-25 National Librarian's Research Fellowship in Digital Scholarship is producing new NLP-focused notebooks that may appear in the repo.
