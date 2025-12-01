# ESTRUTURA DE REPETIÇÃO
# 1 - Dada uma lista de valores inteiros criar um programa para somar
# os valores pares e valores ímpares

import random
inteiros = []
soma_par = 0
soma_impar = 0
for i in range(1, 11):
    inteiros.append(random.randint(1, 10))
for numero in inteiros:
    if numero % 2 == 0:
        soma_par += numero
    else:
        soma_impar += numero
print(f"Valores : {inteiros}")
print(f"A soma dos valores pares é..: {soma_par}")
print(f"A soma dos valores impares é: {soma_impar}")