#pip install pandas
import pandas
from sklearn.linear_model import LinearRegression

#step 2: read the dataset
df = pandas.read_csv('house_prices.csv')
print(df)

#Step 3: split the dataset into input(x) and output(y)
X = df.drop(columns="home_price", axis=1) #we save homeprice in X
print(X)