def adicionar_usuario(cursor, id, nome, email):
    """Adiciona um usuário a um banco de dados"""
    cursor.execute(
        '''
        INSERT INTO usuarios(id, nome, email) VALUES(?,?,?)
        ''', (id, nome, email)
    )

def buscar_usuario(cursor, email):
    """ Busca um usuario pelo seu email """
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email, ))
    return cursor.fetchone()

