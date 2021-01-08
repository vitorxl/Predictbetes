from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

modelo  = pickle.load(open("../dt_reduzido.pkl", "rb"))

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("main.html")

    if request.method == "POST":
        age = int(request.form["age"])
        polyuria_yes = int(request.form["polyuria_yes"])
        polydipsia_yes = int(request.form["polydipsia_yes"])
        weakness_yes = int(request.form["weakness_yes"])
        visual_blurring_yes = int(request.form["visual_blurring_yes"])
        delayed_healing_yes = int(request.form["delayed_healing_yes"])
        alopecia_yes = int(request.form["alopecia_yes"])
        obesity_yes = int(request.form["obesity_yes"])

        resultado = modelo.predict([[age, polyuria_yes, polydipsia_yes, weakness_yes, visual_blurring_yes,delayed_healing_yes, alopecia_yes, obesity_yes]])
        
        return str(resultado)

app.run(debug = True)


features = ['Age', 'Polyuria_Yes', 'Polydipsia_Yes', 'weakness_Yes', 'visual blurring_Yes', 'delayed healing_Yes', 'Alopecia_Yes', 'Obesity_Yes']
