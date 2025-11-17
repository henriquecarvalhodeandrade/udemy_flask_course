from flask import Flask, render_template, request, url_for, redirect, flash
import urllib.request, json
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Comando onde será encontrado o nosso banco de dados
BASE_DIR = r"C:\Users\rique\Documents\GitHub\meus_repositorios\udemy_flask_course\pythondev\12 - Integrando com Banco de Dados\instance\cursos.sqlite3"
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{BASE_DIR}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# criando o banco de dados
db = SQLAlchemy(app)

frutas = []
registros = []

# Criando as classes para as tabelas (mapeamento)
class cursos(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(50))
	descricao = db.Column(db.String(100))
	ch = db.Column(db.Integer)

	def __init__(self, nome, descricao, ch):
		self.nome = nome
		self.descricao = descricao
		self.ch = ch


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

	resposta = urllib.request.urlopen(url) 
	dados = resposta.read()
	jsondata = json.loads(dados)

	return render_template("filmes.html", filmes=jsondata['results'])

@app.route('/cursos', methods=["GET","POST"])
def lista_cursos():
	return render_template('cursos.html', cursos=cursos.query.all())

@app.route('/cria_curso', methods=["GET","POST"])
def cria_curso():
	nome = request.form.get('nome')
	descricao = request.form.get('descricao')
	ch = request.form.get('ch')

	if request.method == 'POST':
		if not nome or not descricao or not ch:
			flash("Preencha todos os campos do formulário!", "error")
		else:
			curso = cursos(nome, descricao, ch)
			db.session.add(curso)
			db.session.commit()
			return redirect(url_for('lista_cursos'))

	return render_template('novo_curso.html')

@app.route('/<int:id>/editar_curso', methods=["GET","POST"])
def editar_curso(id):
	curso = cursos.query.filter_by(id=id).first()
	if request.method == 'POST':
		nome = request.form['nome']
		descricao = request.form['descricao']
		ch = request.form['ch']

		cursos.query.filter_by(id=id).update({"nome":nome, "descricao":descricao, "ch":ch})
		db.session.commit()
		return redirect(url_for('lista_cursos'))

	return render_template('editar_curso.html', curso=curso)

@app.route('/<int:id>/remover_curso')
def remover_curso(id):
	curso = cursos.query.filter_by(id=id).first()
	db.session.delete(curso)
	db.session.commit()
	return redirect(url_for('lista_cursos'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
