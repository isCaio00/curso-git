lista = []

while True:
    print(10 * "=")
    print("LISTA DE COMPRAS")
    print(10 * "=")
    opcao = int(input("""
    1 - Adicionar Produto
    2 - Ver Lista
    3 - Remover Produto
    4 - Sair
    Escolha uma opção: 
        """))

    if opcao == 1:
        produto = input("Digite o nome do produto: ")
        lista.append(produto)
        print("Produto adicionado !")

    elif opcao ==2:
        for produto in lista:
            print("Produto:", produto)

    elif opcao ==3:
        remover = input("Digite o nome do produto que deseja remover: ")
        if remover in lista:
            lista.remove(remover)
            print("Produto removido !")
        else:
            print("Esse produto não está na lista. ")

    elif opcao ==4:
        print("Encerrando sistema !")
        break