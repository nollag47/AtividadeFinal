from abc import ABC, abstractmethod
class picareta(ABC):
    def __init__(self,nome,durabilidade,velocidade):
        self.nome = nome
        self.durabilidade = durabilidade
        self.velocidade = velocidade
    def getstatus(self):
        return f"Nome: {self.nome}, Durabilidade:{self.durabilidade}, Velocidade: {self.velocidade}"
        @abstractmethod
        def clone(self):
            pass
        
