import random

# Datos de los personajes
personajes = {
    "Orco": {"esquive": 0},    # 10% de probabilidad de esquivar
    "Elfo": {"esquive": 40},    # 30% de probabilidad de esquivar
    "Humano": {"esquive": 20},  # 20% de probabilidad de esquivar
    "Enano": {"esquive": 5}     # 5% de probabilidad de esquivar
}

def intentar_esquivar(nombre_personaje):
    probabilidad_esquive = personajes[nombre_personaje]["esquive"]
    numero_aleatorio = random.uniform(0, 100)  # Genera un número entre 0 y 100

    if numero_aleatorio <= probabilidad_esquive:
        print(f"{nombre_personaje} esquivó el ataque (Probabilidad: {probabilidad_esquive}%).")
        return True  # Esquiva el ataque
    else:
        print(f"{nombre_personaje} no pudo esquivar el ataque (Probabilidad: {probabilidad_esquive}%).")
        return False  # No esquiva el ataque

# Ejemplo de uso
intentar_esquivar("Elfo")  # Ver si el Elfo esquiva
intentar_esquivar("Orco")  # Ver si el Orco esquiva