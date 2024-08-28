import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("Data.csv")
"print(data.info())"

#split features and target
X = data.iloc[:,:-1]
y = data.iloc[:,-1]
print(X)
print(y)

#check for missing values
print(X.isnull().sum())

#replacing the missing the values
from sklearn.impute import SimpleImputer



