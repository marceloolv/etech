class Funcionario:
    # este é um atributo de classe, é uma vareavel compartilhada por todas as
    # instancias(objeto) de funcionario, o valor é o mesmo para todos
    taxa_bonus = 0.10

    def __init__(self, nome, cargo, salario ):
        #Atributo da instancia: exclusivo desse objeto, O self garante
        # que este nome pertença apenas ao funcionario atual
        self.nome = nome
        #Atributo da instancia: exclusiva deste objeto
        self.cargo = cargo
        # Atributo da instancia: exclusiva deste objeto
        # converte o valor de texto (inout) para numero inteiro
        self.salario = salario

    def calcular_bonus(self):
        #Logica de Metodo
        #usa o 'self.salario'
        return self.salario * Funcionario.taxa_bonus

print("-"*40)
print("Cadastro de Funcioario (1/2")
print("-"*40)

nome_a = input("Nome do Funcionario A:")
cargo_a = input("Cargo do Funcionario A:")
salario_a = float(input("Salario (Apenas números inteiros) do Funcionario A:"))

func_a = Funcionario(nome_a, cargo_a, salario_a)

print("-"*40)
print("Cadastro de Funcionario (2/2")
print("-"*40)

nome_b = input("Nome do Funcionario B:")
cargo_b = input("Cargo do Funcionario B:")
salario_b = input("Salario (Apenas números inteiros) do Funcionario B:")

func_b = Funcionario(nome_b, cargo_b, salario_b)

print(f"Bonus de {func_a.nome}: R$ {func_a.calcular_bonus(): }")
print(f"Bonus de {func_b.nome}: R$ {func_b.calcular_bonus(): }")