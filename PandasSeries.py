import pandas as pd
import random

list = [random.randint(1,50) for i in range(0,15)]
print(list, type(list))

series = pd.Series(list)
print(series, type(series))

#statistic operations
print(series.min())
print(series.max())
print(series.mean())
print(series.median())
print(series.mode())

#sort
print(series.sort_values())
print(series.sort_values(ascending=False))

#count occurance
print(series.value_counts())




