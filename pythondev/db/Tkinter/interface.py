import tkinter as tk
import orm
from tkinter import messagebox

'''criando os comandos para aplicação desktop'''
def add_movie():
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.add_movie(nome,ano,nota)
    messagebox.showinfo("Sucesso", "filme cadastrado")

def update_movie():
    id = entry_id.get()
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.update_movie(id,nome,ano,nota)
    messagebox.showinfo("Sucesso", "filme atualizado")

def delete_movie():
    id = entry_id.get()
    orm.delete_movie(id)
    messagebox.showinfo("Sucesso"," filme excluido")

'''Interface gráfica'''
root = tk.Tk()
root.title("Gerenciador de Filmes")

'''rótulos e campos de entrada'''
label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=1, column=0)
entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

label_ano = tk.Label(root, text="Ano:")
label_ano.grid(row=2, column=0)
entry_ano = tk.Entry(root, width=50)
entry_ano.grid(row=2, column=1, padx=10, pady=5)

label_nota = tk.Label(root, text="Nota:")
label_nota.grid(row=3, column=0)
entry_nota = tk.Entry(root, width=50)
entry_nota.grid(row=3, column=1, padx=10, pady=5)

'''criando os botões'''
button_adicionar = tk.Button(root, text='Adicionar filme', command=add_movie)
button_adicionar.grid(row=4,column=0,columnspan=2,pady=5)

button_atualizar = tk.Button(root, text='Atualizar filme', command=update_movie)
button_atualizar.grid(row=5,column=0,columnspan=2,pady=5)

button_excluir = tk.Button(root, text='Excluir filme', command=delete_movie)
button_excluir.grid(row=6,column=0,columnspan=2,pady=5)


root.mainloop()
