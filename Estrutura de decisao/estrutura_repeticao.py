# for

# INTERANDO SOBRE UMA LISTA

# frutas = ["maça","banana","cereja"]
#
# for fruta in frutas:
#     print(fruta)



# INTERANDO 'range' PARA REPETIR UM BLOCO DE CODIGO 5 VEZES

# for i in range(5):
#     print("interacao: ", i)


# O enumerate() é uma função útil em Python que permite iterar
# sobre uma sequência, como uma lista ou uma string, ao mesmo
# tempo em que mantém um contador automático. Essa função
# retorna pares contendo o índice (ou contador) e o valor
# correspondente da sequência.

frutas = ["maça","banana","cereja"]
for indice, fruta in enumerate(frutas):
    print(f"Fruta {indice}: {fruta}")