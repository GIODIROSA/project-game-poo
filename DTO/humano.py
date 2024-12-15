from raza import Raza
from inventario.pociones import pociones

class Humano(Raza):
    def __init__(self, nombre):
        super().__init__(nombre, vida_base=300, vida=300, esquive=20, raza="Humano")

    def set_nivel(self, nivel):
        if 1 <= nivel <= 3:
            super().set_nivel(nivel)
            if nivel == 2:
                self.actualizar_vida_base(450)
                self.__inventario.inv_restaurar_pocion()
            elif nivel == 3:
                self.actualizar_vida_base(580)
                self.__inventario.inv_restaurar_pocion()

    

    def usar_pocion(self):
        # Bonificación según nivel
        if self.__vida < self.__vida_base:
            # porcentaje = pociones.get_nivel()
            if self.__pociones == 1 or self.__pociones == 2:
                porcentaje = porcentaje[self.get_nivel()]
                curacion = (self.__vida_base * porcentaje)
                #En el caso de que la pocion exeda el maximo de la vida, solo se recupera la vida maxima
                if curacion > self.__vida_base - self.__vida:
                    self.__vida = self.__vida_base
                    print(f"{self.get_nombre()}, usaste una poción y recuperaste toda tu vida")
                    print(f"Te queda {self.__pociones} pocion")

                else:
                    self.__vida += curacion
                    print(f"{self.get_nombre()}, usaste una poción y recuperaste {curacion} puntos de vida. Te quedan {self.__vida} puntos de vida")
                    print(f"Te queda {self.__pociones} pocion")
            else:
                print(f"No te quedan pociones")
        else:
            print(f"Tienes tu vida completa, no puedes usar pociones")
            
    def atacar(self):
        arma = self.get_arma_equipada()
        #Habilidad del "Humano", hace 10% mas de daño con cualquier arma
        danho_ataque = (arma.get_danho() + (arma.get_danho() * 0.10))
        return danho_ataque




######PRUEBA DE FUNCIONAMIENTO#####
# # Crear personaje
humano = Humano("Aragorn")
print(f"{humano.get_nombre()} (Nivel {humano.get_nivel()}): Vida Base {humano.get_vida_base()}, Vida Actual {humano.get_vida()}")
humano.elegir_arma()
# # # Modificar vida
humano.modificar_vida(100)
humano.usar_pocion()
# # # Cambiar nivel
humano.set_nivel(2)
print(f"{humano.get_nombre()} (Nivel {humano.get_nivel()}): Vida Base {humano.get_vida_base()}, Vida Actual {humano.get_vida()}")
humano.usar_pocion()
humano.modificar_vida(200)
# # Usar poción (Opcional si tienes lógica de curación)