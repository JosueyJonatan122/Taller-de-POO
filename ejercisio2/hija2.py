from vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, modelo, color, combustible, carga):
        super().__init__(modelo, color, combustible)
        self.carga = carga

    def mostrar_carga(self):
        print("Capacidad de carga:", self.carga)
