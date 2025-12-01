# 3- Criar um programa para adicionar funcionários. Os funcionários
# devem ter nome, sexo e salário o programa deve retornar a
# soma de salários dos homens e soma dos salários das mulheres

soma_salario_homens = 0
soma_salario_mulheres = 0
print(f'{" CADASTRO DE FUNCIONÁRIOS ":=^50}')
while True:
    nome = input("Nome......: ")
    sexo = " "
    while sexo not in "MF":
        sexo = input("Sexo [M/F]:").upper()
        if sexo not in "MF":
            print("Opção invalida! Informe o Sexo novamente.")
    salario = float(input("Salário...: "))
    if sexo == "M":
        soma_salario_homens += salario
    else:
        soma_salario_mulheres += salario
    opcao = " "
    while opcao not in "SN":
        opcao = input("Deseja cadastrar outro funcionário [S/N]?").upper()
        if opcao not in "SN":
            print("Opção invalida! Digite [S/N].")
    print("-" * 50)
    if opcao == "N":
        break
print(f"A somatória dos salários dos Homens é {soma_salario_homens:.2f}")
print(f"A somatória dos salários das Mulheres é {soma_salario_mulheres:.2f}")




