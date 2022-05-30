# -*- coding: utf-8 -*-
"""Data_Cleaning_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gbKarMPIfO8E5AabRFB3z8LBYsikW8Dq
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')
df.head()

df.shape

pd.set_option('display.max_columns', None)

df.head(10)

df.info()

df.isnull()

df.isnull().sum()

plt.figure(figsize=(12,16))
sns.heatmap(df.isnull())

null_var = df.isnull().sum()/df.shape[0] * 100
null_var

drop_cols = null_var[null_var > 17].keys()
drop_cols

df2 = df.drop(columns = drop_cols)
df2.shape

sns.heatmap(df2.isnull())

df3 = df2.dropna()
df3.shape

sns.heatmap(df3.isnull())

df3.isnull().sum().sum()

df3.select_dtypes(include = ['int64','float64']).columns

sns.distplot(df['MSSubClass'])

sns.distplot(df3['MSSubClass'])

sns.distplot(df['MSSubClass'])
sns.distplot(df3['MSSubClass'])

num_var = [ 'MSSubClass', 'LotArea', 'OverallQual', 'OverallCond',
       'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
       'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF',
       'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
       'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces',
       'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF',
       'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal',
       'MoSold', 'YrSold', 'SalePrice' ]

plt.figure(figsize=(15,18))
for i, var in enumerate(num_var):
  plt.subplot(9,4, i+1)
  sns.distplot(df[var], bins = 20)
  sns.distplot(df3[var], bins = 20)

df3.select_dtypes(include=['object']).columns

xis = 1,



pd.concat([df['MSZoning'].value_counts()/df.shape[0] * 100,
          df3['MSZoning'].value_counts()/df3.shape[0] * 100],
          axis = 1, keys = ['MSZoning Org', 'MSZoning_Clean'])

def cat_var_dist(var):
  pd.concat([df[var].value_counts()/df.shape[0] * 100,
      df3[var].value_counts()/df3.shape[0] * 100],
      axis = 1, keys = [var+'_Org', var+'_Clean'])

cat_vars = ['MSZoning', 'Street', 'LotShape', 'LandContour', 'Utilities',
       'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2',
       'BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl', 'Exterior1st',
       'Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation',
       'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
       'Heating', 'HeatingQC', 'CentralAir', 'Electrical', 'KitchenQual',
       'Functional', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond',
       'PavedDrive', 'SaleType', 'SaleCondition']

for i,var in enumerate(cat_vars):
  cat_var_dist(var)



