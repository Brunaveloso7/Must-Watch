from flask import Flask, render_template, request, redirect

app = Flask(__name__)

filmes = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        nome_filme = request.form.get("filme")
        if nome_filme:
            filmes.append(nome_filme)
        return redirect("/")
    return render_template("index.html", filmes=filmes)


@app.route("/deletar/<int:id>")
def deletar(id):
    if 0 <= id < len(filmes):
        filmes.pop(id)
    return redirect("/")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    if request.method == "POST":
        novo_nome = request.form.get("filme")
        if novo_nome:
            filmes[id] = novo_nome
        return redirect("/")
    return render_template("editar.html", filme=filmes[id], id=id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
