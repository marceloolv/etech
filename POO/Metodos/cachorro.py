class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    # Metodo: Comportamento/ação
    def latir(self):
        return f"{self.nome} o cachorro esta latindo 'au au'"

    # Método: Comportamento que modifica o estado do objeto


    def fazer_aniversario(self):
        self.idade += 1  # MODIFICA O ATRIBUTO 'IDADE'
        return f"Parabéns! {self.nome} agora tem {self.idade}"

    # Método: Comportamento que usa multiplos atributos
    def apresentar(self):
        return f"Olá, sou {self.nome}, um {self.raca} de {self.idade} anos."

dog_a = Cachorro("Max", "Golden Retriever", 5)
dog_b = Cachorro("Luna", "Poodle", 2)

print(dog_a.apresentar())
print(dog_a.latir())

print(dog_b.apresentar())
print(dog_b.latir())

# Alterando o estado do Max attravés do metodo
print(dog_a.fazer_aniversario())
print(dog_a.apresentar()) # verifica a idade atualizada (6)


