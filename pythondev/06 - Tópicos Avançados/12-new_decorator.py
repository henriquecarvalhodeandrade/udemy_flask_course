from .decorator import my_decorator, uppercase_decorator, split_string

@my_decorator
def my_function():
    print("Dentro da Função")
my_function()

print()

@uppercase_decorator
def text():
    return 'hello world'
print(text())

print()

@split_string
def example():
    return 'Aprendendo Python e criando decorators'

print(example())
 