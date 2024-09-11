import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("Data.csv")
"print(data.info())"

#split features/indepedant variable and target/dependant variable
X = data.iloc[:,:-1]
y = data.iloc[:,-1]
print(X)
print(y)

#check for missing values
print(X.isnull().sum())

#replacing the missing the values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
X.iloc[:,-2:] = imputer.fit_transform(X.iloc[:,-2:])
print(X)

#encoding non-numerical values
#features
X_encoded = pd.get_dummies(X,columns=["Country"],dtype=int,drop_first=True)
print(X_encoded)
#target
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_encoded = le.fit_transform(y)
print(y_encoded)

#split data into training and testing 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_encoded,y_encoded,test_size=0.3,random_state=6)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

#scaling the data, standard scaler
from sklearn.preprocessing import StandardScaler
SS = StandardScaler()
X_train.iloc[:,:2] = SS.fit_transform(X_train.iloc[:,:2])
print(X_train)
X_test.iloc[:,:2] = SS.fit_transform(X_test.iloc[:,:2])
print(X_test)

