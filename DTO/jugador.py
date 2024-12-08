
from personaje import Personaje

class Jugador(Personaje):
    __raza = ""
    __experiencia = 0
    
    def __init__(self, raza, experiencia, nombre, nivel, salud):
        self.__raza = raza
        self.__experiencia = experiencia
        self.setNombre(nombre)
        self.setNivel(nivel)
        self.setSalud(salud)


    def funcionalidad(self):
        pass
    def disparar(self):
        pass
    def cargar(self):
        pass
