class Pagamento:
    def __init__(self, valor):
        self.valor = valor

    def calcular_valor(self):
        #garante que o piliformismo aconteça
        return self.valor

class PagamentoCartao(Pagamento):
    def __init__(self, valor, taxa):
        # chama o  etodo contrutor da classe mae
        super().__init__(valor)
        self.__taxa = taxa

    def calcular_valor(self):

        return self.valor + (self.valor * self.__taxa / 100)

class PagamentoPix(Pagamento):
    def __init__(self, valor, desconto):
        super().__init__(valor)

        self.__desconto = desconto

    def calcular_valor(self):

        return self.valor - (self.valor * self.__desconto / 100)

class PagamentoBoleto(Pagamento):
    def __init__(self, valor, taxa_fixa ):
        super().__init__(valor)
        self.__taxa_fixa = taxa_fixa

    def calcular_valor(self):
        return self.valor + self.__taxa_fixa

# lista que ira armazenar todos os pagamentos criados

pagamentos = []

quantidade = int(input("Quantos pagamentos deseja processar? "))

#Laço para criar varios pagamentos

for i in range(quantidade):
    print("\n1 - Cartão")
    print("2 - Pix")
    print("3 - Boleto")

    tipo = int(input("Escolha a forma de pagamento: "))

    valor = float(input("Digite o valor do boleto de pagamento: "))

    if tipo == 1:
        taxa = float(input("Digite a taxa do cartao: "))
        pagamento = PagamentoCartao(valor, taxa)
    elif tipo == 2:
        desconto = float(input("Digite o desconto do Pix: "))
        pagamento = PagamentoPix(valor, desconto)
    elif tipo == 3:
        taxa_fixa = float(input("Digite a taxa fixa do boleto: "))
        pagamento = PagamentoBoleto(valor, taxa_fixa)

    pagamentos.append(pagamento)

total_geral = 0   #vareavel para somar todos os pagamento

for pagamento in pagamentos:
    valor_final = pagamento.calcular_valor()

    print(f"Valor final: {valor_final}")
    total_geral += valor_final
print(f"\nTotal processado: {total_geral}")






