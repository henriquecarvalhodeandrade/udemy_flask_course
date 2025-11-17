# Fazendo a requisição dos filmes mais famosos usando a api do site themoviedb
import urllib.request, json

url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=3d233df44d861ce3baf0b9b31ecb14d4'

resposta = urllib.request.urlopen(url) 
print(resposta, "\n")

# com este código nós estamos fazendo a requisição ao site e o site está
# devolvendo a requisição com o HTTPResponse, mas note que ele retorna um objeto que
# humanamente não conseguimos ler, então devemos ler este objeto usando outro método, veja:

dados = resposta.read()
print(dados, "\n")
print(type(dados), "\n")

# Note que este valores não estão em formato json, que é o formato padrão para 
# sites da internet. logo:

jsondata = json.loads(dados) # aqui ele vai transformar o resultado em formato json
print(jsondata, "\n")
print(type(jsondata), "\n")

# vamos retornar apenas os resultados:
print(jsondata['results'], "\n")


