class Produto:
    def __init__(self, preco):
        self.__preco = preco

    def set_preco(self, valor):
        if valor > 0:
            self.__preco = valor
            print(f"Preço alterado para: {valor}")
        else:
            print(f"Preço Invalido! Não pode ser negativo ou zero")

    def get_preco(self):
        return self.__preco

#uso
produto = Produto(100)

# Tentando alterar o preço para um valor negativo
produto.set_preco(200)

#mostrar o preço usando o getter
print("Preço atual", produto.get_preco())

