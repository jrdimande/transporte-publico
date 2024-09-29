from Chapa import *

def menu():
    empresa = TransporteEmpresa("Mozambique-Transporte")

    while True:
        print("\n=== Menu ===")
        print("1. Adicionar Autocarro")
        print("2. Remover Autocarro")
        print("3. Adicionar Rota")
        print("4. Mostrar Autocarros")
        print("5. Mostrar Rotas")
        print("6. Adicionar Passageiro a um Autocarro")
        print("7. Remover Passageiro de um Autocarro")
        print("8. Mostrar Passageiros de um Autocarro")
        print("9. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            marca = input("Marca do autocarro: ")
            modelo = input("Modelo do autocarro: ")
            matricula = input("Matrícula do autocarro: ")
            capacidade = int(input("Capacidade do autocarro: "))
            autocarro = Autocarro(marca, modelo, matricula, capacidade)
            empresa.adicionar_autocarro(autocarro)

        elif escolha == "2":
            matricula = input("Matrícula do autocarro a remover: ")
            autocarro = next((a for a in empresa.autocarros if a.matricula == matricula), None)
            if autocarro:
                empresa.remover_autocarro(autocarro)
            else:
                print("Autocarro não encontrado!")

        elif escolha == "3":
            nome_rota = input("Nome da rota: ")
            origem = input("Origem da rota: ")
            destino = input("Destino da rota: ")
            distancia = int(input("Distância da rota (km): "))
            rota = Rota(nome_rota, origem, destino, distancia)
            empresa.rotas.append(rota)
            print(f"Rota {nome_rota} adicionada!")

        elif escolha == "4":
            empresa.exibir_info()

        elif escolha == "5":
            empresa.exibir_info()

        elif escolha == "6":
            matricula = input("Matrícula do autocarro: ")
            autocarro = next((a for a in empresa.autocarros if a.matricula == matricula), None)
            if autocarro:
                passageiro = input("Nome do passageiro: ")
                autocarro.adicionar_passageiro(passageiro)
            else:
                print("Autocarro não encontrado!")

        elif escolha == "7":
            matricula = input("Matrícula do autocarro: ")
            autocarro = next((a for a in empresa.autocarros if a.matricula == matricula), None)
            if autocarro:
                passageiro = input("Nome do passageiro: ")
                autocarro.remover_passageiro(passageiro)
            else:
                print("Autocarro não encontrado!")

        elif escolha == "8":
            matricula = input("Matrícula do autocarro: ")
            autocarro = next((a for a in empresa.autocarros if a.matricula == matricula), None)
            if autocarro:
                autocarro.mostrar_passageiros()
            else:
                print("Autocarro não encontrado!")

        elif escolha == "9":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

menu()

