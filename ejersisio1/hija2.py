from padre import Botella

class BotellaVidrio(Botella):
    def __init__(self, material, grabados, tapa, grosor):
        super().__init__(material, grabados, tapa)
        self.grosor = grosor

    def mostrar_grosor(self):
        print(f"El grosor del vidrio es: {self.grosor}")
