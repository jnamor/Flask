from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/bonjour', methods=['POST'])
def hello():
    resultat = request.form
    nomComplet = resultat['nom'] + " " + resultat['prenom']
    meteo = resultat['meteo']
    return render_template("bonjour.html", reponse_meteo=meteo, message=nomComplet)

app.run(debug=True)
