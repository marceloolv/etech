# Definindo uma vareavel
# idade = 20
# if idade >= 18:
#     codigo executado se a condicao for verdadeira
#    print("Você é maior de idade"
# elif 13 <= idade < 18:
#     codigo executado se o primeiro if for falso
#    print("Você é adolescente")
# else:
#    # codigo executado se todos as condições anteriores forem falsas
#    print("você é menor de idade")


# exemplos com multiplas condições e operadores lógicos

# numero = 10
# if numero > 0 and numero % 2 == 0:
#     print("O numero é positivo e par")
# elif numero > 0 and numero % 2 != 0:
#     print("O númeor é positivo e impar")
# else:
#     print("O numero é zero ou negativo")


# exemplo de estrutura aninhada
idade = 20
tem_CNH = True

if idade >= 18:
    if tem_CNH:
        print("Você pode dirigir")
    else:
        print("Você não pode dirigir")
else:
    print("Você não tem idade para dirigir")





