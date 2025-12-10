# class Aeronave:
#     espaco_aereo = "Controlado"
#     total_aeronave = 0
#
#     def __init__(self, prefixo, companhia, altitude=0):
#         self.prefixo = prefixo
#         self.companhia = companhia
#         self.altitude = altitude
#         Aeronave.total_aeronave += 1
#
#     def mostra_aeronave_cadastradas(self):
#         print(f"Total de aeronaves cadastradas: {Aeronave.total_aeronave}")
#         print("-"*50)
#
#     def mostra_dados(self):
#         print(f"Prefixo: {self.prefixo},  Altitude: {self.altitude}")
#
#
# aero1 = Aeronave("PR-ABC", "GOL")
# aero1.mostra_dados()
# aero1.mostra_aeronave_cadastradas()
# aero2 = Aeronave("AM-123", "AZUL", 10)
# aero2.mostra_dados()
# aero2.mostra_aeronave_cadastradas()


#OU  metodo professor

class Aeronave:
    espaco_aereo = "Controlado"
    total_aeronave = 0

    def __init__(self, prefixo, companhia):
        self.prefixo = prefixo
        self.companhia = companhia
        self.altitude = 0
        Aeronave.total_aeronave += 1

    def mostra_aeronave_cadastradas(self):
        print(f"Total de aeronaves cadastradas: {Aeronave.total_aeronave}")
        print("-"*50)

    def mostra_dados(self):
        print(f"Prefixo: {self.prefixo},  Altitude: {self.altitude}")


aero1 = Aeronave("PR-ABC", "GOL")
aero1.mostra_dados()
aero1.mostra_aeronave_cadastradas()
aero2 = Aeronave("AM-123", "AZUL")
aero2.mostra_dados()
aero2.mostra_aeronave_cadastradas()
