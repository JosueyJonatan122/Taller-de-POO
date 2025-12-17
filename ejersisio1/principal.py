from hija1 import BotellaPlastica
from hija2 import BotellaVidrio
from basededatos import BaseDatos

# Crear la base de datos
bd = BaseDatos()

# Crear objetos
botella1 = BotellaPlastica("Plástico", "puntos", "rosca", True)
botella2 = BotellaVidrio("Vidrio", "lineas", "corcho", "grueso")

# Agregar botellas
bd.agregar_botella(botella1)
bd.agregar_botella(botella2)

# Mostrar información
bd.mostrar_botellas()
