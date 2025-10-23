import sqlite3

'''conectando ao banco'''
conexao = sqlite3.connect('titulo.db')

'''criando cursor'''
cursor = conexao.cursor()

'''inserindo dados'''
cursor.execute(
    '''
        INSERT INTO filmes(nome, ano, nota)
        VALUES ("Sonic: The Movie",2020, 8)
    '''
)

'''confirmar ação'''
conexao.commit()

'''fechar conexao'''
conexao.close()
print('Dados inseridos na tabela\n')
