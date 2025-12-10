class Estrela:
    tipo_corpo = "Corpo Celeste"
    total_estrelas_catalogadas = 0
    def __init__(self, nome, massa):
        self.nome = nome
        self.massa = massa
        self.em_atividade = True
        Estrela.total_estrelas_catalogadas += 1

    def mostra_atributos(self):
        print(f"Nome: {self.nome} | Massa: {self.massa} | Em atividade: {self.em_atividade} | Tipo de corpo: {self.tipo_corpo}")
        print("-"*85)


estrela_a = Estrela("Alpha Centauri", 1.1)
estrela_b = Estrela("Sirius", 2.0)

print("-"*85)
print(f'{">>>  E S T R E L A S  <<<":=^85}')
print("-"*85)

estrela_a.mostra_atributos()
estrela_b.mostra_atributos()

print(f"Estrelas catalogadas: {Estrela.total_estrelas_catalogadas:}")
print("-"*85)