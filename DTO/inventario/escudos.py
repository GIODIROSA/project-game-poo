
class Escudo:
    __nombre = ""
    __tipo = ""
    __nivel = ""
    __defensa = 0

    def __init__(self, nombre, tipo, nivel, defensa):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__nivel = nivel
        self.__defensa = defensa
    
    def __str__(self):
        print(f"Nombre del escudo: {self.__nombre}, Tipo: {self.__tipo}, Nivel: {self.__nivel}, Defensa: {self.__defensa}")

    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo

    def get_nivel(self):
        return self.__nivel

    def get_defensa(self):
        return self.__defensa

    def get_n_golpes(self):
        return self.__n_golpes

escudo_pequeño = Escudo("Escudo pequeño", "Escudo", 1, 30)
# escudo_pequeño.__str__()
# print("-"*30)

escudo_mediano = Escudo("Escudo mediano", "Escudo", 2, 45)
# escudo_mediano.__str__()
# print("-"*30)

escudo_grande = Escudo("Escudo grande", "Escudo", 3, 60)
# escudo_grande.__str__()