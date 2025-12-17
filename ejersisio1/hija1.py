from padre import Botella

class BotellaPlastica(Botella):
    def __init__(self, material, grabados, tapa, reciclable):
        super().__init__(material, grabados, tapa)
        self.reciclable = reciclable

    def mostrar_reciclaje(self):
        if self.reciclable:
            print("La botella es reciclable")
        else:
            print("La botella no es reciclable")
