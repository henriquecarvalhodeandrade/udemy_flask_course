import sqlite3

conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

'''Excluindo dados'''

id = (1,2)
cursor.execute(
    '''
        DELETE FROM filmes 
        WHERE id in (?,?)
    ''',
    id
)

conexao.commit()
print("Dados excluidos com sucesso")
