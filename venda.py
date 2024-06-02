from Carros import carros 
from dataclasses import dataclass
from os import system
from historico import vendas 

# Venda e valor total vendido

@dataclass
class Venda:
    totalvalor: float 
    totalvendido = 0

    @classmethod
    def vender_carro(self):
        vender = input("Informe o modelo a ser vendido: ").upper()
        
        for indice, carro in enumerate(carros):
            if carro['modelo'] == vender:
                Venda.totalvendido += carro['preco']                
                print(f"\nO veiculo do modelo {carro['modelo']} foi vendido por R${Venda.totalvendido:.2f}!")
                vendas.append(carros[indice])
                del carros[indice]
                system("pause")

        