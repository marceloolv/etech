class ContadorDeObjetos:
    #Atributo de classe:
    total_objetos = 0

    def __init__(self, nome):
        self.nome = nome #Atributo de instancia

        #Modifica o atributo de Classe a cada nova instancia
        ContadorDeObjetos.total_objetos += 1

    def exibir_contagem(self):
        print(f"Objeto {self.nome} criado. Total geral: "
            f"{ContadorDeObjetos.total_objetos}")

obj1 = ContadorDeObjetos("Item A")
obj1.exibir_contagem()
#Saida: Objeto Item A criado. Total geral: 1

obj2 = ContadorDeObjetos("Item B")
obj2.exibir_contagem()
#Saida: Objeto Item B criado. Total geral: 2

# obj1 e obj2 compartilham o mesmo contador!!!!