class Aluno:
    def __init__(self, nome, nota):
        self.__nome = nome
        self.__nota = nota

    def get_nome(self):
        return self.__nome

    def get_nota(self):
        return self.__nota

    def set_nome(self, nome):
        self.__nome = nome

    def set_nota(self, valor):
        if 0<= valor <=10:
            self.__nota = valor
        else:
            print(f"Valor invalido! O valor deve estar entre 0 e 10.")

class Professor:
    def __init__(self, nome, nota):
        self.__nome = nome
        self.__nota = nota

    def get_nome_professor(self):
        return self.__nome

    def get_nota(self):
        return self.__nota

    def set_nome(self, nome):
        self.__nome = nome

    def set_nota(self, valor):
        if 0<= valor <=10:
            self.__nota = valor
        else:
            print(f"Valor invalido! O valor deve estar entre 0 e 10.")


aluno1 = Aluno("Marcelo", 5)
aluno1.set_nota(8)
aluno1.set_nome("marcelo Fernandes")

#acessando os dados via getters
print(f"Aluno: {aluno1.get_nome()} | nota: {aluno1.get_nota()}")
