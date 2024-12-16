class Arma:
    __nombre = ""
    __tipo = ""
    __danho = 0
    __n_golpes = 1

    def __init__(self, nombre, tipo, danho, n_golpes):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__danho = danho
        self.__n_golpes = n_golpes
    
    def __str__(self):
        return (f"Nombre del arma: {self.__nombre}, Tipo: {self.__tipo}, Daño: {self.__danho}, Numero de golpes: {self.__n_golpes}")
    
    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo

    def get_danho(self):
        return self.__danho

    def get_n_golpes(self):
        return self.__n_golpes

espada = Arma("Escalibur", "Espada", 40, 1)
hacha = Arma("Molag'Mal", "Hacha", 40, 1)
arco = Arma("Arco de Ebano", "Arco",40, 1)


