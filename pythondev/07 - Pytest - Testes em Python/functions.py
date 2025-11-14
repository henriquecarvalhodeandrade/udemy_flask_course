def is_positive(number):
    return number > 0

def sub(a,b):
    return a-b

def lenght(list):
    return len(list)

def validate_email(email):
    return ('@' in email) and ('.' in email)

def somar_lista(valores):
    """ Soma todos os valores de uma lista. """
    if not all(isinstance(i,(int, float)) for i in valores):
        raise ValueError("Todos os valores da lista devem ser numéricos.")
    
    return sum(valores)

def encontrar_valor(dicionario, chave):
    """ Retorna o Valor associado à sua Chave do Dicionário. """
    if not all(isinstance(dicionario, dict)):
        raise ValueError("O primeiro argumento deve ser um dicionário.")

    return dicionario.get(chave, None)
