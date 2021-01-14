import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

diabetes = pd.read_csv("~/Downloads/diabetes_data_upload.csv")

X = diabetes.drop("Gender", axis = 1)
X = pd.get_dummies(X.iloc[:, :-1], drop_first = True)
y = diabetes['class']

lg = LogisticRegression(max_iter = 10000)
lg.fit(X, y)

pickle.dump(lg, open("lg.pkl", "wb"))
