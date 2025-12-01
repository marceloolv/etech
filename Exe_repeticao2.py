# 2- Dada uma palavra criar uma programa para retornar a
# quantidade de vogais e quantidade de consoantes

palavra = input("escreva uma palavra: ").upper()
qtd_vogais = 0
qtd_consoantes = 0
for letra in palavra:
    if (letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U" or letra == "Á" or
    letra == "É" or letra == "Í" or letra == "Ó" or letra == "Ú" or letra == "Â" or letra == "Ê" or
    letra == "Ô" or letra == "À"):
        qtd_vogais += 1
    else:
        if letra != "-":
            qtd_consoantes += 1
print(f"Na palavra {palavra}, existem {qtd_vogais} vogais.")
print(f"Na palavra {palavra}, existem {qtd_consoantes} consoantes.")


