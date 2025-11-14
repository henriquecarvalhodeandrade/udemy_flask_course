# Meu primeiro scripit em flask
from flask import Flask, render_template

app = Flask(__name__)

# Informar a rota, ex:
# https://google.com/search?q=vvfeffr


@app.route("/")
def principal():
	nome = "Fulano"
	idade = 25

	fruta1 = "morango"
	fruta2 = "uva"
	fruta3 = "maçã"
	fruta4 = "laranja"

	return render_template("index.html", 
		nome=nome, 
		idade=idade, 
		fruta1=fruta1,
		fruta2=fruta2,
		fruta3=fruta3,
		fruta4=fruta4
	)

# http://127.0.0.1:5000


@app.route("/sobre")
def sobre():
	return render_template("sobre.html")
	