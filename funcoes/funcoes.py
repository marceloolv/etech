
def mensagem():
    print("Olá, mundo!")

mensagem()


# passando valores

def saudacao(nome):
    print(f"Olá, {nome}")

saudacao("João")

# ele retorna um valor usando uma palavra chamada "return"

def soma (a, b):
    return a+b

resultado = soma(5,4)
print(resultado)


# função permite retornar multiplus valores usando tupla

def dividir(a, b):
    quociente = a // b
    resto = a % b
    return quociente, resto

q, r = dividir(10, 3)
print(f"quociente: {q} e o resto {r}")

# *args

def soma(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado

print(soma(1,2,3,4))
print(soma(10,20))

#exemplos com args
def lista_convidados(formatura, *args):
    print(f"Evento: {formatura}")

    if args: #verifica se a tupla args não esta vazia
        print("Convidados:")
        for nome in args:
            print(f"- {nome}")
    else:
        print("Nenhum convidado resgistrado!")

lista_convidados("Reunião de equipe", "Marcos", "Alice", "João", "Sofia")


def criar_etiqueta_produto( nome_produto, *args):
    print("\nEtiqueta do Produto:")
    print(nome_produto)
    if args:
        for caract in args:
            print(f"- {caract}")
    else:
        print("não há caracteristicas adicionais!")

criar_etiqueta_produto("Carro", "Pneus", "motor", "bancos", "Alarme")





