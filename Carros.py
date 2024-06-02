from dataclasses import dataclass

# cadastro e exibir carros 

@dataclass
class Carro:
    marca: str
    modelo: str
    preco: float
    
    @classmethod
    def cadastrar_carro(self):
        marca = input("Digite a marca do carro: ").upper()
        modelo = input("Digite o modelo do carro: ").upper()
        preco = float(input("Digite o preço do carro: "))

        carro = {
            'marca': marca,
            'modelo': modelo,
            'preco': preco
        }
        carros.append(carro)
        
    @classmethod
    def mostrar_carro(self):
        for carro in carros:
            print(f"Marca: {carro['marca']} | Modelo: {carro['modelo']} | Preço: R${carro['preco']:.2f}\n")
 
                
carros = []