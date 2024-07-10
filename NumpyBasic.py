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
print(random)

#reshape array
print(random.reshape(2,6))

#sort
unsorted = np.arange(1,11)
unsorted = np.random.permutation(unsorted)
print(unsorted)
sorted = np.sort(unsorted)
print(sorted)


