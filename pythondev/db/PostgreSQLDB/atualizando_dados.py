from conexao_post import conn

cursor_obj = conn.cursor()

sql = '''
    UPDATE games  
    SET name = %s
    WHERE ID = %s

'''

'''devo passsar os valores dentro de uma tupla'''
cursor_obj.execute(sql, ('Fifa 23', 3))
conn.commit()
print("Dados atualizados com sucesso!")
conn.close()