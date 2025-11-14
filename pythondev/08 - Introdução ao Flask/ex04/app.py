# Meu primeiro scripit em flask
from flask import Flask, render_template

app = Flask(__name__)

# Informar a rota, ex:
# https://google.com/search?q=vvfeffr


@app.route("/")
def principal():
	frutas = ["morango", "uva", "banana", "laranja", "maça", "pera", "melao", "abacaxi", "abacate"]

	return render_template("index.html", frutas=frutas)

# http://127.0.0.1:5000


@app.route("/sobre")
def sobre():
	return render_template("sobre.html")
	