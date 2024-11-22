from titanic_analysis.summary_table import create_summary_table 
import pandas as pd

def test_create_summary_table():
    # Mock a DataFrame
    mock_df = pd.DataFrame(data={
        'Age': [22, 38, 26, 35, None],
        'Sex': ['male', 'female', 'female', 'male', 'male'],
        'Survived': [0, 1, 1, 0, 1]
    })
    
    summary_df = create_summary_table(mock_df)
    
    expected_columns = ['Feature Name', 'Data Type', 'Number of Unique Values', 'Has Missing Values?']
    assert all(col in summary_df.columns for col in expected_columns), "Summary table is missing expected columns"
    assert summary_df.loc[summary_df['Feature Name'] == 'Age', 'Has Missing Values?'].values[0] == True, "Age should have missing values"
