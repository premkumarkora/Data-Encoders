import pandas as pd
import numpy as np
import category_encoders as ce

df = pd.read_csv("Bengaluru_House_Data.csv")
df= df.head(100)
print(df["size"].unique())

encod = ce.OneHotEncoder(cols="area_type",return_df=True,use_cat_names=True)

encoded_Data = encod.fit_transform(df)
print(encoded_Data)

