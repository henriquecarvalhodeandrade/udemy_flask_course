import sqlite3

'''conectando ao banco'''
conexao = sqlite3.connect('titulo.db')

'''criando cursor'''
cursor = conexao.cursor()

'''
Leitura de dados
'''

dados = cursor.execute("SELECT * FROM filmes")
print(dados.fetchall())