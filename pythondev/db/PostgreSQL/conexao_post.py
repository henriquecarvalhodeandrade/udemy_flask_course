'''este arquivo serve como módulo para criar uma conexão com o database'''
import psycopg2

'''conexao'''
conn = psycopg2.connect(
    database = 'db_games',
    user = 'postgres',
    password = '#henR901.',
    host = 'localhost',
    port = '5432',
)