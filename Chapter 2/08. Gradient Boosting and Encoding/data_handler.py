import pandas as pd
import sklearn
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error,explained_variance_score
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeClassifier


#print(sklearn.__version__)

hello = "<3"
# pth = '08. Gradient Boosting and Encoding\insurance.csv'

def get_data(path):
    data = pd.read_csv(path)
    X = data.iloc[:,:-1]
    y = data.iloc[:,-1]
    #print(X.shape)
    x_train, x_test, y_train, y_test = train_test_split(data.iloc[:,:-1], data.iloc[:,-1], test_size=0.2, random_state = 0)
    ct = ColumnTransformer([('ordinal', OrdinalEncoder(handle_unknown= 'use_encoded_value', unknown_value = -1), [1,4,5] )])

    x_train = ct.fit_transform(x_train)
    x_test = ct.transform(x_test)


    return x_train, x_test, y_train, y_test

#get_data("08. Gradient Boosting and Encoding\insurance.csv")











