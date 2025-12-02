import pandas as pd

df = pd.read_csv("titanic.csv")

print(df.info())

print("*******************************")

print(df.describe())

print("*******************************")

print(df.head(3))

print("*******************************")

print(df.tail())

print("*******************************")
