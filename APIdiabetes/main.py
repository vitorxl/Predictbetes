from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

features = ["Age", "Gender_Male", "Polyuria_Yes", "Polydipsia_Yes", "Alopecia_Yes"]
modelo  = pickle.load(open("../dt_reduzido.sav", "rb"))

@app.route("/")
def home():
    #return "Minha HOME"
    return render_template("main.html")

@app.route("/", methods = ["POST"])
def preditor():
    dados = request.get_json()
    dados_input = [dados[col] for col in features]
    resultado = modelo.predict([dados_input])
    return jsonify(resultado = resultado[0])

app.run(debug = True)