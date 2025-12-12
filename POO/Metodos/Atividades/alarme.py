class Alarme:
    def __init__(self, senha,):
        self.senha = senha
        self.armado = False
        self.disparado = False

    def armar(self,senha_tentativa):
        if senha_tentativa == self.senha:
            self.armado = True
            print(f"Senha correta ✅. Alarme Armado!")
        else:
            print(f"A senha {senha_tentativa} está errada ❌, Alarme continua desarmado. Tente novamente!")

    def disparar(self):
        if self.armado == True:
            self.disparado = True
            print(f"ALARME ATIVADO! POLICIA CHAMADA!!! 🚨🚨🚨 ")

    def desarmar(self, senha_tentativa):
        if senha_tentativa == self.senha:
            self.armado = False
            self.disparado = False
            print(f"Senha correta ✅. Alarme Desarmado !!!")
        else:
            print(f"A senha {senha_tentativa} está errada ❌, A poicia esta chegando 🚨🚨🚨, tente novamente!")

alarme_a = Alarme(1234)

alarme_a.armar(5645)
alarme_a.armar(1234)
alarme_a.disparar()
alarme_a.desarmar(8956)
alarme_a.desarmar(1234)
