import data_handler as dh
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import metrics

def train_model():

    x_train, x_test, y_train, y_test = dh.get_data("08. Gradient Boosting and Encoding\insurance.csv")

    classifiers = {
    'Decision Tree': DecisionTreeRegressor(),
    'Random Forest': RandomForestRegressor(),
    'AdaBoost': AdaBoostRegressor(),
    'GradientBoosting': GradientBoostingRegressor(verbose=0),
    }


    results = []
    for name, model in classifiers.items():
        model.fit(x_train, y_train)
        prediction = model.predict(x_test)
        r2_score = metrics.r2_score(prediction, y_test)
        results.append({
            'ModelName': name,
            'R2 Score': r2_score
        })

    results = pd.DataFrame(results)
    print(results)

    return results

train_model()
