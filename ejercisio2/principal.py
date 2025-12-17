from hija1 import Carro
from hija2 import Camion
from basededatos import BaseDatos

# Crear base de datos
bd = BaseDatos()

# Crear objetos
carro1 = Carro("BMW", "Negro", "Gasolina", 2)
carro2 = Carro("Mazda", "Rojo", "Gasolina", 4)
camion1 = Camion("Camión", "Blanco", "Diésel", "10 toneladas")

# Agregar a la lista
bd.agregar_vehiculo(carro1)
bd.agregar_vehiculo(carro2)
bd.agregar_vehiculo(camion1)

# Mostrar datos
bd.mostrar_vehiculos()
