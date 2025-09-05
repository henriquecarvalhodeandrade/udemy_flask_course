name = input("Insira o nome do filme: \n")
year = int(input('Digite o ano de lançamento: \n'))
noteMovie= float(input('Digite a nota de classificação: \n'))

# Alternativas de concatenação:
print("Descrição do Filme:")
print("===================")

# 1)
print("Nome do filme: " , name)
print("Ano do filme: " ,year)
print("Nota do filme: " ,noteMovie)

# 2)
print("Nome do filme: " , name, "Ano do filme: " ,year, "Nota do filme: " ,noteMovie)

# 3)
print(f"Nome do filme: {name}\nAno do filme: {year}\nNota do filme: {noteMovie}")