from hija1 import Mamifero
from hija2 import Ave
from basededatos import BaseDatos

# Crear base de datos
bd = BaseDatos()

# Crear objetos
mamifero1 = Mamifero("Perro", 5, "Casa", "Corto")
mamifero2 = Mamifero("Gato", 3, "Apartamento", "Largo")
ave1 = Ave("Loro", 2, "Selva", "Verde")

# Agregar a la lista
bd.agregar_animal(mamifero1)
bd.agregar_animal(mamifero2)
bd.agregar_animal(ave1)

# Mostrar datos
bd.mostrar_animales()
