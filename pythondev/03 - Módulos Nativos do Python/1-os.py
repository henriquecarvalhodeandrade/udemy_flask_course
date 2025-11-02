import os

'''
Consultar Funcionalidades
'''

# No terminal digitar "help('os')"

'''Retornar a pasta presente'''
print(os.getcwd())

'''Listar arquivos e pastas'''
print(os.listdir())

'''Verificar versão do sistema operacional'''
os.system('ver')

'''Config. da máquina'''
os.system('systeminfo')

'''Limpar a tela do terminal'''
os.system('cls')

'''Desligar o computador'''
os.system('shutdown /s')
os.system('shutdown /s /t 0') # desliga imediantamente

'''Cancelar o desligamento'''
os.system('shutdown /a')

'''Funções de exmplo usando os'''
def turn_off_one_hour():
    os.system('shutdown /s /t 3600') # tempo em segundos

def turn_off_half_an_hour():
    os.system('shutdown /s /t 1800') # tempo em segundos

def cancel_turn_off():
    os.system('shutdown /a') # tempo em segundos



