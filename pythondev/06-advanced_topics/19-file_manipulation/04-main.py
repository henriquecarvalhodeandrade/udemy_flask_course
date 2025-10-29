from agenda import add_contact, view_contacts, delete_contacts

def main():
    while True:
        print("\nAgenda de Contatos")
        print('1. Adiciona Contato')
        print('2. Lista Contato')
        print('3. Deleta todos os Contatos')
        print('0. Sair')

        choice = input("Escolha uma das opções acima.\n")

        if choice == '1':
            add_contact()

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            delete_contacts()

        elif choice == "0":
            break

        else:
            print("Escolha uma das opções!")

if __name__ == '__main__':
    main()
    

