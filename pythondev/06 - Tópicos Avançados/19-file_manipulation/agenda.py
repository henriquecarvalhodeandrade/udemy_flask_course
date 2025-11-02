
import os

def add_contact():
    name = input("Inform your name:\n")
    address = input("Inform your address:\n")
    phone = input("Inform your phone number:\n")

    contact = f"Nome: {name}\nAddress: {address}\nPhone: {phone}\n"

    with open("data/contacts.txt", "a", encoding="utf-8") as file:
        file.write(contact)

def view_contacts():
    if not os.path.exists("data/contacts.txt"):
        print("Lista de contatos está vazia.")

    with open("data/contatos.txt", 'r', encoding='utf-8') as file:
        contacts = file.read()
    print("Lista de Contatos:")
    print(contacts)

def delete_contacts():
    if not os.path.exists("data/contacts.txt"):
        print("Lista de contatos está vazia.")

    with open("data/contacts.txt", 'w', encoding='utf-8') as file:
        file.write('')
        print("Contatos excluidos com sucesso.")