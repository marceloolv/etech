
class Personagem:  # Super Classe ou Classe Pai ou mãe
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

class Heroi(Personagem):  # subclasse ou classe filha
    def __init__(self, nome, vida, habilidade):
        super().__init__(nome, vida)
        self.habilidade = habilidade

class Vilao(Personagem):   # subclasse ou classe filha
    def __init__(self, nome, vida, poder):
        super().__init__(nome, vida)
        self.poder = poder

def atacar(personagem):
    print(f"{personagem.nome} esta atacando e tem {personagem.vida} de vida")

heroi1 = Heroi("Superman", 98, "Voo")
vilao1 = Vilao("Lex Luthor", 80, "inteligencia")

atacar(heroi1)
atacar(vilao1)

