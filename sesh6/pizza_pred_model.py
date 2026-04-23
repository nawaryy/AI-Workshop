#import
import pandas as pd
from sklearn.linear_model import LogisticRegression

#load dataset
df = pd.read_csv("pizza_dataset.csv")

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

model = LogisticRegression()
model.fit(X,y)
#no need to split since it's a small dataset

age = int(input("Enter your age:")) #casting into integer since input from      keyboard is always a string
weight = int(input("Enter your weight:"))

pred = model.predict([[age,weight]]) #as 2D array
#print(pred[0])
if pred[0] == 1:
    print("Enjoy your pizza")
else:
    print("Go to the gym bro")
