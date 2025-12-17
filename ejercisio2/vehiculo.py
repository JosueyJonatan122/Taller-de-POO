class Vehiculo:
    def __init__(self, modelo, color, combustible):
        self.modelo = modelo
        self.color = color
        self.combustible = combustible

    def arrancar(self):
        print("El vehículo ha arrancado")

    def apagar(self):
        print("El vehículo se ha apagado")

    def mostrar_info(self):
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Combustible:", self.combustible)
