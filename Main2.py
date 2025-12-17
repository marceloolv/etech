from POO.Encapsulamento.Aluno import Aluno, Professor

aluno1 = Aluno("Marcelo", 5)
aluno1.set_nota(8)
aluno1.set_nome("marcelo Fernandes")

#acessando os dados via getters
print(f"Aluno: {aluno1.get_nome()} | nota: {aluno1.get_nota()}")

professor1 = Professor("Marcos", 6)
print(professor1.get_nota())