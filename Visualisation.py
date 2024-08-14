import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#create line plot
x = [1,2,7,16,25]
y = x
plt.title("x=y")
plt.plot(x,y,"p-")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#multiple plots in a single graph
x = np.arange(0,10)
y1 = x**2
y2 = x**3
plt.plot(x,y1,"rp-",label="y = x^2",linewidth=2)
plt.plot(x,y2,"bx-",label="y = x^3",linewidth=3)
plt.title("y = x^2 and y = x^3")
plt.legend()
plt.show()

#bar graph
plt.bar([1,3,5,7],[6,5,2,9],color="b")
plt.bar([2,4,6,8],[10,7,7,4],color="r")
plt.show()

plt.bar(["Apple","Pineapple","Crab apple"],[6,2,23])
plt.show()

#showing the number of male and female on titanic
titanic = pd.read_csv("titanic.csv")
sex = titanic["Sex"].value_counts()

"""plt.bar("Male",sex["male"],color="b")
plt.bar("Female",sex["female"],color="r")"""
plt.bar(sex.index,sex.values)
plt.show()

#histogram
ages = np.random.randint(0,80,50)
bins = np.arange(0,81,10)

plt.hist(ages,bins,rwidth=0.9,color="g",align="mid")
#plt.yticks()
plt.show()

