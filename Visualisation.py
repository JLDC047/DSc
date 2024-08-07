import matplotlib.pyplot as plt
import numpy as np

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
