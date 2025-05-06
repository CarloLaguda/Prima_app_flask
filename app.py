from flask import Flask, request, redirect, render_template #render template per poter renderizare html

app = Flask("__name__")
lista = [1, 2, 3, 4]

@app.route("/")
def index():
    return render_template("index.html", lista = lista) #Prende il template da templates e gli passo la lista, con nuovo nome

if __name__ == "__main__":
    app.run(debug = True)