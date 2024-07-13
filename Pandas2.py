import pandas as pd
import numpy as np
# Using cut() function of Converting contious value into Discrete values
data = {'value': [10,15,20,25,30,35,40]}
df = pd.DataFrame(data)
bins = [0,20,30,100]
labels = ['low','medium','high']
df['Category'] = pd.cut(df['value'], bins = bins, labels = labels)
print(df)
print("----------------------------------------")
# Using interpolate()function for filling the values
series = pd.Series([1, np.nan, 3, np.nan, 5])
filled_series = series.interpolate()
print(filled_series)
print("_____________________________________")
#Using numpy.where() to retrieve the position of True values in Boolean
series = pd.Series([10,25,7,30,45,50,62,15,20])
positions = np.where(series % 5 == 0)[0]
print("Positions of Multiples of 5:")
print(positions)