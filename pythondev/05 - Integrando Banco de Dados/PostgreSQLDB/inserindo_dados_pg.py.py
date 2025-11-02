'''importando o módulo de conexão'''
from conexao_post import conn

cursor_obj = conn.cursor()

'''criando novos dados no formato para a tabela do banco'''
games = [
    ('The Last of Us II', 2020, 10),
    ('COD: Warzone', 2020, 4),
    ('Far Cry 6', 2016, 7),
]

'''inserindo dados na tabela do banco de dados'''
for game in games:
    cursor_obj.execute(
        '''
            INSERT INTO games(name,ano,score)
            VALUES (%s, %s, %s)
        ''', game
    )

conn.commit()
print('Dados inseridos com sucesso!')
conn.close()