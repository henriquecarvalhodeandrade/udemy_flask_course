# Meu primeiro scripit em flask
from flask import Flask

app = Flask(__name__)


# Para criar uma página, devo informar a rota, ex:
# https://google.com/search?q=vvfeffr

@app.route("/")
def principal():
	return "Hello, World!"

# Ao rodar no terminal, ele criará uma sessão host para: http://127.0.0.1:5000


