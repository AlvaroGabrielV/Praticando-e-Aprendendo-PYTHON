from os import system
system("cls")


menu = [
    "[0] - Fechar Programa "
    "[1] - Cadastrar Veiculo "
    "[2] - Cadastrar Cliente "
    "[3] - Mostrar Veiculos "


] 

veiculos = []

marcas = []

clientes = []

def cadastrar_Carro():
    marca = str(input("Marca do veiculo: "))
    modelo = str(input("Modelo do veiculo: "))
    KMrodados = float(input("Kilometragem inicial: "))
    preco_Carro = float(input("Preço da diaria: "))

    carro = {
        'marca': marca,
        'modelo': modelo,
        'kilometros': KMrodados,
        'preco': preco_Carro,

    }

    veiculos.append(carro)

def cadastrar_Cliente():
    nome = str(input("Nome do cliente: "))
    idade = int(input("Idade: "))
    opcao_Carro = int(input("Escolha o veiculo: "))
    carro_Alugado = veiculos[opcao_Carro]

def mostrar_Carros():
    for carro in veiculos:
        print("Marca:", carro['marca'])
        print("Modelo:", carro['modelo'])
        print(f"Kilometros: {carro['kilometros']:2.2f}")
        print(f"Preço: R${carro['preco']:2.2f}")
        print("    ")



while True:
    print("\n".join(menu)) 
    print()
    opcao = str(input("Informe a opção: "))

    if opcao == '1':
        cadastrar_Carro()

    elif opcao == '2':
        cadastrar_Cliente()

    elif opcao == '3':
        mostrar_Carros()
        input("Pressione ENTER para continuar...")

    elif opcao == '0':
        break        

    else:
        print("Opção inválida! Tente Novamente.")

    system("cls")
    
