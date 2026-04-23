#Step 1: import libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#Step 2: load the data set
df = pd.read_csv("diabetesCSV.csv") #load and save in db
#print(df) #prints the whole file
#print(df.head()) #prints first 5 (default)
#print(df.head(7)) #prints first 7
#print(dr.tail()) #prints last 5

#Step 3: split the dataset into X and Y axis (input n output)
X = df.iloc[:,:-1] #index location has 2 arguments, : means everything
#include everything but -1 (:-1)
y = df.iloc[:,-1] 

#Step 4: split the dataset into training and testing
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2) #test=20%
#automatically assume training is 80%, or u can specify the training instead
#print(df.size)
#print(X_train) #80%
#print(X_test) #20%

#Step 5: call the model
model = LogisticRegression()

#Step 6: train the model
model.fit(X_train, y_train) #pass x and y train

#Step 7: model prediction
pred = model.predict([[9,170,74,31,0,44,0.403,43]]) #pass in a form of 2D array
print(pred[0]) #prints 1 since the example i chose has diabetes
if pred[0] == 1:
    print("The patient has diabetes")
else:
    print("The patient doesn't have diabetes")

y_pred = model.predict(X_test)
#print(y_pred) #predected output
#print(y_test) #actual output

acc = accuracy_score(y_pred, y_test) #predected output and actual output
print("The model accuracy is: ", acc*100) #range from 70-80% then its good
#if over 80% then its outstanding

cm = confusion_matrix(y_pred, y_test)
print("The confusion matrix is: ", cm)

cr = classification_report(y_pred, y_test)
print("The classification report is: ", cr)