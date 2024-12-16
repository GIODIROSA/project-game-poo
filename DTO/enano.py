from .raza import Raza

class Enano(Raza):
    def __init__(self, nombre):
        super().__init__(nombre, vida_base=330, vida=330, esquive=20, raza="Enano")

    def set_nivel(self, nivel):
        if 1 <= nivel <= 3:
            super().set_nivel(nivel)
            if nivel == 2:
                self.actualizar_vida_base(490)
            elif nivel == 3:
                self.actualizar_vida_base(600)

    def atacar(self):
        arma = self.get_arma_equipada()  # Usar el método de la clase base para obtener el arma equipada
        if arma.get_tipo() == "Hacha":
            # Habilidad del enano: si tiene una hacha equipada, hace 15% más de daño
            danho_ataque = arma.get_danho() + (arma.get_danho() * 0.15)
        else:
            danho_ataque = arma.get_danho()
        return danho_ataque
        
    def defender(self):
        defensa = self.get_escudo_equipado().get_defensa()+0.5
        return defensa
