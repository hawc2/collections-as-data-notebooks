# Sentiment, Vocabulary, and Style in Science Fiction: A Pilot Analysis Using HathiTrust Extracted Features

March 2026

---

## Overview

This report summarizes a pilot computational analysis of 22 science fiction novels spanning nearly two centuries (1833-2004), using page-level word frequency and part-of-speech data from the HathiTrust Extracted Features dataset. The analysis applies sentiment scoring (AFINN lexicon), type-token ratio measurement, and TF-IDF distinctiveness scoring to a hand-picked sample of canonical works drawn from a larger corpus of 1,206 speculative fiction volumes identified by Thompson & Mimno.

The methods and code are documented in the accompanying Jupyter notebooks:
- `01_Build_SciFi_Corpus.ipynb` -- corpus construction and data retrieval
- `02_Analyze_SciFi_Corpus.ipynb` -- analysis and visualization

---

## Corpus

The 22 volumes represent major currents in anglophone science fiction, from proto-SF (Shelley, Verne, Wells) through the Golden Age (Asimov, Clarke, Heinlein) and New Wave (Ballard, Le Guin, Dick, Zelazny) to cyberpunk and contemporary work (Gibson, Butler, Banks, Atwood). The corpus totals 2.76 million tokens across 7,340 pages.

| Author | Title | Year | Pages | Tokens | Unique |
|---|---|---|---|---|---|
| Shelley | The Last Man | 1833 | 234 | 112,589 | 10,369 |
| Wells | The First Men in the Moon | 1901 | 384 | 82,305 | 7,623 |
| London | The Iron Heel | 1917 | 382 | 104,027 | 9,213 |
| Verne | Twenty Thousand Leagues Under the Sea | 1922 | 530 | 146,838 | 11,407 |
| Orwell | Nineteen Eighty-Four | 1949 | 326 | 121,577 | 9,553 |
| Clarke | The Sands of Mars | 1952 | 232 | 88,946 | 7,387 |
| Heinlein | The Past Through Tomorrow | 1967 | 680 | 384,115 | 18,649 |
| Huxley | Island | 1972 | 316 | 137,827 | 11,371 |
| Ballard | Vermilion Sands | 1973 | 216 | 72,764 | 8,135 |
| Herbert | Hellstrom's Hive | 1973 | 296 | 125,026 | 8,705 |
| Le Guin | The Wind's Twelve Quarters | 1975 | 320 | 119,583 | 10,607 |
| Bester | The Demolished Man | 1978 | 248 | 85,657 | 7,994 |
| Dick | A Handful of Darkness | 1978 | 258 | 99,774 | 7,893 |
| Bradbury | The Illustrated Man | 1978 | 202 | 95,777 | 7,325 |
| Zelazny | Eye of Cat | 1982 | 232 | 71,053 | 7,036 |
| Gibson | Burning Chrome | 1986 | 216 | 73,512 | 9,163 |
| Atwood | The Handmaid's Tale | 1986 | 334 | 118,393 | 9,137 |
| Butler | Kindred | 1988 | 294 | 133,599 | 6,951 |
| Banks | Consider Phlebas | 1991 | 520 | 209,139 | 11,340 |
| Lem | Memoirs of a Space Traveller | 1991 | 168 | 50,688 | 6,995 |
| Shelley | Frankenstein | 1999 ed. | 376 | 155,264 | 12,599 |
| Asimov | Robot Dreams | 2004 | 360 | 173,326 | 10,793 |

---

## Sentiment Analysis

Sentiment scores were computed per page using the AFINN-111 lexicon (2,477 words, scored -5 to +5). Each token on a page is looked up in the lexicon and its score multiplied by its frequency; the page score is the sum. Books were divided into thirds (beginning, middle, end) to reveal narrative arc shapes.

### Darkest works (lowest mean sentiment)

| Rank | Author | Title | Mean | End |
|---|---|---|---|---|
| 1 | Butler | Kindred | -9.1 | -12.4 |
| 2 | Bester | The Demolished Man | -6.2 | -6.8 |
| 3 | Banks | Consider Phlebas | -5.3 | -6.0 |
| 4 | Herbert | Hellstrom's Hive | -5.2 | -8.4 |
| 5 | Orwell | Nineteen Eighty-Four | -4.4 | -7.2 |

Butler's *Kindred*, a time-travel novel set partly in the antebellum American South, registers the most negative sentiment in the corpus, and its final third (-12.4) is by far the darkest ending. This is consistent with the novel's escalating violence and its unflinching confrontation with slavery. Orwell and London share the same final-third score (-7.2), both depicting the triumph of authoritarian systems over their protagonists.

### Brightest works (highest mean sentiment)

| Rank | Author | Title | Mean | End |
|---|---|---|---|---|
| 1 | Shelley | The Last Man | +10.9 | +5.3 |
| 2 | Huxley | Island | +6.5 | +4.3 |
| 3 | Clarke | The Sands of Mars | +6.0 | +5.7 |
| 4 | Shelley | Frankenstein | +4.5 | +8.0 |
| 5 | Verne | Twenty Thousand Leagues | +2.4 | +0.5 |

The high sentiment scores for Shelley's works reflect 19th-century literary diction, which is rich in emotionally charged vocabulary (love, beauty, hope, wonder). Huxley's *Island* -- his utopian counterpart to *Brave New World* -- reads as the most positive 20th-century novel in the sample. Clarke's optimistic interplanetary adventure scores consistently positive throughout.

### Narrative arc patterns

Several distinct arc shapes emerge:

- **Descent into darkness** (London, Orwell, Herbert): sentiment declines steadily from beginning to end, matching the dystopian structure in which early hope gives way to systemic oppression or collapse
- **Stable negativity** (Banks, Bester, Gibson): uniformly dark across all thirds, reflecting sustained conflict or noir atmosphere
- **Bright middle** (Clarke): the middle third (+8.8) is markedly more positive than the beginning (+3.4) or end (+5.7), consistent with a classic adventure arc
- **Mixed valence** (Dick): begins very dark (-4.5), brightens in the middle (+1.1), and settles near zero -- the structure of a short story collection with varied tones

---

## Vocabulary Richness

Type-token ratio (TTR) measures lexical diversity: the proportion of unique words to total words. Higher TTR indicates more varied vocabulary. TTR is affected by text length (longer texts naturally produce lower ratios as common words recur), so comparisons are most meaningful between texts of similar size.

### Most lexically diverse

| Rank | Author | Title | TTR | Tokens |
|---|---|---|---|---|
| 1 | Lem | Memoirs of a Space Traveller | 0.1380 | 50,688 |
| 2 | Gibson | Burning Chrome | 0.1246 | 73,512 |
| 3 | Ballard | Vermilion Sands | 0.1118 | 72,764 |
| 4 | Zelazny | Eye of Cat | 0.0990 | 71,053 |
| 5 | Bester | The Demolished Man | 0.0933 | 85,657 |

Lem's satirical SF, filtered through English translation, uses the most diverse vocabulary. Gibson and Ballard -- both associated with stylistically ambitious, prose-forward SF -- rank second and third. These three authors are frequently cited in literary criticism for their distinctive registers, and TTR provides quantitative support for that characterization.

The lowest TTR values belong to Heinlein's omnibus (0.049, but at 384K tokens it's an outlier in length), Banks (0.054), and Butler (0.052). Butler's low score may reflect the novel's deliberately plain, first-person narration -- a stylistic choice that contrasts with the baroque vocabularies of Lem and Ballard.

---

## Distinctive Words

TF-IDF scoring identifies words that are frequent in one volume but rare across the corpus. In fiction, this reliably surfaces character names, place names, and thematic vocabulary -- the "fingerprint" of each work.

| Author | Title | Distinctive Words |
|---|---|---|
| Shelley | The Last Man | perdita, raymond, adrian, idris, evadne, windsor, ryland, lionel |
| Wells | First Men in the Moon | cavor, selenites, selenite, cavorite, mooncalf, bedford, mooncalves |
| London | The Iron Heel | ernest, everhard, oligarchy, bishop, wickson, plutocracy, socialists, labor |
| Verne | Twenty Thousand Leagues | nemo, conseil, nautilus, ned, aronnax, captain, canadian, submarine |
| Orwell | Nineteen Eighty-Four | winston, julia, telescreen, newspeak, oceania, ministry, proles, ingsoc |
| Clarke | Sands of Mars | gibson, jimmy, hadfield, norden, hilton, ares, mars, kilometres |
| Huxley | Island | murugan, susila, vijaya, pala, rani, raja, farnaby, sarojini |
| Ballard | Vermilion Sands | vermilion, lunora, tristram, tony, aurora, leonora, fay, nolan |
| Herbert | Hellstrom's Hive | hellstrom, peruge, janvert, saldo, merrivale, hive, kraft, depeaux |
| Le Guin | Wind's Twelve Quarters | pugh, osden, ganil, semley, kaph, harfex, tomiko, lenoir |
| Bester | The Demolished Man | reich, powell, tate, peeper, chooka, esper, ben, barbara |
| Dick | A Handful of Darkness | olham, miller, rick, trent, silvia, ellis, elwood, grote |
| Bradbury | The Illustrated Man | peregrine, ettil, saul, hitchcock, braling, hollis, willie, mink |
| Zelazny | Eye of Cat | billy, ironbear, tedders, fisher, yellowcloud, mancin, canyon, coyote |
| Gibson | Burning Chrome | deke, korolev, coretti, bobby, rubin, hiroshi, ralfi, yefremov |
| Atwood | The Handmaid's Tale | moira, janine, lydia, serena, ofglen, luke, cora, aunt |
| Butler | Kindred | rufus, kevin, weylin, nigel, alice, dana, rufe, carrie |
| Banks | Consider Phlebas | horza, yalson, balveda, kraiklyn, wubslin, idiran, xoxarle, aviger |
| Lem | Memoirs of a Space Traveller | tichy, mattrass, corcoran, diagoras, eminents, zazul, washers, razglaz |
| Asimov | Robot Dreams | fellowes, drake, ralson, multivac, timmie, hoskins, rioz, blaustein |

Beyond character names, the thematic vocabulary is revealing. London's *Iron Heel* is marked by political terms (oligarchy, plutocracy, socialists, labor) that distinguish it from the rest of the corpus. Orwell's invented vocabulary (telescreen, newspeak, ingsoc, proles) surfaces immediately. Wells produces genre-specific neologisms (cavorite, mooncalf, selenites). Huxley's *Island* is identifiable by its Sanskrit-derived names (murugan, susila, vijaya, pala), reflecting the novel's engagement with Eastern philosophy.

---

## Limitations and Next Steps

**Limitations of this pilot:**

- The AFINN lexicon is a blunt instrument. It captures broad emotional valence but misses irony, genre-specific connotations (e.g., "alien" is neutral in SF but may carry negative weight in other contexts), and the distinction between depicted emotion and narrative tone.
- TTR comparisons across texts of different lengths are imprecise. A normalized measure (e.g., moving average TTR, or Yule's K) would be more robust.
- The 22-volume sample is too small for decade-level generalizations. The full 1,206-volume corpus (metadata fetched, features downloadable) would support more reliable trend analysis.
- Extracted Features data is non-consumptive: we have word frequencies but not word order, so syntactic and narrative structure are inaccessible.

**Possible extensions:**

- **Scale to full corpus**: download features for all 1,206 volumes and re-run the analysis for statistically meaningful trends across decades and subgenres
- **Comparison corpus**: use Underwood's fiction metadata (101K volumes) to build a matched non-SF corpus and identify what's *distinctively* science-fictional in vocabulary and sentiment
- **Topic modeling**: cluster volumes by token frequency profiles to identify thematic groupings (space opera, dystopia, first contact, cyberpunk) without relying on pre-assigned labels
- **Proper noun extraction**: use NNP/NNPS tags as a proxy for named entity recognition to map character networks and setting vocabularies
- **Time-series analysis**: with the full corpus, test whether SF sentiment darkens after specific historical events (Cold War escalation, Vietnam, climate awareness)

---

## Data Sources

- **Thompson & Mimno speculative fiction workset**: 1,206 HathiTrust volume IDs matched from [Worlds Without End](https://worldswithoutend.com/). Source: [github.com/laurejt/authorless-tms](https://github.com/laurejt/authorless-tms)
- **HathiTrust Extracted Features API**: `https://data.htrc.illinois.edu/ef-api/volumes/{htid}`. Returns EF Schema 3.0 JSON with page-level token/POS counts. No authentication required. HTRC suspending end of December 2026.
- **AFINN-111 sentiment lexicon**: 2,477 English words scored -5 to +5, accessed via the `afinn` Python package.
- **HTRC recommended workset** (larger): "20th Century English-Language Speculative Fiction" (2,454 volumes) at [analytics.hathitrust.org/staticrecommendedworksets](https://analytics.hathitrust.org/staticrecommendedworksets)
