from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/bonjour', methods=['GET'])
def hello():
    resultat = request.args
    nom = resultat['Nom']
    prenom = resultat['Prénom']
    nomComplet = nom + " " + prenom
    return render_template("bonjour.html", message=nomComplet)

app.run()
