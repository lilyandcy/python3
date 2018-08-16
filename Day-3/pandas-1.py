import numpy as np
import pandas as pd

df = pd.DataFrame([10, 20, 30, 40], columns= ['Numbers'], index= ['a', 'b', 'c', 'd'])

print(df.index)
print(df.columns)
print(df.ix['c'])
print(df.ix[['a', 'd']])
print(df.ix[df.index[1:3]])
print(df.sum())
ts = df ** 2
print(ts)