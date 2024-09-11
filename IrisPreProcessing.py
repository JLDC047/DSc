import numpy as np
import pandas as pd

iris = pd.read_csv("iris.csv")

#print(iris.isnull().sum())

y = iris.iloc[:,-1]
X = iris.iloc[:,:-1]
#print(X, "\n", y)

from sklearn.preprocessing import LabelEncoder
LabEn = LabelEncoder()
yEn = LabEn.fit_transform(y)
#print(yEn)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,yEn, test_size=0.25, random_state=1)
#print(X_train, "\n", X_test, "\n", y_train, "\n", y_test)

from sklearn.tree import DecisionTreeClassifier
DTC = DecisionTreeClassifier(max_depth=3)
DTC.fit(X_train, y_train)
predicted_values = DTC.predict(X_test)
print("Predicted value: \n", predicted_values)
print("Original results: \n", y_test)

from sklearn import metrics
print(metrics.accuracy_score(y_test, predicted_values))