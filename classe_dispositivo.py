class Dispositivo:
    rede_padrao = "Rede Domestica V.2"
    total_ativos = 0
    def __init__(self, id_serie, localizacao):
        self.id_serie = id_serie
        self.localizacao = localizacao
        self.status = "Desconectado"
        Dispositivo.total_ativos += 1

    def imprimi_dispositivos(self):
        print(f"Id_Série: {self.id_serie[0:10]:10} | Localização: {self.localizacao[0:12]:15} | Status: {self.status:12} | Rede padrão: {self.rede_padrao:18}")
        print("-" * 108)



lista_dispositivos = []
while True:
    id_serie =    input("Informe o id_série do dispositivo...: ")
    localizacao = input("Informe a licalização do dispositivo: ")
    lista_dispositivos.append([id_serie, localizacao])

    escolha = " "
    while escolha not in "SN":
        escolha = input("Continuar cadastrando? [S/N]").upper()
        if escolha not in "SN":
            print("resposta incorreta! tente novamente ")
    if escolha == "N":
        break

print(lista_dispositivos)
print("\n>>>  D I S P O S I T I V O S  <<<")
print("-" * 108)

for i in range(len(lista_dispositivos)):
    dispositivo_usuario = Dispositivo(lista_dispositivos[i][0], lista_dispositivos[i][1])
    dispositivo_usuario.imprimi_dispositivos()
print(f"Total de ativos >>> {Dispositivo.total_ativos}\n")

# uma outra forma do for para a mesma situação
# for i in lista_dispositivos:
#     dispositivo_usuario = Dispositivo(i[0], i[1])
#     dispositivo_usuario.imprimi_dispositivos()
# print(f"Total de ativos >>> {Dispositivo.total_ativos}\n")