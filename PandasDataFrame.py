import pandas as pd

dictionary = {"Name":["Alex","Bailey","Camilla"], "Age":[16,7,21],"City":["NYC","Yorkshire","Paris"]}
data_frame = pd.DataFrame(dictionary)

print(data_frame, type(data_frame))

#number of rows and columns
print(data_frame.shape)

#accessing a single column
print(data_frame["City"])
print(data_frame["Name"])

#statistic operations on column
print(data_frame["Age"].mean())

#loading data from a file
titanticdf = pd.read_csv("titanic.csv")
print(titanticdf.info())
print(titanticdf.describe())

print(titanticdf.head())
print(titanticdf.tail())

print(titanticdf["Survived"].head(10))
print(titanticdf["Survived"].value_counts())

#selecting multiple columns
print(titanticdf[["Name","Age","Survived"]])

#filtering rows
print(titanticdf[titanticdf["Age"]<18])
print(titanticdf[(titanticdf["Age"]>18) & (titanticdf["Pclass"]==1)])
print(titanticdf[(titanticdf["Pclass"]==1) | (titanticdf["Fare"]>=30)])

