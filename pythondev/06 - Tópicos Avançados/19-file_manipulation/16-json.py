import json

dados = {
    "clientes": [
        {"id":1, "nome": "Ana", "idade": 25, "cidade": "São Paulo"},
        {"id":2, "nome": "Carlos", "idade": 30, "cidade": "Rio de Janeiro"},
        {"id":3, "nome": "Fernanda", "idade": 22, "cidade": "Curitiba"},
        {"id":4, "nome": "João", "idade": 35, "cidade": "Belo Horizonte"}
    ] 
}

caminho_arquivo = "data/clientes.json"

# 1 - Escrevendo dados em arquivo json
with open(caminho_arquivo, 'w', encoding="utf-8") as f:
    json.dump(dados, f, indent=4)

# 2 - Lendo os dados do arquivo json
with open(caminho_arquivo, "r", encoding="utf-8") as f:
    dados_lidos = json.load(f)
    print(dados_lidos)

# 3 - Manipulando dados
for cliente in dados_lidos["clientes"]:
    if cliente["nome"] == "Carlos":
        cliente["idade"] = 20

novo_cliente = {"id": 5, "nome": "Samir", "idade": 28, "cidade": "Florianópolis"}
dados_lidos["clientes"].append(novo_cliente)

# 4 - Salvar os dados manipulados
with open(caminho_arquivo, "w", encoding='utf-8') as f:
    json.dump(dados_lidos, f, indent=4)

