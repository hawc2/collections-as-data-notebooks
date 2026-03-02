# Digital Archaeology -- O-DATE Welcome

**Source:** [o-date/notebooks](https://github.com/o-date/notebooks)
**Status:** Archival (last commit Aug 2018)
**Selected notebook:** `Welcome.ipynb`

## What it does

A purely narrative/orientation notebook for the Open Digital Archaeology Textbook Environment (O-DATE). Explains how Jupyter notebooks work (markdown vs. code cells, the toolbar), and instructs users how to save work via git. Contains no executable code cells.

## V2.0 fixes applied

- Changed `git push -u origin master` to `git push -u origin main` (GitHub default branch changed in 2020)
- Fixed `requirements.txt`: changed `sklearn` to `scikit-learn` (the `sklearn` pip package was deprecated Dec 2023)

## Notes

- The referenced image `imgs/toolbar.png` must exist alongside the notebook to render
- The `requirements.txt` includes `tensorflow` and other heavy dependencies for the broader O-DATE course, not for this specific notebook
- The [mybinder.org](http://mybinder.org) link in the notebook is still live
- Shawn Graham's (Carleton University) current computational archaeology work has shifted toward LLM and embedding-based methods

## What else is in the source repo

Only 2 notebooks exist in the repo despite the [original blog post](https://electricarchaeology.ca/2018/08/21/jupyter-notebooks-for-digital-archaeology-and-history-too/) referencing 16+ archaeology notebooks:

- `Welcome.ipynb` (selected) -- orientation/intro
- `demo-R.ipynb` -- R language demo

The broader O-DATE project is at [o-date.github.io](https://o-date.github.io/), which acknowledges it needs a revamp. The archaeology notebooks referenced in the blog post may have been hosted elsewhere in the O-DATE ecosystem.
