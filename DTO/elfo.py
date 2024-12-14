from raza import Raza

class Elfo(Raza):
    def __init__(self, nombre):
        super().__init__(nombre, vida_base=270, vida=270, esquive=40, raza="Elfo")

    def set_nivel(self, nivel):
        if 1 <= nivel <= 3:
            super().set_nivel(nivel)
            if nivel == 2:
                self.actualizar_vida_base(400)
            elif nivel == 3:
                self.actualizar_vida_base(550)
    
    def usar_pocion(self):
        # Bonificación según nivel
        porcentaje = {1: 0.20, 2: 0.30, 3: 0.40}[self.get_nivel()]
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