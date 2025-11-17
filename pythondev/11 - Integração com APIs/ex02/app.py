
from flask import Flask, render_template, request

app = Flask(__name__)

frutas = []
registros = []

@app.route("/", methods=["GET","POST"])
def principal():

	if (request.method == "POST") and (request.form.get("fruta")):
		frutas.append(request.form.get("fruta"))

	return render_template("index.html", frutas=frutas)

@app.route("/sobre", methods=["GET", "POST"])
def sobre():

	if (request.method == "POST") and ((request.form.get("aluno")) and (request.form.get("nota"))):
		registros.append(
			{"aluno": request.form.get("aluno"), "nota": request.form.get('nota')}
		)

	return render_template("sobre.html", registros=registros)
	
@app.route('/filmes', methods=["GET","POST"])
def filmes():
	import urllib.request, json

	url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=3d233df44d861ce3baf0b9b31ecb14d4'

	resposta = urllib.request.urlopen(url) 
	dados = resposta.read()
	jsondata = json.loads(dados)

	return render_template("filmes.html", filmes=jsondata['results'])

if __name__ == "__main__":
	app.run(debug=True)