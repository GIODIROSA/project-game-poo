from raza import Raza
import random

class Elfo(Raza):
    def __init__(self, nombre):
        super().__init__(nombre, vida_base=270, vida=270, esquive=40, raza="Elfo")

    def set_nivel(self, nivel):
        if 1 <= nivel <= 3:
            super().set_nivel(nivel)
            if nivel == 2:
                self.actualizar_vida_base(400)
                self.actualizar_esquive(45)
                self.__inventario.inv_restaurar_pocion()
            elif nivel == 3:
                self.actualizar_vida_base(550)
                self.actualizar_esquive(50)
                self.__inventario.inv_restaurar_pocion()

    
    def actualizar_esquive(self, nuevo_esquive):
        self.__esquive = nuevo_esquive
    

    def atacar(self):
        arma = self.get_arma_equipada()
        #Habilidad del "Elfo", si tiene un arco equipado, hace 20% mas de daño / los arcos pegan 2 veces
        if arma.get_tipo() == "Arco":
            danho_ataque = (arma.get_danho() + (arma.get_danho() * 0.20)) * 2
            return danho_ataque
        else:
            danho_ataque = self.__arma_equipada.get_danho()
            return danho_ataque
        
    def esquivar(self):
        probabilidad_esquive = self.__esquive
        numero_aleatorio = random.uniform(0, 100)# Genera un número entre 0 y 100
        if numero_aleatorio <= probabilidad_esquive:
            print(f"{self.__nombre} esquivó el ataque.")
            return True  # Esquiva el ataque
        else:
            print(f"{self.__nombre} no pudo esquivar el ataque.")
            return False  # No esquiva el ataque