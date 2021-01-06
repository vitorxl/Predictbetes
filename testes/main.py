from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__)
modelo = pickle.load(open("modelo.pickle", "rb"))

@app.route("/", methods = ["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("main.html")

    if request.method == "POST":
        dado = float(request.form["valor"])
        resultado = modelo.predict([[dado]])
        return str(resultado)


#@app.route("/", methods = ["POST"])

app.run(debug = True)