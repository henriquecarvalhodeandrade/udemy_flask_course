import xml.etree.ElementTree as ET

dados = '''<?xml version="1.0" encoding="utf-8"?>
<clientes>

    <cliente>
        <id>1</id>
        <nome>Rodrigo</nome>
        <idade>25</idade>
        <cidade>BH</cidade>
    </cliente>

    <cliente>
        <id>2</id>
        <nome>Fulano</nome>
        <idade>30</idade>
        <cidade>SP</cidade>
    </cliente>

    <cliente>
        <id>3</id>
        <nome>Douglas</nome>
        <idade>35</idade>
        <cidade>RJ</cidade>
    </cliente>

</clientes>
'''

caminho_arquivo = "data/clientes.xml"

# 1 - Exportando dados para xml
with open(caminho_arquivo, 'w', encoding='utf-8') as f:
    f.write(dados)

# 2 - Lendo dados do xml
tree = ET.parse(caminho_arquivo)
root = tree.getroot()

for cliente in root.findall("cliente"):
    id_cliente = cliente.find("id").text
    nome_cliente = cliente.find("nome").text

    print(f'ID: {id_cliente} -> Nome: {nome_cliente}')

# 3 - Adicionando novo cliente
novo_cliente = ET.Element("cliente")
id_novo = ET.SubElement(novo_cliente, "id")
id_novo.text = "5"
nome_novo = ET.SubElement(novo_cliente, "nome")
nome_novo.text = "Marcos"
idade_novo = ET.SubElement(novo_cliente, "idade")
idade_novo.text = "40"
cidade_novo = ET.SubElement(novo_cliente, "cidade")
cidade_novo.text = "AM"

root.append(novo_cliente)

# 4 - Salvando no xml
tree.write(caminho_arquivo, encoding='utf-8', xml_declaration=True)


