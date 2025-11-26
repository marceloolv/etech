inteiro = 10
decimal = 10.5
complexo = 3 + 4j

print(inteiro, decimal, complexo)
print(f"Tipos:{type(inteiro)}, {type(decimal)}, {type(complexo)}")

#texto
Texto = "olá, Miundo!"
print(Texto)
print(f"Tipo:{type(Texto)}")

# boleanos
verdadeiro = True
falso = False
print(verdadeiro, falso)
print(f"Tipos:{type(verdadeiro)}, {type(falso)}")

# Coleções
lista = [1, 2, 3]   # mutável
tupla = (1, 2, 3)   # imutável
dicionario = {"nome": "Marcos"}   # dict (dicionario)
conjunto = {1, 2, 3}   #set (conjuntos)
print(lista, tupla, dicionario, conjunto)
print(f"Tipos: {type(lista)}, {type(tupla)}, {type(dicionario)}, {type(conjunto)}")