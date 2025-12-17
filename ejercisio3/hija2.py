from animal import Animal

class Ave(Animal):
    def __init__(self, nombre, edad, habitat, tipo_plumaje):
        super().__init__(nombre, edad, habitat)
        self.tipo_plumaje = tipo_plumaje

    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo de plumaje:", self.tipo_plumaje)
