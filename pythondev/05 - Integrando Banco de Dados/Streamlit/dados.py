import sqlite3

def connect_db():
    '''conecta bd'''
    conexao = sqlite3.connect('titulo.db')
    return conexao

def insert_data(nome, ano, nota):
    '''inserir dados'''
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute(
        '''
            INSERT INTO filmes(nome, ano, nota)
            VALUES (?,?,?)
        ''', (nome, ano, nota) 
    )

    conexao.commit()
    conexao.close()

def view_data():
    conexao = connect_db()
    cursor = conexao.cursor()
    dados = cursor.execute("SELECT * FROM filmes")
    
    dados = cursor.fetchall()
    cursor.close()
    return dados
