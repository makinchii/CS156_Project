import os
import pandas as pd
from pathlib import Path

# helper to load ds
def load_dataset(local_rel_path="data/your_dataset.csv",raw_url="https://raw.githubusercontent.com/makinchii/CS156_Project/main/data/biosensor_dataset_with_target.csv"):

    # 1) Try local file (works when repo is cloned locally OR cloned in Colab)
    p = Path(local_rel_path)
    if p.exists():
        print(f"Reading local file: {p}")
        return pd.read_csv(p)

    # 2) Try RAW URL 
    raw_env = os.environ.get("RAW_DATA_URL")
    use_url = raw_env or raw_url
    if use_url:
        print(f"Reading from RAW URL: {use_url}")
        return pd.read_csv(use_url)
    
    raise FileNotFoundError("Dataset not found. Set a valid local path, or provide RAW_DATA_URL")