class Pocion:
    __nombre = ""
    __tipo = ""
    __nivel = 0
    __cantidad = 0
    def __init__(self, nombre="Poción de Vida", tipo="Consumible", cantidad = 2):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__nivel = {1: 0.30, 2: 0.40, 3: 0.50}  # Nivel de la poción, que determina el porcentaje de curación
        self.__cantidad = cantidad

    def __str__(self):
        return (f"{self.__nombre}, Tipo: {self.__tipo}, Nivel: {self.__nivel}, Cantidad de pociones {self.__cantidad}")
        
        
    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo
    
    def get_nivel(self):
        return self.__nivel
    
    def get_cantidad(self):
        return self.__cantidad
    
    def restar_pocion(self):
        self.__cantidad -= 1

    def restaurar_pociones(self):
        self.__cantidad = 2
    
pociones = Pocion()


