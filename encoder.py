import pandas as pd
import numpy as np
import category_encoders as ce


data = pd.DataFrame(
    {"city":["Mohali", "Chandigar","Roopar"]})
encoders = ce.OneHotEncoder(cols="City",
                            return_df=True,
                            use_cat_names=True)

encoded_Data = encoders.fit_transform(data)

print(encoded_Data)