from bs4 import BeautifulSoup
import pandas as pd

def transform_html(html: BeautifulSoup) -> pd.DataFrame:
    """Transform a BeautifulSoup object"""
    df = pd.DataFrame(columns=["Average Rank","Film","Year"])
    tables = html.find_all('tbody')
    rows = tables[0].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            newData = {
                'Average Rank': col[0].contents[0],
                'Film': col[1].contents[0],
                'Year': col[2].contents[0],
            }

            newPd = pd.DataFrame(newData, index=[0])
            df = pd.concat([df, newPd], ignore_index=True)
    return df

    
            
        
    