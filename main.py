import pandas as pd
from utils import get_html
from transform import transform_html
from load import load_data

url = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"
target_file = "transformed_data.csv"

path_output = "output/"

def main() -> None:
    html = get_html(url)
    df = transform_html(html)
    load_data(df, path_output + target_file)

if __name__ == "__main__":
    main()