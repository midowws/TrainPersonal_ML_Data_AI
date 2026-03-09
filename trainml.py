import pandas as pd


df = pd.read_csv('iris.csv')

print (df.head)
print(df.tail)

print (df.info)

print (df.describe)

dataset = df.values
