class Autocarro:
    def __init__(self, marca, modelo, matricula, capacidade):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.capacidade = capacidade
        self.passageiros = []

    def adicionar_passageiro(self, passageiro):
        if len(self.passageiros) < self.capacidade:
            if passageiro not in self.passageiros:
                self.passageiros.append(passageiro)
                print(f"Passageiro {passageiro.title()} Adicionado")
            else:
                print("O passageiro já se encontra na lista")
        else:
            print("Excedeu o limite de passageiros!")

    def remover_passageiro(self, passageiro):
        if passageiro in self.passageiros:
            self.passageiros.remove(passageiro)
            print(f"Passageiro {passageiro.title()} removido!")
        else:
            print(f"Passageiro {passageiro.title()} não encontrado")

    def mostrar_passageiros(self):
        if self.passageiros:
            print("Passageiros:")
            for passageiro in self.passageiros:
                print(f"\t{passageiro.title()}")
        else:
            print("Nenhum passageiro encontrado!")


class Rota:
    def __init__(self, nome_rota, origem, destino, distancia):
        self.nome_rota = nome_rota
        self.origem = origem
        self.destino = destino
        self.distancia = distancia
        self.autocarros = []

    def adicionar_autocarro(self, autocarro):
        if autocarro not in self.autocarros:
            self.autocarros.append(autocarro)
            aut = f"{autocarro.marca} {autocarro.modelo} {autocarro.matricula}"
            print(f"Autocarro {aut.title()} Adicionado a rota {self.nome_rota.title()}")
        else:
            aut = f"{autocarro.marca} {autocarro.modelo}| Matricula: {autocarro.matricula} |capacidade: {autocarro.capacidade}"
            print(f"O Autocarro {aut.title()} está na lista!")

    def remover_autocarro(self, autocarro):
        if autocarro in self.autocarros:
            self.autocarros.remove(autocarro)
            aut = f"{autocarro.marca} {autocarro.modelo}| Matricula: {autocarro.matricula} |capacidade: {autocarro.capacidade}"
            print(f"Autocarro {aut.title()} removido da lista!")
        else:
            print(f"Autocarro {autocarro.matricula.title()} não encontrado")

    def mostrar_autocarros(self):
        if self.autocarros:
            print(f"Autocarros disponíveis na rota {self.nome_rota.title()}:")
            for autocarro in self.autocarros:
                aut = f"{autocarro.marca} {autocarro.modelo}| Matricula: {autocarro.matricula} |capacidade: {autocarro.capacidade}"
                print(f"{aut.title()}")
        else:
            print("Nenhum autocarro disponível nesta rota!")


class TransporteEmpresa:
    def __init__(self, nome_empresa):
        self.rotas = []
        self.autocarros = []

    def adicionar_autocarro(self, autocarro):
        if autocarro not in self.autocarros:
            self.autocarros.append(autocarro)
            aut = f"{autocarro.marca} {autocarro.modelo}| Matricula: {autocarro.matricula} |capacidade: {autocarro.capacidade}"
            print(f"Autocarro {aut.title()} Adicionado")
        else:
            print(f"Autocarro {aut.title()} já se encontra registado")

    def remover_autocarro(self, autocarro):
        if autocarro in self.autocarros:
            self.autocarros.remove(autocarro)
            aut = f"{autocarro.marca} {autocarro.modelo}| Matricula: {autocarro.matricula} |capacidade: {autocarro.capacidade}"
            print(f"Autocarro {aut.title()} Removido")
        else:
            print(f"Autocarro {aut.title()} não encontrado")

    def exibir_info(self):
        if self.autocarros:
            print("Autocarros disponíveis:")
            for autocarro in self.autocarros:
                aut = f"{autocarro.marca} {autocarro.modelo} | Matricula: {autocarro.matricula} | Capacidade: {autocarro.capacidade}"
                print(aut)
        else:
            print("Nenhum autocarro disponível")

        if self.rotas:
            print("Rotas disponíveis:")
            for rota in self.rotas:
                print(f"{rota.nome_rota} | Origem: {rota.origem} | Destino: {rota.destino} | Distância: {rota.distancia} km")
        else:
            print("Nenhuma rota disponível")


