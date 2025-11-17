from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

app = Flask(__name__)

# Comando onde será encontrado o nosso banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cursos.sqlite3"

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



'''
ADICIONANDO ROTAS DINAMICAS, SEM PRECISAR CRIAR PÁGINAS OU FUNÇÕES PARA CADA ROTA.
'''
@app.route('/filmes/<propriedade>', methods=["GET","POST"])
def filmes(propriedade):

	if propriedade == 'populares':
		url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=3d233df44d861ce3baf0b9b31ecb14d4'

	elif propriedade == 'kids':
		url = 'https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=3d233df44d861ce3baf0b9b31ecb14d4'

	elif propriedade == '2010':
		url = 'https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=3d233df44d861ce3baf0b9b31ecb14d4'

	elif propriedade == 'drama':
		url = 'https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=3d233df44d861ce3baf0b9b31ecb14d4'

	elif propriedade == 'tom_cruise':
		url = 'https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=3d233df44d861ce3baf0b9b31ecb14d4'
	
	else:
		return "Erro em def filmes(propriedade)"



	import urllib.request, json


	resposta = urllib.request.urlopen(url) 
	dados = resposta.read()
	jsondata = json.loads(dados)

	return render_template("filmes.html", filmes=jsondata['results'])

if __name__ == "__main__":
	app.run(debug=True) 