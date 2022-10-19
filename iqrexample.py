import pandas as pd
import numpy as np
import category_encoders as ce
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv("Bengaluru_House_Data.csv")
df = df.fillna(value=0)
pct25 = df["price"].quantile(0.25)
pct75 = df["price"].quantile(0.75)

df1 = df[ (df["price"] > pct25) & (df["price"] < pct75)  ]
print(df1["price"].values)
plt.boxplot(df1["price"])
plt.show()