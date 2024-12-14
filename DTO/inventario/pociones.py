
class Pocion:
    __nombre = ""
    __tipo = ""
    __nivel = 0
    __curacion = 0
    __num_uso = 0

    def __init__(self, nombre, tipo, nivel, curacion, num_uso):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__nivel = nivel
        self.__curacion = curacion
        self.__num_uso = num_uso

    def __str__(self):
        print(f"Nombre de la poción: {self.__nombre} \nTipo: {self.__tipo} \nNivel: {self.__nivel} \nCuración: {self.__curacion} \nCantidad de usos: {self.__num_uso}")

pocion_pequeña = Pocion("Pocion pequeña", "Poción", 1, 30, 1)
pocion_pequeña.__str__()
print("-"*30)
pocion_mediana = Pocion("Pocion mediana", "Poción", 2, 50, 2)
pocion_mediana.__str__()
print("-"*30)
pocion_grande = Pocion("Pocion grande", "Poción", 3, 80, 3)
pocion_grande.__str__()