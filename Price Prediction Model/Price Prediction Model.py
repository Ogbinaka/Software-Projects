import pandas as pd

#importing pandas and renaming it as pd because it is great tool for reading csv files in a python environment

df = pd.read_csv("pricequotes.csv")

#reading the csv files

df

#execute

df.tail(9)
#personal choice to see the first 9 data

X = df.select_dtypes(include=[object])

#Select all the column that appears as string to be the input data 'X'

X = df.loc[:, ~df.columns.isin(['QUOTE_DATE', 'VALIDITY', 'PRICE_RELATIVE', 'LOG_PRICE_RELATIVE',
 'STRATUM_WEIGHT', 'STRATUM_TYPE', 'BASE_VALIDITY', 'END_DATE', 'STRATUM_CELL', 'BASE_VALIDITY', 'STRATUM_TYPE', 'SHOP_TYPE', 'SHOP_WEIGHT', 'PRICE',])]


#filtering the data

from sklearn import preprocessing

#import a function that will help convert the input data from strings to integers

LE = preprocessing.LabelEncoder()

X = X.apply(LE.fit_transform)

#converting strings to integers

X = X.drop(columns=['INDICATOR_BOX', 'ORIG_INDICATOR_BOX'])



X.head(3)

y = df.drop(columns=['BASE_PRICE','ITEM_DESC', 'ITEM_ID', 'QUOTE_DATE',
'REGION', 'START_DATE', 'END_DATE', 
'SHOP_TYPE', 'SHOP_CODE', 'INDICATOR_BOX', 'ORIG_INDICATOR_BOX'])

y.head(3)

#Filtering the output data

from sklearn.model_selection import train_test_split

#Importing a function that help split data into testing data and training data

from sklearn.tree import DecisionTreeRegressor

#importing regressor model

from sklearn.metrics import accuracy_score

#importing a function that scores the prediction data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

#Splitting the data into testing data and training data

model = DecisionTreeRegressor()

model.fit(X_train, y_train)

#train model

prediction = model.predict(X_test)

prediction

#predicting the model

score = model.score(X_test, y_test)

score

#scoring the model

