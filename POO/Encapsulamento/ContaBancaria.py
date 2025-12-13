class Conta:
    def __init__(self):
        #Atributo privado: só pode ser acessado dentro da classe
        self.__saldo = 0

    # GETTER -> UTILIZADO PARA LER UM ATRIBUTO PRIVADO
    # permite acessar o valor sem alterar diretamente.
    def get_saldo(self):
        return self.__saldo

    # SETTER -> ALTERAR O ATRIBUTO PRIVADO, mas de forma controlada
    # Aqui ele funciona como um SETTER, mas com o nome "depositar"
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

# Exemplo de uso

conta = Conta()

print(conta.get_saldo())

conta.depositar(500)

conta.sacar(200)

#verificar novamente o saldo da conta via GETTER
print(conta.get_saldo())

print(f"saldo usando o getter R$ {conta.get_saldo()}")