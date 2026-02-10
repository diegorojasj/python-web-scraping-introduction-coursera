import pandas as pd

def load_data(df: pd.DataFrame, target_file: str) -> None:
    """Load data from a BeautifulSoup object"""
    df.to_csv(target_file, index=False)