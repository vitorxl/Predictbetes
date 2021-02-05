from flask import Flask, request, render_template
import pickle
import numpy

app = Flask(__name__)

modelo2 = pickle.load(open("../Model/lg.pkl", "rb")) #logistic regression

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("main.html")

    if request.method == "POST":
        age = int(request.form["age"])

        polydipsia_yes = 0
        polyuria_yes = 0
        visual_blurring_yes = 0
        itching_yes = 0
        delayed_healing_yes = 0
        partial_paresis_yes = 0
        alopecia_yes = 0 
        obesity_yes = 0

        if request.form.get("polydipsia_yes"):
            polydipsia_yes = 1

        if request.form.get("polyuria_yes"):
            polyuria_yes = 1

        if request.form.get("visual_blurring_yes"):
            visual_blurring_yes = 1

        if request.form.get("itching_yes"):
            itching_yes = 1

        if request.form.get("delayed_healing_yes"):
            delayed_healing_yes = 1

        if request.form.get("partial_paresis_yes"):
            partial_paresis_yes = 1

        if request.form.get("alopecia_yes"):
            alopecia_yes = 1

        if request.form.get("obesity_yes"):
            obesity_yes = 1
        
        #resultado = modelo2.predict([[age, polyuria_yes, polydipsia_yes, visual_blurring_yes, itching_yes, delayed_healing_yes, partial_paresis_yes, alopecia_yes, obesity_yes]])
        
        probabilidade = modelo2.predict_proba([[age, polyuria_yes, polydipsia_yes, visual_blurring_yes, itching_yes, delayed_healing_yes, partial_paresis_yes, alopecia_yes, obesity_yes]])
        
        return render_template("main.html", probabilidade = "Você tem {}% de chances de ser diabético(a)".format(int(probabilidade[:,1].round(2)*100)) )

app.run(debug = True)
