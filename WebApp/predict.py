import pickle as plk
import pandas as pd

X_pred = [
[ 0, 23, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1 ]
]


features = ['GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY', 'PEER_PRESSURE',
 'CHRONIC DISEASE', 'FATIGUE ', 'ALLERGY ', 'WHEEZING', 'ALCOHOL CONSUMING',
 'COUGHING', 'SHORTNESS OF BREATH', 'SWALLOWING DIFFICULTY', 'CHEST PAIN']

# print(len(features), len(X_pred[0]))

import sklearn
with open("/Users/sakibdalal/Downloads/Lung-Cancer-Prediction/models/RandomForestModel.pkl", "rb") as f:
    model = plk.load(f)

y_pred = model.predict(X_pred)
# y_pred = model.feature_names_in_
print(y_pred)

# data = pd.read_csv("../data/survey lung cancer.csv")
# print(len(data.columns))
# print(len(X_pred[0]))