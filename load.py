import pandas as pd
import os

def load_data(df: pd.DataFrame, target_file: str) -> None:
    """Load data from a BeautifulSoup object"""
    os.makedirs(os.path.dirname(target_file), exist_ok=True)
    df.to_csv(target_file, index=False)