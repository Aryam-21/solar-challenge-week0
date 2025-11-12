import pandas as pd
from pathlib import Path


def load_data():
    file = Path("data/solar_data.csv")
   
    return pd.read_csv(file)


def filter_by_country(df, countries):
    """Filter dataframe by selected countries."""
    return df[df["Country"]==countries]
