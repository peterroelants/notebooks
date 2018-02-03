import math
import pandas as pd


def combine_categories(df, col1, col2, name):
    """Combine categories if a row can have multiple categories of a certain type."""
    # Find unique categories
    uniques = set(pd.unique(df[col1])) | set(pd.unique(df[col2]))
    # Merge different columns
    all_dummies = pd.get_dummies(df[[col1, col2]], dummy_na=True)
    for condition in uniques:
        if type(condition) == float and math.isnan(condition):
            continue
        c1 = col1 + '_' + condition
        c2 = col2 + '_' + condition
        c_combined = name + condition
        if c1 in all_dummies and c2 in all_dummies:
            df[c_combined] = all_dummies[c1] | all_dummies[c2]
        elif c1 in all_dummies:
            df[c_combined] = all_dummies[c1]
        elif c2 in all_dummies:
            df[c_combined] = all_dummies[c2]
    del df[col1]
    del df[col2]


def preprocess(df, columns_needed=None):
    if columns_needed is None:
        columns_needed = []
    
    ### MSSubClass is integer but should be categorical (integer values don't have meaning)
    df['MSSubClass'] = df['MSSubClass'].astype('int').astype('category')

    # Alley has NaN variable that actually have meaning
    df['Alley'].fillna('NoAlley', inplace=True)
    assert df['Alley'].notnull().all()

    # LotShape is an ordinal variable
    assert df['LotShape'].notnull().all()
    df['LotShape'].replace({'Reg': 0, 'IR1': 1, 'IR2': 2, 'IR3': 3}, inplace=True)

    # Utilities is complex categorical
    df['Utilities_Electricity'] = df['Utilities'].apply(
        lambda x: 1 if x in ['ELO', 'NoSeWa', 'NoSewr', 'AllPub'] else 0)
    df['Utilities_Gas'] = df['Utilities'].apply(
        lambda x: 1 if x in ['NoSeWa', 'NoSewr', 'AllPub'] else 0)
    df['Utilities_Water'] = df['Utilities'].apply(
        lambda x: 1 if x in ['NoSewr', 'AllPub'] else 0)
    df['Utilities_SepticTank'] = df['Utilities'].apply(
        lambda x: 1 if x in ['AllPub'] else 0)
    del df['Utilities']

    # LandSlope is ordinal
    assert df['LandSlope'].notnull().all()
    df['LandSlope'].replace({'Gtl': 0, 'Mod': 1, 'Sev': 2}, inplace=True)

    # Neighborhood is a categorical
    assert df['Neighborhood'].notnull().all()
    df['Neighborhood'] = df['Neighborhood'].astype('category')

    # Condition1 and Condition2 are similar  categoricals
    combine_categories(df, 'Condition1', 'Condition2', 'Condition')

    # Exterior1st and Exterior2nd are similar categoricals
    combine_categories(df, 'Exterior1st', 'Exterior2nd', 'Exterior')

    # ExterQual is an ordinal variable
    df['ExterQual'].fillna(-1, inplace=True)
    assert df['ExterQual'].notnull().all()
    df['ExterQual'].replace({'Po': 0, 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4}, inplace=True)

    # ExterCond is an ordinal variable
    df['ExterCond'].fillna(-1, inplace=True)
    assert df['ExterCond'].notnull().all()
    df['ExterCond'].replace({'Po': 0, 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4}, inplace=True)

    # BsmtQual is an ordinal variable
    df['BsmtQual'].fillna('NA', inplace=True)
    assert df['BsmtQual'].notnull().all()
    df['BsmtQual'].replace({'NA':0 , 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5}, inplace=True)

    # BsmtCond is an ordinal variable
    df['BsmtCond'].fillna('NA', inplace=True)
    assert df['BsmtCond'].notnull().all()
    df['BsmtCond'].replace({'NA':0 , 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5}, inplace=True)

    # BsmtExposure is an ordinal variable
    df['BsmtExposure'].fillna('NA', inplace=True)
    assert df['BsmtExposure'].notnull().all()
    df['BsmtExposure'].replace({'NA':0 , 'No': 1, 'Mn': 2, 'Av': 3, 'Gd': 4}, inplace=True)

    # BsmtFinType1 is an ordinal variable
    df['BsmtFinType1'].fillna('NA', inplace=True)
    assert df['BsmtFinType1'].notnull().all()
    df['BsmtFinType1'].replace({'NA':0 , 'Unf': 1, 'LwQ': 2, 'Rec': 3, 'BLQ': 4, 'ALQ': 5, 'GLQ':6}, inplace=True)

    # BsmtFinType2 is an ordinal variable
    df['BsmtFinType2'].fillna('NA', inplace=True)
    assert df['BsmtFinType2'].notnull().all()
    df['BsmtFinType2'].replace({'NA':0 , 'Unf': 1, 'LwQ': 2, 'Rec': 3, 'BLQ': 4, 'ALQ': 5, 'GLQ':6}, inplace=True)

    # HeatingQC is an ordinal variable
    df['HeatingQC'].fillna(-1, inplace=True)
    assert df['HeatingQC'].notnull().all()
    df['HeatingQC'].replace({'Po': 0, 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4}, inplace=True)

    # CentralAir is a binary variable
    df['CentralAir'].fillna(-1, inplace=True)
    assert df['CentralAir'].notnull().all()
    df['CentralAir'].replace({'N': 0, 'Y': 1}, inplace=True)

    # KitchenQual is an ordinal variable
    df['KitchenQual'].fillna(-1, inplace=True)
    assert df['KitchenQual'].notnull().all()
    df['KitchenQual'].replace({'Po': 0, 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4}, inplace=True)

    # Functional is an ordinal variable
    df['Functional'].fillna(-1, inplace=True)
    assert df['Functional'].notnull().all()
    df['Functional'].replace(
        {'Sal': 0, 'Sev': 1, 'Maj2': 2, 'Maj1': 3, 'Mod': 4, 'Min2': 5, 'Min1': 6, 'Typ': 7}, inplace=True)

    # FireplaceQu is an ordinal variable
    df['FireplaceQu'].fillna('NA', inplace=True)
    assert df['FireplaceQu'].notnull().all()
    df['FireplaceQu'].replace({'NA':0 , 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5}, inplace=True)

    # GarageFinish is an ordinal variable
    df['GarageFinish'].fillna('NA', inplace=True)
    assert df['GarageFinish'].notnull().all()
    df['GarageFinish'].replace({'NA': 0, 'Unf': 1, 'RFn': 2, 'Fin': 3}, inplace=True)

    # FireplaceQu is an ordinal variable
    df['GarageQual'].fillna('NA', inplace=True)
    assert df['GarageQual'].notnull().all()
    df['GarageQual'].replace({'NA':0 , 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5}, inplace=True)

    # GarageCond is an ordinal variable
    df['GarageCond'].fillna('NA', inplace=True)
    assert df['GarageCond'].notnull().all()
    df['GarageCond'].replace({'NA':0 , 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5}, inplace=True)

    # CentralAir is an ordinal variable
    df['PavedDrive'].fillna(-1, inplace=True)
    assert df['PavedDrive'].notnull().all()
    df['PavedDrive'].replace({'N': 0, 'P': 1, 'Y': 2}, inplace=True)

    # PoolQC is an ordinal variable
    df['PoolQC'].fillna('NA', inplace=True)
    assert df['PoolQC'].notnull().all()
    df['PoolQC'].replace({'NA':0 , 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4}, inplace=True)

    # Fence is an ordinal variable
    df['Fence'].fillna('NA', inplace=True)
    assert df['Fence'].notnull().all()
    df['Fence'].replace({'NA': 0, 'MnWw': 1, 'GdWo': 2, 'MnPrv': 3, 'GdPrv': 4}, inplace=True)

    # Combine YrSold and MoSold into more or less continous variable
    df['YrSold'] = df['YrSold'] + (df['MoSold'] - 1) / 12.
    # Still convert MoSold to categorical to keep seasonality effect
    # (note: to fully do this it should be encoded into a circular 2D variable)
    df['MoSold'] = df['MoSold'].astype('int').astype('category')

    # Assume that LotFrontage==NaN means there is no street connected directly
    df['LotFrontage'].fillna(0, inplace=True)

    # No veneer area when veneer is not present
    df['MasVnrArea'].fillna(0, inplace=True)

    # No Garage means no year build
    df['GarageYrBlt'].fillna(0, inplace=True)

    # No Basement
    df['BsmtFinSF1'].fillna(0, inplace=True)
    df['BsmtFinSF2'].fillna(0, inplace=True)
    df['BsmtUnfSF'].fillna(0, inplace=True)
    df['TotalBsmtSF'].fillna(0, inplace=True)
    df['BsmtFullBath'].fillna(0, inplace=True)
    df['BsmtHalfBath'].fillna(0, inplace=True)
    # No Garage
    df['GarageCars'].fillna(0, inplace=True)
    df['GarageArea'].fillna(0, inplace=True)

    df = pd.get_dummies(df, dummy_na=True)

    missing_columns = set(columns_needed) - set(df.columns)
    if missing_columns:
        print('Columns {} are missing, adding them.'.format(missing_columns))
    for col in missing_columns:
        df[col] = 0

    assert df.notnull().all().all(), 'Nan s in {}'.format(
        df.columns[df.isnull().any()].tolist())
    return df
