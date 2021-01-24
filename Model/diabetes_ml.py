import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import numpy

diabetes = pd.read_csv("~/Downloads/diabetes_data_upload.csv")

X = diabetes.drop("Gender", axis = 1)

X.rename(columns = {"Age": "age",
		    "Polyuria": "polyuria",
		    "Polydipsia": "polydipsia",
		    "Genital thrush": "genital_thrush",
		    "visual blurring": "visual_blurring",
		    "Itching": "itching",
		    "Irritability": "irritability",
		    "delayed healing": "delayed_healing",
		    "partial paresis": "partial_paresis",
		    "muscle stiffness": "muscle_stiffness",
		    "Alopecia": "alopecia",
		    "Obesity": "obesity"}, inplace = True)

features = ["age", "polyuria", "polydipsia", "visual_blurring", "itching", "delayed_healing", "partial_paresis", "alopecia", "obesity"]

X = X[features]

X = pd.get_dummies(X, drop_first = True)
y = diabetes['class']

lg = LogisticRegression(max_iter = 10000)
lg.fit(X, y)

#pickle.dump(lg, open("lg.pkl", "wb"))


