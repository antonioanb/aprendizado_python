#lista de compras com as opções de inserir apagar listas sair

import os

lista = []

while True:
    print("--LISTA DE COMPRAS--")
    opcao = input(" Escolha um a opção [i]Insert, [a]Apagar, [l]Listar,[s]Sair-> ").lower()

    #limpar a tela de forma universal (windows ou linux)
    os.system("cls" if os.name == "nt" else "clear")

    if opcao == "i":
        valor = input("ok adicione um item: ")
        lista.append(valor)
        print(f"{valor} adicionado !")

    elif opcao == "a":
        try:
            indice = int(input("digita o um indice para apagar: "))
            removido = lista.pop(indice)
            print(f"Item {removido} removido.")
        except ValueError:
            print("Erro: por favor digite um numero inteiro")
        except IndexError:
            print("Erro: Esse indice não existe na lista")

    elif opcao == "l":
        if not lista:
            print("a lista esta vazia")
        else:
            for i, v in enumerate(lista):
                print(f"indice: {i}  Valor: {v}")
                print("-" * 10)
    elif opcao == "s":
        print("Saindo do sistema .... Até logo ! 👋")
        break
    else:
        print("opção invalida, escolha entre i, a, l ou s")