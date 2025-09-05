import sqlite3

'''Conectando ao banco de dados'''
conexao = sqlite3.connect('titulo.db')

'''Criando o cursor

o cursor serve para a manipulação do banco: 
CRUD, create, read, update, delete'''
cursor = conexao.cursor()

'''Criando tabela'''
cursor.execute(
    '''
        CREATE TABLE filmes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL  
        );
    '''
)

'''Fechando conexão'''
conexao.close()
print('tabela criada')


