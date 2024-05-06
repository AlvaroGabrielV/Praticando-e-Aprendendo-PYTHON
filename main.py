carros = []
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

    carros.append(carro)
   
def cadastrar_Cliente():
    nome = str(input("Nome do cliente: "))
    idade = int(input("Idade: "))
    opcao_Carro = int(input("Escolha a marca do veiculo: "))
    carro_Alugado = carros[opcao_Carro]
