class Interruptor:
    def __init__(self):
        self.ligada = False
    def alternar(self):
        if self.ligada == True:
            print(f"Interrupitor Ligado!")
            self.ligada = False
        else:
            print(f"Interrupitor Desligado!")
            self.ligada = True

interruptor_1 = Interruptor()
interruptor_1.alternar()
interruptor_1.alternar()
interruptor_1.alternar()
interruptor_1.alternar()