# CS156 Project

This repository has all the necessary files and requirements so that we have the same working environment. I have included some instructions on how to initialize the working environment.
---

## Project Layout

```
CS156_Project/
├── data/                     
│   └── biosensor_dataset_with_target.csv
├── notebooks/                
├── src/                      # shared helpers (importable by notebooks)
│   └── utils.py
├── requirements.txt          # Python dependencies
└── README.md
```
---

## Quick Start (All Platforms)

```bash
# 1) Clone the repo
git clone https://github.com/<org-or-user>/<repo>.git
cd <repo>

# 2) Create a virtual environment
python -m venv .venv

# 3) Activate it
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
# Windows (Git Bash)
source .venv/Scripts/activate
# macOS / Linux (bash/zsh)
source .venv/bin/activate

# 4) Install deps
python -m pip install -U pip
python -m pip install -r requirements.txt

# 5) Verify
python -c "import sys, pandas as pd; print(sys.executable); print(pd.__version__)"
```

If the last line prints a path inside `.venv` and a pandas version, you’re good.

---

## Opening Notebooks

* **Locally (VS Code / Jupyter Lab):** open any file in `notebooks/` and run cells.
* **In Colab:** open a notebook’s GitHub URL, or use this pattern:

  ```
  https://colab.research.google.com/github/<org-or-user>/<repo>/blob/main/notebooks/01_exploration.ipynb
  ```
* **Data path in notebooks:**

  ```python
  import pandas as pd
  df = pd.read_csv('data/biosensor_dataset_with_target.csv')
  ```

---

## Shared Helpers

Add reusable code in `src/utils.py`. In notebooks:

```python
import sys, pathlib
sys.path.append(str(pathlib.Path().resolve() / 'src'))
import utils
```
---
## Colab Workflow

1. **Open from GitHub**

  Use the pattern:

```
https://colab.research.google.com/github/<org-or-user>/<repo>/blob/main/notebooks/<file>.ipynb
```

2. **Install deps (per-run)**

  First cell:

```python
!pip -q install -r requirements.txt
```

3. **Work normally**

  Run cells, generate figures, etc. Use data paths relative to repo, e.g.:

```python
import pandas as pd
df = pd.read_csv('data/biosensor_dataset_with_target.csv')
```

4. **Save back to GitHub**

  `File → Save a copy to GitHub` → choose branch (prefer your feature branch), add a commit message

> If you pick **Save a copy in Drive**, that saves to your Drive only. To share with the repo, always **Save a copy to GitHub**.

5. **Open a PR** (if on a feature branch)

  On GitHub, open a Pull Request from your branch to `main`. Someone should and will merge with main branch.

---
