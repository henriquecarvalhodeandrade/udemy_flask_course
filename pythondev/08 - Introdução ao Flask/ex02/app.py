# Meu primeiro scripit em flask
from flask import Flask, render_template

app = Flask(__name__)

# Informar a rota, ex:
# https://google.com/search?q=vvfeffr


@app.route("/")
def principal():
	

	return render_template("index.html")

# http://127.0.0.1:5000


@app.route("/sobre")
def sobre():
	return render_template("sobre.html")
	