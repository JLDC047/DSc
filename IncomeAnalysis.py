import pandas as pd

income = pd.read_csv("adult_income.csv",sep=", ")
print(income.info())
#print(income.isnull().sum())
income.drop(["fnlwgt","educational-num","capital-gain","capital-loss","hours-per-week"],axis=1,inplace=True)

import matplotlib.pyplot as plt

print(income["income"].value_counts())
income["income"] = income["income"].map({"<=50K":0, ">50K":1})
print(income["income"].value_counts())

education_level = income[["income","education"]].groupby("education").mean()
print(education_level)
plt.bar(x=education_level.index, height=education_level["income"])
plt.xticks(rotation=45)
plt.show()


