from vehiculo import Vehiculo

class Carro(Vehiculo):
    def __init__(self, modelo, color, combustible, puertas):
        super().__init__(modelo, color, combustible)
        self.puertas = puertas

    def mostrar_puertas(self):
        print("Número de puertas:", self.puertas)
