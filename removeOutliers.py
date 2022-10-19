import pandas as pd
import numpy as np
import category_encoders as ce
import matplotlib.pyplot as plt

df = pd.read_csv("Bengaluru_House_Data.csv")

fig = plt.figure(figsize=(10,7))
df = df.fillna(value=0)
plt.boxplot(df["price"])
plt.show()

print("Avg : ", df["price"].mean())
print("STD :", df["price"].std())

min_Val = df["price"].mean()-3*df["price"].std()
max_Val = df["price"].mean()+3*df["price"].std()

df1= df[ ( df["price"] < max_Val)  & (df["price"]>min_Val) ]

plt.boxplot(df1["price"])
plt.show()