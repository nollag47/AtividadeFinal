import copy
from picareta import picareta

class Picareta_de_Diamante(picareta):
    def __init__(self, nome,durabilidade,velocidade):
        self.ferramenta = "Picareta de Diamante"

    def getstatus(self):
        return f"Ferramenta: {self.ferramenta}, Nome: {self.nome}, Durabilidade:{self.durabilidade}, Velocidade: {self.velocidade}"

    def clone(self):
        return copy.deepcopy(self)
