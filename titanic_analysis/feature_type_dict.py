def create_feature_type_dict(df): 
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).

    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.

    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [],
            'discrete': []
        },
        'categorical': {
            'nominal': [],
            'ordinal': []
        }
    }
    
    for column in df.columns:
        if df[column].dtype in ['float64', 'int64']:
            # Assuming 'Age' and 'Fare' are continuous, others are discrete
            if column in ['Age', 'Fare']:
                feature_types['numerical']['continuous'].append(column)
            else:
                feature_types['numerical']['discrete'].append(column)
        else:
            # Categorical features (nominal features assumed here for simplicity)
            feature_types['categorical']['nominal'].append(column)
    
    return feature_types
