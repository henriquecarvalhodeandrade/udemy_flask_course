def my_decorator(function):
    def wrapper():
        print("Antes de Executar a função")
        function()
        print("Depois de executar a função")
    return wrapper

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        string_splitted = func.split()
        return string_splitted
    return wrapper
 