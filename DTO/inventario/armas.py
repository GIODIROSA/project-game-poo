
class Arma:
    __nombre = ""
    __tipo = ""
    __nivel = ""
    __danho = 0
    __municion = 1

    def __init__(self, nombre, tipo, nivel, danho, municion):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__nivel = nivel
        self.__danho = danho
        self.__municion = municion
    
    def __str__(self):
        return (f"Nombre del arma: {self.__nombre} \n"
                f"Tipo: {self.__tipo} \n"
                f"Nivel: {self.__nivel} \n"
                f"Daño: {self.__danho} \n"
                f"Numero de golpes: {self.__municion}")
    
    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo

    def get_nivel(self):
        return self.__nivel

    def get_danho(self):
        return self.__danho

    def get_municion(self):
        return self.__municion

espada = Arma("Escalibur", "Espada", 1, 40, 1)
hacha = Arma("Molag'Mal", "Hacha", 1, 40, 1)
arco = Arma("Arco de Ebano", "Arco", 1, 20, 2)


