import pandas as pd

# 1 - Importing Data
tb_clients = pd.read_excel('data/clients.xlsx', sheet_name='Tab 3')

print(tb_clients)
print(type(tb_clients))


# 2 - Adding Columns
tb_clients = pd.read_excel('data/clients.xlsx', index_col=0)
print(tb_clients)

# 3 - Importing Specific Columns
tb_clients = pd.read_excel('data/clients.xlsx', usecols=[1,2])
print(tb_clients)

# 4 - Exporting Data to Spreadsheet
tb_clients_tab1 = pd.read_excel('data/clients.xlsx', sheet_name='Tab 1')
tb_clients_tab2 = pd.read_excel('data/clients.xlsx', sheet_name='Tab 2')

with pd.ExcelWriter('data/new_clients.xlsx') as new_spreadsheet:
    tb_clients_tab1.to_excel(new_spreadsheet, sheet_name='Tab 1', index=False)
    tb_clients_tab2.to_excel(new_spreadsheet, sheet_name='Tab 2', index=False)

    

