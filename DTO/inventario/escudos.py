
class Escudo:
    __nombre = ""
    __tipo = ""
    __nivel = ""
    __defensa = 0

    def __init__(self, nombre, tipo, nivel, defensa, ):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__nivel = nivel
        self.__defensa = defensa
    
    def __str__(self):
        print(f"Nombre del escudo: {self.__nombre} \nTipo: {self.__tipo} \nNivel: {self.__nivel} \nDefensa: {self.__defensa}")

escudo_pequeño = Escudo("Escudo pequeño", "Escudo", 1, 0.30)
# escudo_pequeño.__str__()
# print("-"*30)

escudo_mediano = Escudo("Escudo mediano", "Escudo", 2, 0.45)
# escudo_mediano.__str__()
# print("-"*30)

escudo_grande = Escudo("Escudo grande", "Escudo", 3, 0.60)
# escudo_grande.__str__()