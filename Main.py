# from pagamento import Pagamento
#
# p = Pagamento(100)
# print(p.calcular())

# from POO.Encapsulamento.ContaBancaria import Conta
#
# conta = Conta()
#
# print(conta.get_saldo())
#
# conta.depositar(500)
#
# conta.sacar(200)
#
# #verificar novamente o saldo da conta via GETTER
# print(conta.get_saldo())
#
# print(f"saldo usando o getter R$ {conta.get_saldo()}")
#


# TRATAMENTO DE EXCESSOES
from Operacoes import dividir

while True:
    try:
        x = int(input("Digite o primeiro numero: "))
        y = int(input("Digite o segundo numero : "))
        print(dividir(x,y))
        break
    except ValueError:
        print("Erro: Digite um numero")
    except ZeroDivisionError:
        print(("Erro: não é possivel dividir por zero"))



