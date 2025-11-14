# Meu primeiro scripit em flask
from flask import Flask, render_template, request

app = Flask(__name__)

# Informar a rota, ex:
# https://google.com/search?q=vvfeffr

frutas = []

@app.route("/", methods=["GET","POST"])
def principal():

	if (request.method == "POST") and (request.form.get("fruta")):
		frutas.append(request.form.get("fruta"))

	return render_template("index.html", frutas=frutas)

# http://127.0.0.1:5000


@app.route("/sobre")
def sobre():
	notas = {
		"Henrique": 10,
		"Alice": 9,
		"Beatriz": 8,
		"Aurora": 7,
		"Rodrigo": 9.5,
	}

	return render_template("sobre.html", notas=notas)
	