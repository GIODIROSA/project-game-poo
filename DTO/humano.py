from raza import Raza

class Humano(Raza):
    def __init__(self, nombre):
        super().__init__(nombre, vida_base=300, vida=300, esquive=20, raza="Humano")

    def set_nivel(self, nivel):
        if 1 <= nivel <= 3:
            super().set_nivel(nivel)
            if nivel == 2:
                self.actualizar_vida_base(450)
            elif nivel == 3:
                self.actualizar_vida_base(580)
    
    def usar_pocion(self):
        # Bonificación según nivel
        porcentaje = {1: 0.27, 2: 0.44, 3: 0.61}[self.get_nivel()]
        vida_actual = self.get_vida()
        vida_base = self.get_vida_base()
        curacion = vida_base * porcentaje
        #En el caso de que la pocion exeda el maximo de la vida, solo se recupera la vida maxima
        if vida_actual + curacion > vida_base:
            self.set_vida(vida_base)
            print(f"{self.get_nombre()}, usaste una poción y recuperaste toda tu vida.")
        else:
            self.set_vida(vida_actual + curacion)
            print(f"{self.get_nombre()}, usaste una poción y recuperaste {curacion} puntos de vida. Te quedan {self.get_vida()} puntos de vida.")  




# ######PRUEBA DE FUNCIONAMIENTO#####
# # # Crear personaje
humano = Humano("Aragorn")
print(f"{humano.get_nombre()} (Nivel {humano.get_nivel()}): Vida Base {humano.get_vida_base()}, Vida Actual {humano.get_vida()}")

humano.equipar_arma()

# # # Modificar vida
humano.modificar_vida(100)

humano.usar_pocion()

# # # Cambiar nivel
humano.set_nivel(2)
print(f"{humano.get_nombre()} (Nivel {humano.get_nivel()}): Vida Base {humano.get_vida_base()}, Vida Actual {humano.get_vida()}")

humano.usar_pocion()

humano.modificar_vida(200)
# # # Usar poción (Opcional si tienes lógica de curación)