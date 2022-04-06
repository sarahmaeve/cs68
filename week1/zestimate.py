#!/usr/local/bin/python3
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from vega_datasets import data
import seaborn as sns


pd.set_option('display.max_columns', None)

housing_data =  pd.read_csv('https://raw.githubusercontent.com/cjflanagan/cs68/master/housing.csv')

housing_data = pd.get_dummies(housing_data, columns=['SaleCondition','LotShape','GarageType'], drop_first=True)

# try to sum up bathrooms in an off-the-cuff-formula
housing_data['BathComps'] = housing_data['FullBath'] + ( housing_data['HalfBath'] * .33 ) + (housing_data['BsmtHalfBath'] * .25)

# Data description available here: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data?select=data_description.txt
# housing_data.head()

housing_data.shape

sns.scatterplot(y='SalePrice', x='LotArea', data=housing_data)

sns.lmplot(y='SalePrice', x='LotArea', data=housing_data)

y = housing_data['SalePrice']

X = housing_data[['LotArea', 'BedroomAbvGr', 'OverallQual','OverallCond','GarageType_Attchd','GarageType_Detchd','YearBuilt','GrLivArea','BathComps']]

X = sm.add_constant(X)

model = sm.OLS(y, X)
results = model.fit()
print(results.summary())


