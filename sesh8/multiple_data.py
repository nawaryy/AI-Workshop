#handling the missing values in dataset
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import math
df=pd.read_csv("homeprices_multivariable_linear_regression.csv")
print(df)

# median
median_bedrooms=math.floor(df.bedrooms.median())
print(f"The median is (floor): {median_bedrooms}")

df.bedrooms=df.bedrooms.fillna(median_bedrooms)

# then train the model with the same steps
X=df.iloc[:,:-1]
y=df.iloc[:,-1]
model=LinearRegression()
model.fit(X,y)
predict=model.predict([[2600,3.0,20]])
print(f"The price is: {predict}")
