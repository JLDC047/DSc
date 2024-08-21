import matplotlib.pyplot as plt
import numpy as np

#scatter graph
x = np.arange(1,11)
y = np.random.randint(1,4,10)
plt.scatter(x,y,100,"g","x")
plt.yticks(ticks=y,labels=y)
plt.show()

#pie graph
values = [166,1000,914,2521,1504]
names = ["Just a Teenage Gaea", "Bigfoot", "The Clockworks", "..........","Joe Schmo"]
colours = ["g","c","k","r","b"]
plt.pie(values, labels=names,startangle=90,shadow=True,autopct='%1.1f%%')
plt.show()

#stack graph
y21 = [2,56,78,2]
y22 = [1,23,26,85]
y23 = [49,63,33,1]
y24 = [45,62,3,106]
years = [0.25,0.5,0.75,1]
plt.stackplot(years,y21,y22,y23,y24)
plt.xticks(ticks=years,labels=years)
plt.show()

