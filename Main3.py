from funcionario import Funcionario

funcionarios = []  #lista que ira armazenar os objetos funcionario
total_folha = 0    #vareaval para acumular o total da folha de pagamento
quantidade = int(input("Quantos funcionarios deseja cadastrar? "))
c = 0
while c < quantidade:
    c +=1
    while True:
        nome = input("Nome do funcionario: ")
        try:
            salario = float(input("Digite o Sálario: "))
            if salario < 0:
                print("O Salario não pode ser negativo")
            else:
                break   #sai do laço
        except ValueError:
            print("Erro: Digite um numero para salario")

    # Criação do objeto funcionario
    funcionario = Funcionario(nome, salario)
    # adiciona funcionario na lista
    funcionarios.append(funcionario)

print("\n*** Folha de pagamento\n ***")
for funcionario in funcionarios:
    total_folha += funcionario.calcular_salario()
    print(f"Funcionario: {funcionario.get_nome()}, Salario: {funcionario.get_salario()}")

print(f"Total da folha: {total_folha}")




