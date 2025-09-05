'''importando o módulo de conexão'''
from conexao_post import conn

cursor_obj = conn.cursor()

'''listagem do banco de dados'''
cursor_obj.execute('SELECT * FROM games')

result = cursor_obj.fetchall()

print(result)