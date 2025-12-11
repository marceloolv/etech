class Nave:
    def __init__(self, nome, combustivel):
        self.nome = nome
        self.combustivel = combustivel
        self.status = "Estacionada"

    def decolar(self):
        #Primeiro verificamos se ha combustivel na nva pelo menos 20
        if self.combustivel >= 20:
            self.combustivel -= 20  #gasta 20 unidade de combustivel
            self.status = "Em voo"  #Atualiza o status da nave
            print(f"A Nave {self.nome} Decolou restante: {self.combustivel}")
        else:
            print("Combustivel insuficiente!")

    def recarregar(self, quantidade):
        self.combustivel += quantidade
        print(f"Combustivel recarregado, Nivel atual  {self.combustivel} ")


    def verificar_status(self,):
        print(f"A Nave {self.nome} esta {self.status} com {self.combustivel} lts de combustivel")


nave_1 = Nave("Apolo", 10)

nave_1.verificar_status()  # mostra o status atual
nave_1.decolar()           # enta decolar, mais nao vai conseguir
nave_1.recarregar(50)      # recarrega combustivel
nave_1.decolar()           # agora a nave consegue decolar
nave_1.verificar_status()  # Mostra o novo status atual