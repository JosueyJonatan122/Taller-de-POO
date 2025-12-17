class Botella:
    def __init__(self, material, grabados, tapa):
        self.material = material
        self.grabados = grabados
        self.tapa = tapa

    def mostrar_grabados(self):
        if self.grabados == "puntos":
            print("Grabados: ....")
        elif self.grabados == "lineas":
            print("Grabados: ||||")

    def cerrar_tapa(self):
        print(f"Tapa utilizada: {self.tapa}")

    def imprimir_info(self):
        print(f"Material: {self.material}")
        print(f"Grabados: {self.grabados}")
        print(f"Tapa: {self.tapa}")
