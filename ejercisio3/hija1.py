from animal import Animal

class Mamifero(Animal):
    def __init__(self, nombre, edad, habitat, tipo_pelo):
        super().__init__(nombre, edad, habitat)
        self.tipo_pelo = tipo_pelo

    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo de pelo:", self.tipo_pelo)
