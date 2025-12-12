class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        print(f"{self.nome} faz um genérico")


class Cachorro(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} é da raça {self.raca} esta latindo: Au Au!")

    def mostrar_detalhes(self):
        print(f"Nome: {self.nome} | Espécie: {self.especie} | Raça: {self.raca}")


class Gato(Animal):
    def __init__(self, nome, especie, cor_pelo, raca):
        super().__init__(nome, especie)
        self.cor_pelo = cor_pelo
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} é da raça {self.raca} esta miando: Miau mial!")

    def mostrar_detalhes(self):
        print(f"Nome: {self.nome} | Espécie: {self.especie} | Cor do pelo: {self.cor_pelo} | Raça: {self.raca}")


cachorro1 = Cachorro("Ducky", "Canino", "Golden Retriever")

gato1 = Gato("Laura", "Felino", "Branco", "Siamês")

print(f"Nome do herdado: {cachorro1.nome}")
cachorro1.fazer_som()
cachorro1.mostrar_detalhes()
print()
print(f"Nome do herdado: {gato1.nome}")
gato1.fazer_som()
gato1.mostrar_detalhes()

