class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    # Metodo que troca o status da tarefa para conclida (True)
    def marcar_concluida(self, concluida = True):
        self.concluida = concluida
        print(f"A tarefa {self.descricao} esta concluída")


tarefa_1 = Tarefa("Varrer")
tarefa_1.marcar_concluida()

