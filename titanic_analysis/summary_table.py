import pandas as pd

def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type,  number of unique values, and if it has missing values.

    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.

    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    summary_data = {
        'Feature Name': [],
        'Data Type': [],
        'Number of Unique Values': [],
        'Has Missing Values?': []
    }
    
    for column in df.columns:
        summary_data['Feature Name'].append(column)
        summary_data['Data Type'].append(df[column].dtype)
        summary_data['Number of Unique Values'].append(df[column].nunique())
        summary_data['Has Missing Values?'].append(df[column].isnull().any())
    
    summary_df = pd.DataFrame(summary_data)
    return summary_df
