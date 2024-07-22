import numpy as np

list = [20, 3, 658, 7362, 7492, 546, 1]
"print(type(list))"

#coverting list to array
array = np.array(list)
"print(type(array))"

for value in list:
    v = value + 5
    list[list.index(value)] = v

"print(list)"    

"print(array + 5)"

#create array with zeros
D1zero = np.zeros(5)
D2zero = np.zeros((2,3), dtype = int)

#create array with ones
D2one = np.ones((7,4))

#check dimesion
"""print(D1zero.ndim)
print(D2zero.ndim)
print(D2one.ndim)"""

#shape
"""print(D1zero.shape)
print(D2zero.shape)
print(D2one.shape)"""

#size
"""print(D1zero.size)
print(D2zero.size)
print(D2one.size)"""

#create arrays with numbers in a range
arange = np.arange(3,19,2)
"print(arange)"

#get a random arrangement of an already-made array
"""print(np.random.permutation(arange))
print(np.random.permutation(arange))
print(np.random.permutation(arange))"""

#array of random numbers
"print(np.random.randint(3,23,7))"

random = np.random.randint(1,100,(3,4))
"print(random)"

#reshape array
"print(random.reshape(2,6))"

#sort
unsorted = np.arange(1,11)
unsorted = np.random.permutation(unsorted)
"print(unsorted)"
sorted = np.sort(unsorted)
"print(sorted)"

#array slicing
pre_slice = np.random.randint(1,100,10)
"print(pre_slice)"
"""print(pre_slice[1:7])
print(pre_slice[:5])
print(pre_slice[6:])
print(pre_slice[::3])
print(pre_slice[::-1])"""

pre_slice2 = np.random.randint(1,100,(5,6))
"print(pre_slice2)"
"print(pre_slice2[2:5,0:2])"

#conditional slicing
"""print(pre_slice2[pre_slice2 % 2 == 0])
print(pre_slice2[pre_slice2 >= 50])"""

#selection by indices
"print(pre_slice[[2,0,7,9,4]])"

#arithmetic operation
a1 = np.arange(1,9)
a2 = np.arange(3,11)
"""print(a1,"+",a2,"=", a1 + a2)"""

a12d = np.random.randint(1,10,(3,4))
a22d = np.random.randint(1,10,(3,4))
"""print(a12d,"+",a22d,"=", a12d + a22d)"""

#evaluating expression
def expression_solve(x):
    return 2*x+3
to10 = np.arange(1,11)
print(expression_solve(to10))


