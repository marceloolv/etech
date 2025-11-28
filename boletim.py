print("="*40)
print(f'{"B O L E T I M":^40}')
print("="*40)

frequencia =  float(input("Informe a Frequência em porcentagem: "))
media_final = float(input("Informe a Média final..............: "))

if frequencia >= 75 and media_final >= 7:
    print("\nAluno Aprovado!")
elif frequencia < 75 or (frequencia >= 75 and media_final < 5):
    print("\nAluno esta Reprovado!")
elif frequencia >= 75 and 5.0 <= media_final <=6.9:
    print("\nAluno esta em Recuperação!")
