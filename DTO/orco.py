from .raza import Raza
class Orco(Raza):
    def __init__(self, nombre):
        super().__init__(nombre, vida_base=350, vida=350, esquive=0, raza="Orco")

    def set_nivel(self, nivel):
        if 1 <= nivel <= 3:
            super().set_nivel(nivel)
            if nivel == 2:
                self.actualizar_vida_base(550)
            elif nivel == 3:
                self.actualizar_vida_base(700)


    def atacar(self):
        arma = self.get_arma_equipada()  # Usar el método de la clase base para obtener el arma equipada
        if arma.get_tipo() == "Hacha":
            # Habilidad del Orco: si tiene una hacha equipada, hace 40% más de daño
            danho_ataque = arma.get_danho() + (arma.get_danho() * 0.40)
        else:
            danho_ataque = arma.get_danho()
        return danho_ataque