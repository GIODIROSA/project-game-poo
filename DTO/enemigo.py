from humano import Humano
from orco import Orco
from elfo import Elfo
from enano import Enano
import random

enem_humano_lvl_1 = Humano("Aldric Valheir")
enem_humano_lvl_1.arma_aleatoria()
enem_humano_lvl_2 = Humano("Cedric Leostrand")
enem_humano_lvl_2.set_nivel(2)
enem_humano_lvl_2.arma_aleatoria()
enem_humano_lvl_3 = Humano("Evelynn Crowne")
enem_humano_lvl_3.set_nivel(3)
enem_humano_lvl_3.arma_aleatoria()



enem_orco_lvl_1 = Orco("Grommak Sangredura")
enem_orco_lvl_1.arma_aleatoria()
enem_orco_lvl_2 = Orco("Zugar el Implacable")
enem_orco_lvl_2.set_nivel(2)
enem_orco_lvl_2.arma_aleatoria()
enem_orco_lvl_3 = Orco("Krag'gol Rompecráneos")
enem_orco_lvl_3.set_nivel(3)
enem_orco_lvl_3.arma_aleatoria()


enem_elfo_lvl_1 = Elfo("Lirael Estrella Plateada")
enem_elfo_lvl_1.arma_aleatoria()
enem_elfo_lvl_2 = Elfo("Thaelor Lunargéntea")
enem_elfo_lvl_2.set_nivel(2)
enem_elfo_lvl_2.arma_aleatoria()
enem_elfo_lvl_3 = Elfo("Aeronil Vientosusurro")
enem_elfo_lvl_3.set_nivel(3)
enem_elfo_lvl_3.arma_aleatoria()

enem_enano_lvl_1 = Enano("Thorgar Hierrofuerte")
enem_enano_lvl_1.arma_aleatoria()
enem_enano_lvl_2 = Enano("Bofrik Barbalarga")
enem_enano_lvl_2.set_nivel(2)
enem_enano_lvl_2.arma_aleatoria()
enem_enano_lvl_3 = Enano("Durnik Hojabrillante")
enem_enano_lvl_3.set_nivel(3)
enem_enano_lvl_3.arma_aleatoria()


lista_enemigos_lvl_1 = [enem_humano_lvl_1, enem_orco_lvl_1, enem_elfo_lvl_1, enem_enano_lvl_1]
lista_enemigos_lvl_2 = [enem_humano_lvl_2, enem_orco_lvl_2, enem_elfo_lvl_2, enem_enano_lvl_2]
lista_enemigos_lvl_3 = [enem_humano_lvl_3, enem_orco_lvl_3, enem_elfo_lvl_3, enem_enano_lvl_3]


enemigo_actual_lvl_1 = random.choice(lista_enemigos_lvl_1)
enemigo_actual_lvl_2 = random.choice(lista_enemigos_lvl_2)
enemigo_actual_lvl_3 = random.choice(lista_enemigos_lvl_3)

# print(f"Tu enemigo actual es: {enemigo_actual_lvl_1}")
# print(f"Tu enemigo actual es: {enemigo_actual_lvl_2}")
# print(f"Tu enemigo actual es: {enemigo_actual_lvl_3}")
