import pandas as pd
import numpy as np

iris = pd.read_csv("iris.csv")

print("Here's some information about the Iris dataframe \n")

print(iris.info())
print()

print(iris.head())
print()

print("Sepal Length:", str(iris["sepal_length"].min())+",", str(iris["sepal_length"].max())+",", str(iris["sepal_length"].mean()))
print()

print("Sepal Width:", str(iris["sepal_width"].min())+",", str(iris["sepal_width"].max())+",", str(iris["sepal_width"].mean()))
print()

print("Petal Length:", str(iris["petal_length"].min())+",", str(iris["petal_length"].max())+",", str(iris["petal_length"].mean()))
print()

print("Petal Width:", str(iris["petal_width"].min())+",", str(iris["petal_width"].max())+",", str(iris["petal_width"].mean()))
print()

print(iris["species"].value_counts())





