from .raza import Raza
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
            elif nivel == 3:
                self.actualizar_vida_base(550)
                self.actualizar_esquive(50)
    
    def actualizar_esquive(self, nuevo_esquive):
        self.__esquive = nuevo_esquive
    

    def atacar(self):
        arma = self.get_arma_equipada()  # Usar el método de la clase base para obtener el arma equipada
        if arma.get_tipo() == "Arco":
            # Habilidad del elfo: si tiene una hacha equipada, hace 20% más de daño
            danho_ataque = (arma.get_danho() + (arma.get_danho() * 0.20))
        else:
            danho_ataque = arma.get_danho()
        return danho_ataque
        
    def esquivar(self):
        probabilidad_esquive = self.get_esquive()
        numero_aleatorio = random.uniform(0, 100)# Genera un número entre 0 y 100
        if numero_aleatorio <= probabilidad_esquive:
            print(f"{self.get_nombre()} esquivó el ataque.")
            return True  # Esquiva el ataque
        else:
            print(f"{self.get_nombre()} no pudo esquivar el ataque.")
            return False  # No esquiva el ataque
        
