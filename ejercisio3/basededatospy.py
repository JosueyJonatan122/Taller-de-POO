class BaseDatos:
    def __init__(self):
        self.lista_animales = []

    def agregar_animal(self, animal):
        self.lista_animales.append(animal)
        print("Animal agregado a la base de datos")

    def mostrar_animales(self):
        print("\nAnimales registrados:")
        for a in self.lista_animales:
            a.mostrar_info()
            print("-------------------")
