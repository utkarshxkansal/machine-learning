# Foundations

This folder contains the programming and data-work foundations I am building before and alongside machine learning.

The material is organised by tool so that notes, notebooks, practice exercises, and small supporting datasets stay together. Some files are experiments or works in progress; this repository records the learning process rather than presenting every topic as a finished course.

## Learning areas

| Area | Focus | Materials |
|---|---|---|
| [Python](./Python/) | Core syntax, data types, operators, strings, OOP, file handling, and JSON practice | Python scripts, text/CSV examples, and notebooks |
| [NumPy](./Numpy/) | Arrays, array properties, indexing and slicing, reshaping, aggregation, broadcasting, stacking, and vectorisation | Small focused Python examples |
| [Pandas](./Pandas/) | DataFrames, reading/writing data, missing values, grouping, and data exploration | Notebooks, exercises, and sample datasets |
| [Matplotlib](./Matplotlib/) | Plotting and visual exploration, including Matplotlib/Seaborn practice | Notebooks and small spreadsheet examples |
| [SQL](./SQL/) | SQL query practice organised by chapter and exercise | SQL files |
| [LLM notes](./llms.ipynb) | Early notes and experiments related to large language models | Jupyter notebook |

## Getting started

1. Clone or download the repository.
2. Create and activate a Python virtual environment.
3. Install the shared dependencies from the repository root:

   ```bash
   python -m venv .venv
   # Windows:
   .venv\\Scripts\\activate
   # macOS/Linux:
   source .venv/bin/activate

   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Start Jupyter with `jupyter notebook` and open a notebook from the relevant topic folder.
5. Run notebook cells in order. Some notebooks may need extra packages or local data files.

## Working with datasets

- Keep small, reusable sample datasets alongside the notebook that uses them.
- Do not commit secrets, credentials, personal data, virtual environments, or generated cache files.
- GitHub blocks ordinary Git files larger than 100 MB. The large `customers-2000000.csv` file is intentionally not stored in this repository; keep a local copy or use Git LFS / an appropriate data-hosting service if it needs to be shared.
- Check dataset licences and attribution before redistributing downloaded data.

## Folder conventions

- Keep each topic's notes, exercises, and supporting data in its own folder.
- Prefer descriptive filenames over names such as `Untitled.ipynb` when creating new notebooks.
- Add a short Markdown introduction to notebooks explaining the topic, goal, and key concepts.
- Remove temporary exports, duplicate checkpoints, and operating-system files before committing.

## Progress

This is an evolving learning archive. Topics and exercises will be added as I continue learning Python, data analysis, and AI/ML.
