
#Historico de vendas

vendas = []

def Historico():
    for indice, carros in enumerate(vendas):
        print(f"{indice}. Marca: {vendas[indice]['marca']} | Modelo: {vendas[indice]['modelo']} | Valor: R${vendas[indice]['preco']:.2f}\n")
