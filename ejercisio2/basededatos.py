class BaseDatos:
    def __init__(self):
        self.lista_vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.lista_vehiculos.append(vehiculo)
        print("Vehículo agregado")

    def mostrar_vehiculos(self):
        print("Vehículos registrados:")
        for v in self.lista_vehiculos:
            v.mostrar_info()
            print("------------------")
