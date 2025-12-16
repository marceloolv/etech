class Funcionario:
    def __init__(self, nome):
        self.__nome = nome   #Atributo privado

    def get_nome(self):
        return self.__nome   ## getter

    def calcular_salario(self):
        return 0           # è o metodo que sera sobrescrito (polimorfismo)


class FuncionarioCLT(Funcionario):
    def __init__(self, nome, salario_fixo):
        super().__init__(nome)
        self.__salario = salario_fixo

    def get__salario(self):
        return self.__salario  #getter

    def calcular_salario(self):
        return self.__salario


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome)
        self.__horas = horas_trabalhadas
        self.__valor_hora = valor_hora

    def caucular_salario(self):
        return self.__horas * self.__valor_hora   #salario por hora


# ------- programa principal ---------
funcionarios = []    # lista de objetos
total_folha = 0

quantidade = int(input("Quantos funcionarios deseja cadastrar? "))

for i in range(quantidade):
    print(f"\n1 - Funcionario CLT")
    print(f"2 - Funcionario Horista")
    tipo = int(input("Escolha o tipo de funcionario :"))

    nome = input("Digite o nome do funcionario: ")

    if tipo == 1:
        salario = float(input("Digite o salario Fixo: "))
        funcionario = FuncionarioCLT(nome, salario)

    elif tipo == 2:
        horas = float(input("Digite as horas trabalhadas: "))
        valor = float(input("Digite o valor da hora: "))
        funcionario = FuncionarioHorista(nome, horas, valor)

    else:
        print("Tipo Invalido. Funcionario não encontrado")
        continue

    funcionarios.append(funcionario)

for f in funcionarios:
    salario = f.calcular_salario()                    #polimorfismo
    print(f"{f.get_nome()} - Salario: R$ {salario: .2f}")
    total_folha += salario

print(f"\n Total da folha: {total_folha}")
