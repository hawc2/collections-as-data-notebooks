# Process Log: HTRC Sci-Fi Corpus

## What we've compiled

### Workset data (in `data/`)

1. **Original Thompson & Mimno workset** (`scifi-metadata.tsv`)
   - 1,206 HathiTrust volume IDs, from COLING 2018 "Authorless Topic Models" paper
   - Source: [laurejt/authorless-tms](https://github.com/laurejt/authorless-tms)
   - Fields: htid, author, title

2. **Expanded Thompson & Mimno workset** (`sf-hathitrust-volumes.tsv`)
   - 5,811 volumes (2,235 works, 1,201 authors), 1900-2010
   - Source: [laurejt/sf-in-hathitrust](https://github.com/laurejt/sf-in-hathitrust) (last updated Jan 2026)
   - Built via HTRC Advanced Collaborative Support project; matched against Worlds Without End + computational similarity
   - Fields: htid, HTRecord, WWEnd ID, ISFDB ID, Title, Author, Year
   - Listed as HTRC Recommended Workset

3. **Anthology subset** (`sf-hathitrust-anthologies.tsv`)
   - 918 volumes (669 works, 288 editors), subset of the 5,811

### Cached metadata (in `data/`)

- `scifi_metadata.json` -- EF API metadata for 1,205/1,206 volumes from the original workset (one ID failed: `uc1.b3759971`)

### Downloaded Extracted Features (in `data/ef_samples/`)

22 volumes, hand-picked for canonical coverage:

| Author | Title | htid |
|--------|-------|------|
| Shelley | Frankenstein | mdp.39015060998203 |
| Shelley | The Last Man | nyp.33433075746960 |
| Verne | 20,000 Leagues Under the Sea | hvd.hn2vzk |
| Wells | First Men in the Moon | dul1.ark:/13960/t5gb2ss8d |
| London | The Iron Heel | hvd.32044050819549 |
| Huxley | Island | coo.31924001398258 |
| Orwell | 1984 | mdp.39015046412311 |
| Asimov | Robot Dreams | inu.30000094835844 |
| Clarke | Sands of Mars | mdp.39015002701798 |
| Heinlein | The Past Through Tomorrow | mdp.39015000608953 |
| Bradbury | The Illustrated Man | inu.39000002436611 |
| Bester | The Demolished Man | mdp.39015011054155 |
| Le Guin | The Wind's Twelve Quarters | mdp.39015000146798 |
| Dick | A Handful of Darkness | mdp.39015001151276 |
| Ballard | Vermilion Sands | mdp.39015003465583 |
| Herbert | Hellstrom's Hive | mdp.39015001537060 |
| Lem | Memoirs of a Space Traveller | inu.30000009621628 |
| Zelazny | Eye of Cat | mdp.39015001577363 |
| Butler | Kindred | mdp.39015020728666 |
| Gibson | Burning Chrome | mdp.39015020677442 |
| Atwood | The Handmaid's Tale | pst.000013408435 |
| Banks | Consider Phlebas | inu.30000036612392 |

### Analysis completed (see REPORT.md)

Pilot analysis on the 22 volumes: sentiment arcs, vocabulary richness (TTR), TF-IDF distinctive words, POS distribution. Key findings: Butler's Kindred darkest sentiment (-9.1 avg), Shelley's Last Man brightest (+10.9), Lem highest vocabulary diversity.

## What's not yet done

- **Notebooks not yet updated for the 5,811-volume workset.** The current notebooks still reference the original 1,206-volume TSV for metadata fetching. Updating to use `sf-hathitrust-volumes.tsv` would give access to richer fields (WWEnd ID, ISFDB ID, publication year) and nearly 5x the volume IDs.
- **No metadata fetch for expanded workset.** We cached EF API metadata for the original 1,206 but not the full 5,811.
- **Sample is 22 of 5,811.** Downloading EF data for more volumes would enable larger-scale analysis.
- **No topic modeling.** The workset was originally built for topic modeling (LDA); we haven't done that yet.
- **No anthology segmentation.** Thompson presented at DH2020 on segmenting short stories from anthology page-level data -- could be applied to the 918 anthology volumes.

## Other corpora identified (not yet integrated)

| Corpus | Size | Notes |
|--------|------|-------|
| SF-Nexus / Paskow Collection (Temple) | 403 works | New Wave era mass-market paperbacks; 300+ in HathiTrust; datasets on HuggingFace (SF-Corpus) |
| HTRC BookNLP/ELF | ~213,000 fiction volumes | No SF genre tag, but could cross-reference with ISFDB |
| Post45 HathiTrust Fiction | Fiction 1945-2013 | No SF tag; could filter via ISFDB or WWEnd |
| Ted Underwood fiction metadata | 101K volumes | Probabilistic genre classification including SF |
| SCWAReD "Black Fantastic" | curated workset | Intersections of race, technology, speculative imagination |
| Post45 "Time Horizons of Futuristic Fiction" | 2,559 works | Cross-media (film, prose, TV), 1733-2024 |

## Technical notes

- EF API: `https://data.htrc.illinois.edu/ef-api/volumes/{htid}` -- no auth, returns EF Schema 3.0 JSON
- Volume ID encoding for URLs: `:` -> `+`, `/` -> `=`
- Some EF pages return `null` body -- null safety checks required in all parsing functions
- HTRC suspending end of December 2026 -- bulk rsync backup recommended before then
