def calcular_combustivel(missoes_base, *gastos_adicionais):
    combustivel_base = missoes_base * 100
    total_adicional = 0
    for gasto in gastos_adicionais:
        total_adicional += gasto

    total_geral = combustivel_base + total_adicional
    print(f"Total de combustivel necessário: {total_geral}")

missoes = int(input(f"Digite o numero de missoes: "))
gastos_fixos = (50, 25, 10)

calcular_combustivel(missoes, *gastos_fixos)
