from inventario.armas import *
from inventario.escudos import *

class Raza:
    __nombre = ""
    __vida_base = 0
    __vida = 0
    __esquive = 0
    __raza = ""
    __nivel = 1
    __arma_equipada = None
    __escudo_equipado = None

    def __init__(self, nombre, vida_base, vida, esquive, raza, nivel=1):
        self.__nombre = nombre
        self.__vida_base = vida_base  # Vida máxima
        self.__vida = vida  # Vida actual
        self.__esquive = esquive
        self.__raza = raza
        self.__nivel = nivel


    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_vida_base(self):
        return self.__vida_base

    def get_vida(self):
        return self.__vida

    def get_esquive(self):
        return self.__esquive

    def get_raza(self):
        return self.__raza

    def get_nivel(self):
        return self.__nivel

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_vida(self, vida):
        self.__vida = vida

    def set_esquive(self, esquive):
        self.__esquive = esquive

    def set_raza(self, raza):
        self.__raza = raza

    def set_nivel(self, nivel):
        if 1 <= nivel <= 3:
            self.__nivel = nivel

    # Modificar vida cuando te atacan
    def modificar_vida(self, cantidad):
        self.__vida -= cantidad
        if self.__vida <= 0:
            self.__vida = 0  # No permitir que la vida sea negativa
            print(f"{self.get_nombre()} Estas muerto: {self.__vida} puntos de vida.")
        print(f"{self.get_nombre()}, te han hecho {cantidad} puntos de daño, te quedan {self.__vida} puntos de vida.")

    #vALIDA LA OPCION QUE SOLO SEA "INT" Y ENTRE 1 A 3
    def validar_opcion(self, opcion):
        while True:
            try:
                opcion = int(input("Ingrese su opcion (1, 2, 3): "))
                if opcion in [1, 2, 3]:
                    return opcion
                else:
                    print(f" -{opcion}- no es valido, intentelo nuevamente ")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número (1, 2 o 3).")

    # Método para actualizar la vida base al subir de nivel
    def actualizar_vida_base(self, nueva_vida_base):
        self.__vida_base, self.__vida = nueva_vida_base, nueva_vida_base
        if self.__vida > self.__vida_base:
            self.__vida = self.__vida_base  # Ajustar la vida actual si excede la base


    # Usar poción (sin bonificación por defecto)
    def usar_pocion(self):
        # Bonificación según nivel
        porcentaje = {1: 0.20, 2: 0.30, 3: 0.40}[self.get_nivel()]
        curacion = (self.__vida * porcentaje)
        #En el caso de que la pocion exeda el maximo de la vida, solo se recupera la vida maxima
        if curacion > self.__vida_base - self.__vida:
            self.__vida = self.__vida_base
            print(f"{self.get_nombre()}, usaste una poción y recuperaste toda tu vida")
        else:
            self.__vida += curacion
            print(f"{self.get_nombre()}, usaste una poción y recuperaste {curacion} puntos de vida. Te quedan {self.__vida} puntos de vida")

    #Se equipa un arma, se da la opcion de elegir
    def equipar_arma(self):
        """Equipa un arma a la raza."""
        print(f"""
              Eliga una de las siguientes armas para equipar:\n
              1.-Nombre: Escalibur, Tipo: Espada, Nivel: 1, Daño: 40, Numero de golpes: 1)
              2.-Nombre: Molag'Mal, Tipo: Hacha, Nivel: 1, Daño: 40, Numero de golpes: 1)
              3.-Nombre: Arco de Ebano, Tipo: Arco, Nivel: 1, Daño: 20, Numero de golpes: 2)
              """)
        opcion = self.validar_opcion("")
        if opcion == 1:
            self.__arma_equipada = espada
            print(f"{self.__nombre} se ha equipado el arma: {self.__arma_equipada.get_nombre()}")  
        elif opcion == 2:
            self.__arma_equipada = hacha
            print(f"{self.__nombre} se ha equipado el arma: {self.__arma_equipada.get_nombre()}")
        elif opcion == 3:
            self.__arma_equipada = arco
            print(f"{self.__nombre} se ha equipado el arma: {self.__arma_equipada.get_nombre()}")
  


    def atacar(self):
        pass


                



