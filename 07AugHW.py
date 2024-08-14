import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

request = int(input("What do you want to do? "))

if request == 1:
    matrix1 = []
    matrix2 = []

    l = int(input("How long are the martrices? "))
    w = int(input("How long are the martrices? "))
    for i in range(0,l):
        result = int(input("martrix1 index"+str(i)+": "))
        matrix1.append(result)

    for i in range(0,n):
        result = int(input("martrix2 index"+str(i)+": "))
        matrix2.append(result)

    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    operation = int(input("""Addition = 1
Subtraction = 2
What operation do you want to do to the matrices? """))

    if operation == 1:
        print(matrix1 + matrix2)
    elif operation == 2:
        print(matrix1 - matrix2) 
    else:
        print("Error") 


elif request ==2:
    equation = int(input("""Linear = 1
Quadratic = 2
What type of expression do you want to evaluate? """))

    array = np.arange(1,11)
    plotpoints = np.arange(1,51)

    if equation == 1:
        a = int(input("Enter value for a: "))
        b = int(input("Enter value for b: "))
        print(array * a + b)
        plt.title ("ax+b")
        plt.plot(plotpoints*a+b,plotpoints,"bp-")
        plt.show()

    elif equation == 2:
        a = int(input("Enter value for a: "))
        b = int(input("Enter value for b: "))
        c = int(input("Enter value for c: "))
        print((array **2 * a) + (b * array) + c)
        plt.title ("ax^2+bx+c")
        plt.plot((plotpoints**2*a)+(b*plotpoints)+c,plotpoints,"bp-")
        plt.show()

    else:
        print("Error")  


elif request == 3:
    titanic = pd.read_csv("titanic.csv") 

    FareBySexAndPClass = titanic.groupby(["Sex","Pclass"])
    print(FareBySexAndPClass["Fare"].mean()) 

    print()

    survived = titanic[titanic["Survived"]==1]      
    print("Mean age of survived:",survived["Age"].mean())
    print("Median age of survived:",survived["Age"].median())
