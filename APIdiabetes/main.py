from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

features = ["Age", "Gender_Male", "Polyuria_Yes", "Polydipsia_Yes", "Alopecia_Yes"]
modelo  = pickle.load(open("../dt_reduzido.sav", "rb"))

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("main.html")

    if request.method == "POST":
        age = int(request.form["age"])
        gender_male = int(request.form["gender_male"])
        polyuria_yes = int(request.form["polyuria_yes"])
        polydipsia_yes = int(request.form["polydipsia_yes"])
        alopecia_yes = int(request.form["alopecia_yes"])
        resultado = modelo.predict([[age, gender_male, polyuria_yes, polydipsia_yes, alopecia_yes]])
        return str(resultado)


app.run(debug = True)