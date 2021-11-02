import data_handler as dh
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

x_train, x_test, y_train, y_test = dh.get_data("08. Gradient Boosting and Encoding\insurance.csv")

def convert_to_dt(data):
    column = ["age", "sex", "bmi", "children", "smoke", "region"]
    test_data = pd.DataFrame([data], columns = column)
    return test_data


model = GradientBoostingRegressor()

check = True
while check:

    age = int(input("How old are you? \n"))
    sex = str(input("Which gender are you? \n"))
    bmi = float(input("What is your BMI? \n"))
    child = int(input("How many children do you have? \n"))
    smoke = bool(input("Do you smoke? \n"))
    region = str(input("Which region are you from? \n"))
    check_data = [age, sex, bmi, child, smoke, region]
    check_data = convert_to_dt(check_data)
    check_data = dh.get_data(check_data)
    model.fit(dh.get_data(x_train), y_train)    
    prediction = model.predict(check_data)

    print("The estimated insurance cost is:", prediction[0])
    check = False