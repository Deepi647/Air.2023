import pandas as pd

v=pd.read_csv("./madrid_2018.csv")
print(v)
v.dropna(inplace=True)
v.drop_duplicates(inplace=True)
v=v[['NO_2','SO_2','PM10']]
print(v)
