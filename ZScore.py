import pandas as pd
import numpy as np
import category_encoders as ce
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv("Bengaluru_House_Data.csv")
df = df.fillna(value=0)
# if Z value is o=above three and below 3 then remove

df["zscore"] = stats.zscore(df["price"])

df = df[df["zscore"] > -3]
df = df[df["zscore"] < 3]

plt.boxplot(df["price"])
plt.show()

df.to_csv("from class.csv", header =True, mode="a+")