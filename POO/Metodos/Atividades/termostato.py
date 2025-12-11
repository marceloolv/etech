class Termostato:

    def __init__(self, temperatura = 20):
        #Atributo da instância
        self.temperatura = temperatura

    #metodo que adiciona graus a temperatura
    def aumentar(self, graus):
        self.temperatura += graus
        print(f"Temperatura aumentada para: {self.temperatura}º")

    def diminuir(self, graus):
        self.temperatura -= graus
        print(f"Temperatura diminuida para: {self.temperatura}º")

meu_termostato = Termostato()
print(f"Inicial!: {meu_termostato.temperatura}")
meu_termostato.aumentar(3)
meu_termostato.diminuir(1)
print(f"temperatura final: {meu_termostato.temperatura}")