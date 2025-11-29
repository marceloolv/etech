
# for i in range(1, 11):
#     print(f"Contagem: ", i)

# =================================================

# cores = ["azul","verde","amarelo","vermelho"]
# for cor in cores:
#     print(cor)
#
#==========================================

# dinheiro = 50
# while dinheiro >= 0:
#     print(f"Você ainte tem: {dinheiro},")
#     dinheiro -= 10

# ==========================================

# for i in range(1, 21):
#     if i == 17:
#         break
#     if i % 3 == 0:
#         continue # Se for divisivel por 3, volta ao inicio
#     else:
#         print(f"Numero atual: {i}")
#
# # ou
#
# for i in range(1, 21):
#     if i % 3 == 0:
#         continue # Se for divisivel por 3, volta ao inicio
#     if i == 17:
#         print(f"Chegamos .parando o laço")
#         break
#     print(f"Numero atual: {i}")
#
#=======================================================

# # CRIANDO UMA LISTA DE NUMEROS
#
# numeros = [1,2,3,4,5]
# print(numeros)
#
# mistos = [1, "ola", 3.14, True]
# print(mistos)
#
# lista_vazia = list()
# print(lista_vazia)
#
# # CRIANDO UMA LISTA A PARTIR DE UMA SEQUENCIA
#
#
# # CRIANDO UMA LISTA A PARTIR DE UMA STRING
# lista_caracteres = list("Python")
# print(lista_caracteres)
#
#
# #criando uma lista a partir de uma regra
# lista_negra = list(range(5))
#
# # append() --> adiciona um elemento no final da lista
#
# # supondo que 'numeros' é [1,2,3,4,5]
# numeros.append(6)
# print(numeros)
#
# # remove()  -->  remove a ocorrência de um valor específico
# numeros.remove(3)
#
# #pop()
# # remove e retorne o elemento em um posição especifica
# ultimo = numeros.pop()
# print(ultimo)
# print(numeros)
#
# #index()
# # retorna o indice da primeira ocorrencia
# posicao = numeros.index(1)
# print(posicao)
#



# cordenadas = (10.5, 20.3)
# cordenadas.append(30)
# print(cordenadas)
# print("AttributeError: 'tuple' object has no attribute 'append'")

# registro_aulas = ("Python", "SQL", "Java", "Python", "Web", "SQL")
#
# # 1 - Conte as ocorrencias de "Python"
# contagem_python = registro_aulas.count("Python")
# print(contagem_python)
#
# # 2 - Encontre o Indice de "SQL"
# indice_sql = registro_aulas.index("SQL")
# print(indice_sql)

registro1 = ("Ana", 28, "São Paulo")
registro2 = ("Pedro", 35, "Rio de Janeiro")

registro = []
registro = [registro1, registro2]
print(registro)

registro3 = ["Carla", 22, "Recife" ]

registro.append(registro3)
print (registro)
# indice_pedro = registro.index("Pedro")
# print (indice_pedro)


