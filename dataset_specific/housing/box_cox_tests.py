# Box-cox transform for all the independent variables
# Not used atm

def find_transform(df):
    """Find box-cox shift and lambda transform parameters."""
    features_transform_dict = {}
    for feature_name in features:
        vals = df[feature_name].values
        # Ensure positive before box cox
        m_val = min(vals)
        if m_val > 0:
            m_val = 0
        shift = abs(m_val) + 1
        vals = vals + shift
        # Find box cox
        _, lmbda = stats.boxcox(vals)
        features_transform_dict[feature_name] = (shift, lmbda)
    return features_transform_dict

def transform(df, features_transform_dict):
    """Tranforms box-cos according to the parameter found before."""
    df = df.copy()
    for feature_name in features:
        shift, lmbda = features_transform_dict[feature_name]
        df[feature_name] = df[feature_name] + shift
        df[feature_name] = stats.boxcox(df[feature_name], lmbda=lmbda)
    return df


# Merge all data and find transformation of features.
df_all = pd.concat([df_train[features], df_test[features]], axis=0)
print('df_all: ', len(df_all))
features_transform_dict = find_transform(df_all[features])
