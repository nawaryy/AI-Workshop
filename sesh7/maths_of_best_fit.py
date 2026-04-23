# y = mx + c
# m: the slope (coeff)
# c: y-int 
import pandas as pd
df = pd.read_csv("home.csv")
print(df.head())

from sklearn.linear_model import LinearRegression
#split x and y axis
x = df.iloc[:,:-1] #[row,column] : all , :-1 all except last 1
y = df.iloc[:,-1] # : all, -1 only the last column (inverse indexing)
 #no need to make train and test splitting since the dataset is small
 #we can call the model now
model = LinearRegression()
model.fit(x,y)

#prediction
pred = model.predict([[3800]])
print(pred)