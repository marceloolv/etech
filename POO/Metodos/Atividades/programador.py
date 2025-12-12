class Programador:

    def __init__(self, nome, linguagem):
        self.nome = nome
        self.linguagem = linguagem
        self.produtividade = 100

    def codificar(self, horas):
        self.produtividade -= (horas * 5)
        print(f"O programador {self.nome} produziu por {horas} hrs e baixou a produtividade para {self.produtividade} pontos.")

    def tomar_cafe(self):
        self.produtividade += 5
        print(f"Ao tomar um café o programador {self.nome} restaurou sua produtividade para {self.produtividade} pontos.")

    def verifica_produtividade(self):
        print(f"A produtividade atual do programador {self.nome} está em {self.produtividade} pontos.")


programador1 = Programador("Ladislau", "Python")

programador1.codificar(3)
programador1.tomar_cafe()
programador1.verifica_produtividade()

