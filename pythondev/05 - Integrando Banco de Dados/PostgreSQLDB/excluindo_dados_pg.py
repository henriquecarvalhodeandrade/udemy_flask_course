from conexao_post import conn

cursor_obj = conn.cursor()

sql = '''
    DELETE FROM games 
    WHERE id = %s
'''

cursor_obj.execute(sql, (5, ))
conn.commit()
print("Dados excluidos com sucesso!")
conn.close()

