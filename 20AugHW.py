import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#user input for y=mx+c
m = int(input("What is the m: "))
c = int(input("What is the c: "))
x = np.arange(0,101,10)
y = x*m+c
plt.plot(x,y,"go-")
plt.title("y=mx+c")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#bar graph count of passengers per class
titanic = pd.read_csv("titanic.csv")
pclass = titanic["Pclass"].value_counts()
plt.bar(pclass.index, pclass.values)
plt.title("Number of Passengers per Pclass")
plt.xlabel("Pclass")
plt.xticks(ticks=pclass.index,labels=pclass.index)
plt.ylabel("Number of People")
plt.show()

#age of passengers in 10 year intervals
ages = titanic["Age"]
bins = np.arange(0,101,5)
plt.hist(ages,bins,rwidth=0.9,color="r")
plt.title("Age of Passengers in 10 Year Intervals")
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.show()

