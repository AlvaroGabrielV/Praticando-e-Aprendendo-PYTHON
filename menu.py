from Carros import Carro
from dataclasses import dataclass
from os import system
from time import sleep
from venda import Venda
from historico import Historico

# Menu Principal com as opçoes 

@dataclass
class Menu:
    while True:
        system("cls")
        
        print("Concessionária de automóveis")
        print("\n1. Cadastrar Carro")
        print("2. Mostrar Carros")
        print("3. Vender Carro")
        print("4. Historico de vendas")
        print("5. Sair\n")

        print("Total vendido: R$", Venda.totalvendido)
        
        opcao = input("\nDigite a opção desejada: ")

        if opcao == "1":
            system("cls")
            Carro.cadastrar_carro()
            print("\nCarro cadastrado com sucesso!")
            sleep(0.5)

        elif opcao == "2":
            system("cls")
            Carro.mostrar_carro()
            system("\npause")
        
        elif opcao == "3":
            system("cls")
            Carro.mostrar_carro()
            Venda.vender_carro()
            
        elif opcao == "4":
            system("cls")   
            Historico()
            system("pause")     

        elif opcao == "5":
            system("cls")
            print("Saindo do programa...")
            sleep(0.5)
            system("cls")
            print("Programa finalizado com sucesso!")
            break

        else:
            print("Opção inválida. Tente novamente.")