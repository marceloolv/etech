class PlayerMusical:
    def __init__(self):
        self.volume = 50
        self.tocando = False

    def play(self):
        if self.tocando == False:
            self.tocando = True
            print(f"Musica iniciada")

    def pause(self):
        if self.tocando == True:
            self.tocando = False
            print(f"Musica pausada")

    def aumentar_volume(self, passos):
        if (self.volume + passos) > 100:
            maximo_passos = 100 - self.volume
            print(f"O volume esta em {self.volume}, e vai até 100 passos, o Player não suporta mais {passos} passos, tente novamente e coloque no máximo {maximo_passos} passos!")
        else:
            self.volume += passos
            print(f"o Volume foi aumentado para {self.volume} passos.")


player_1 = PlayerMusical()
player_1.play()
player_1.pause()
player_1.aumentar_volume(40)