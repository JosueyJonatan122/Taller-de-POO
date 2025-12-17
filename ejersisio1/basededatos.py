class BaseDatos:
    def __init__(self):
        self.lista_botellas = []

    def agregar_botella(self, botella):
        self.lista_botellas.append(botella)
        print("Botella agregada a la base de datos")

    def mostrar_botellas(self):
        print("Contenido de la base de datos:")
        for botella in self.lista_botellas:
            botella.imprimir_info()
            print("-------------------")
