from titanic_analysis.feature_type_dict import create_feature_type_dict
import pandas as pd
def test_create_feature_type_dict(): 
    # Mock a DataFrame
    mock_df = pd.DataFrame(data={
        'Age': [22, 38, 26, 35],
        'Sex': ['male', 'female', 'female', 'male'],
        'Survived': [0, 1, 1, 0],
        'Fare': [7.25, 71.83, 7.92, 53.10]
    })
    feature_types = create_feature_type_dict(mock_df)
    
    assert 'numerical' in feature_types, "The dictionary should have a 'numerical' key"
    assert 'categorical' in feature_types, "The dictionary should have a 'categorical' key"
    assert 'continuous' in feature_types['numerical'], "Numerical features should have 'continuous' key"
    assert 'discrete' in feature_types['numerical'], "Numerical features should have 'discrete' key"
    assert 'nominal' in feature_types['categorical'], "Categorical features should have 'nominal' key"
