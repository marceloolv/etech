class Carro:
    roda = 4  # Atributo da classe

    def __init__(self, marca, modelo):
        self.marca = marca     #Atributo de instancia
        self.modelo = modelo   #Atributo de instancia


# Criando nossos objetos
carro_a = Carro("Ford", "Ford ka")
carro_b = Carro("BMW", "X1")

# Estamos acessando pelo Objeto (instância)
print(f"O {carro_a.modelo} tem {carro_a.roda} rodas.")
# Saida: O Ford ka tem 4 rodas.

print (f"Todo carro deve ter {Carro.roda} rodas.")
# Saida: Todo carro deve ter 4 rodas.

Carro.roda = 6
print(f"Novo valor {carro_a.roda}")