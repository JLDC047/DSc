import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

titanic = pd.read_csv("titanic.csv")

#bar graph of total men and woman
sex = titanic["Sex"].value_counts()
plt.bar(sex.index,sex.values)
plt.title("Total Number of Men and Women on the Titanic")
plt.xlabel("Sex")
plt.xticks(ticks=sex.index,labels=sex.index)
plt.ylabel("Amount of People")
plt.show()

#average fare of men and women
groupbysex = titanic.groupby(["Sex"])
averageFare = groupbysex["Fare"].mean()
plt.bar(averageFare.index,averageFare.values)
plt.title("Average Fare of Men and Women")
plt.xlabel("Sex")
plt.xticks(ticks=sex.index,labels=sex.index)
plt.ylabel("Fare")
plt.show()

#pie chart for number of people present based on class 
pclass = titanic["Pclass"].value_counts()
plt.pie(pclass.values,labels=pclass.index,shadow=True,autopct='%1.1f%%')
plt.title("Percentage of People based on Class")
plt.show()
