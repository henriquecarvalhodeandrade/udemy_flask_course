import sqlite3

'''conectando ao banco'''
conexao = sqlite3.connect('titulo.db')

'''criando cursor'''
cursor = conexao.cursor()

'''
Atualizando dados
'''

id = 1
cursor.execute(
    '''
        UPDATE filmes SET nota = ?
        WHERE id = ?
    ''',
    ("Homem Aranha", id)
)

cursor.execute(
    '''
        UPDATE filmes SET nota = ?
        WHERE id = ?
    ''',
    (8.5, id)
)

conexao.commit()
print('dados atualizados')