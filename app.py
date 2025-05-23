from flask import Flask, request, redirect, render_template #render template per poter renderizare html
from models import DatabaseWrapper #importo la classe DatabaseWrapper

db = DatabaseWrapper(
    host = "mysql-2866f0dc-iisgalvanimi-94a0.i.aivencloud.com",
    port = 27960,
    password = "AVNS_Gw45d55L_UtOUeZ0JSN",  
    user = "avnadmin",
    database = "studenti"
)

app = Flask("__name__")

"""
lista = [1, 2, 3, 4]
studenti = [
    {"id": 1, "nome": "gianni"},
    {"id": 2, "nome": "luca"}
]
@app.route("/")

def index():
    return render_template("index.html", lista = lista) #Prende il template da templates e gli passo la lista, con nuovo nome
"""
@app.route("/", methods = ["GET"])
def elenco_studenti():
    risultati = db.get_studenti()
    return render_template("index.html", risultati = risultati)

@app.route("/studenti", methods = ["POST"])
def aggiungi():
    dati = request.form["nome"]
    db.aggiungi_studente(dati)
    return redirect("/")
    """
    nome = request.form["nome"]
    nome = {
        "id" :len(studenti)+1,
        "nome": nome
    }
    studenti.append(nome)
    return redirect("/studenti")
    """
"""
@app.route("/studenti")
def visualizza_studente():
    return render_template("elenco.html", studenti = studenti)
"""
if __name__ == "__main__":
    app.run(debug = True)