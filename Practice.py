#Exercise 1:
#Create a 1D array with values ranging from 0 to 9.
import numpy as np
arr = np.arange(10)
print(arr)
print("Question 1")

#Exercise 2:
#Convert a 1D array to a 2D array with 2 rows.
import numpy as np
arr = np.arange(10).reshape(2, -1)
print(arr)
print("Question 2")
print("-"*50)
def tricky_function(a, b = [], c = {}):
    b.append(len(b))
    c[len(b)] = len(c)
    return a, b, c
print(tricky_function('X'))
print(tricky_function('Y'))

































































































