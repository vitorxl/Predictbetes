from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

features = ["Age", "Gender_Male", "Polyuria_Yes", "Polydipsia_Yes", "Alopecia_Yes"]
modelo  = pickle.load(open("../dt_reduzido.sav", "rb"))

@app.route("/")
def home():
    #return "Minha HOME"
    return render_template("main.html")

@app.route("/preditor", methods = ["POST"])
def preditor():
    #dados = request.get_json()
    #dados_input = [dados[col] for col in request.form]
    #resultado = modelo.predict([dados_input])
    #return jsonify(resultado = resultado[0])
    req = 10
    print(req)

app.run(debug = True)