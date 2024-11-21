import pandas as pd
import os
from titanic_analysis.data_loader import load_titanic_data

def test_load_titanic_data():
    filepath = os.path.join("data", "titanic.csv")
    df = load_titanic_data(filepath)
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    assert not df.empty, "The DataFrame should not be empty"
