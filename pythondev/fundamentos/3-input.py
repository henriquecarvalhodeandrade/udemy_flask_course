# Usando inputs

name = input("Insira o nome do filme: \n")
year = input('Digite o ano de lançamento: \n')
noteMovie= input('Digite a nota de classificação: \n')
planIncluded = False


print(name)
print(year)
print(noteMovie)
print(planIncluded)

print(type(name))
print(type(year))
print(type(noteMovie))
print(type(planIncluded))

'''
Perceba que ao usar input, ele converte toda a entrada para uma string.

Por isso devemos tratar esses inputs:
'''

name = input("Insira o nome do filme: \n")
year = int(input('Digite o ano de lançamento: \n'))
noteMovie= float(input('Digite a nota de classificação: \n'))

print(type(name))
print(type(year))
print(type(noteMovie))
print(type(planIncluded))