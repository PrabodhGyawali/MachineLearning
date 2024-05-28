"""
This is a simple implementation of multigression using sklearn library.
"""
from sklearn import linear_model
import pandas as pd

data = pd.read_csv('data.csv')

regr = linear_model.LinearRegression()
X = data[['Volume', 'Weight']]
y = data['CO2']

regr.fit(X, y)

# The coefficients can be used to show the linear regression line (line in a 3D space)
print(regr.coef_)
# [0.00780526 0.00755095]
# which means that the CO2 emission is 0.00780526 times the volume plus 0.00755095 times the weight.
```
