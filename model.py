from abc import abstractmethod

class Model:
    @abstractmethod
    def berechnen(self, num:float):
        pass