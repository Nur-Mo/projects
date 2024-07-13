import pandas as pd
import numpy as np

data = {'A':[1, 2, 3], 'B':[4, 5, 6]}
df = pd.DataFrame(data)

value = df.iloc[0, 1]
subset = df.iloc[1:3, 0:2]
print(value)
print("_____________________")
print(subset)
print("_____________________")
print(df)
print("----------------------")
data = {'A': [1,2,3], 'B': [4,5,6], 'C': [7,8,9]}
df = pd.DataFrame(data, index=['x','y','z'])
subset = df.loc['y':'z','A':'B']
print(df)