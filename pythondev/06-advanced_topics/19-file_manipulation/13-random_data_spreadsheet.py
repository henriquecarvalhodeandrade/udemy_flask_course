import pandas as pd
import numpy as np

data_tab = {
    'ID': [1,2,3,4,5],
    'Nome': ['Ana','Carlos','Lucas','Fernanda', 'Mariana'],
    'Cidade': ['São Paulo','Rio de Janeiro','Curitiba','Porto Alegre','Salvador']
}

data_tab2 = {
    'ID': [1,2,3,4,5],
    'Nome': ['Bia','Henrique','Maria','Vitoria', 'Angelo'],
    'Cidade': ['Brasília','Rio Grande do Norte','Goiás','Porto Alegre','Salvador']
}

data_tab3 = {
    'ID': [1,2,3,4,5],
    'Nome': ['Flavia','Nicollas','Luciano','Bruno', 'Vitor'],
    'Cidade': ['São Paulo','Rio de Janeiro','Curitiba','Sergipe','Amazonas']
}

data_tab4 = {
    'ID': [1,2,3,4,5],
    'Nome': ['Rafaela','Rogerio','Vanessa','Sara', 'Yasmin'],
    'Cidade': ['São Paulo','Rio de Janeiro','Curitiba','Porto Alegre','Salvador']
}

df_tab = pd.DataFrame(data_tab)
df_tab2 = pd.DataFrame(data_tab2)
df_tab3 = pd.DataFrame(data_tab3)
df_tab4 = pd.DataFrame(data_tab4)

path = 'data/clients.xlsx'

with pd.ExcelWriter(path, engine='openpyxl') as writer:
    df_tab.to_excel(writer, sheet_name='Tab 1', index=False)
    df_tab2.to_excel(writer, sheet_name='Tab 2',index=False)
    df_tab3.to_excel(writer, sheet_name='Tab 3',index=False)
    df_tab4.to_excel(writer, sheet_name='Tab 4',index=False)

print(f'Excel file with 4 tabs sucessfully created, you can take a look in {path}!')
