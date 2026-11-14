# Swiss Votes – Who Breaks the Party Line?

Data Analytics project, ZHAW School of Management and Law, autumn semester 2026
(Business Information Technology).

**Team:** Ricardo Barrio, Dan Köhlin, Diako Barzanji

## Research question

To what extent do party strengths explain municipal Yes-shares in federal votes
on environment and transport since 2020, and do the deviations from this
prediction differ systematically between language regions and between urban and
rural municipalities?

## Data sources

| Source | Content | Access |
| --- | --- | --- |
| FSO vote results (opendata.swiss) | Yes-share and turnout per municipality | JSON Web API |
| FSO National Council elections 2019 / 2023 | Party strength per municipality | CSV / JSON |
| FSO spatial divisions | Language region, municipality type | Download |
| FSO municipality register | Municipal mergers (old to new number) | TXT / XML / REST |
| swisstopo / FSO geodata | Municipal boundaries | GeoJSON / Shapefile |
| Swissvotes | Policy area of each vote | CSV |

All sources are joined on the FSO municipality number.

## Repository structure

```
data/raw         raw data exactly as retrieved (never edited by hand)
data/processed   cleaned and integrated tables
notebooks        Jupyter notebooks, numbered in the order they run
src              reusable Python functions and scripts
db               SQLite database
slides           concept and final presentation
docs             AI usage log, data dictionary, notes
```

Notebook names start with a two-digit number and a verb, for example
`01_collect_votes.ipynb`, `02_collect_parties.ipynb`, `03_collect_typology.ipynb`.

## How to run

1. Open a Codespace on this repository (Code > Codespaces). The libraries in
   `requirements.txt` are installed automatically.
2. Check the setup: `python src/check_setup.py`
3. Run the notebooks in `notebooks/` in numerical order.

## Git rules

1. One branch per task, named like `03-collect-typology`. Do not commit to `main` directly.
2. Open a pull request when the task is finished. One teammate reviews and merges it.
3. Clear all notebook outputs before committing (avoids merge conflicts).
4. Pull `main` before starting a new branch.
5. Log every use of AI in `docs/ai_usage_log.md`.
