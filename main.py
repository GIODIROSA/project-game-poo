
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


import menu
import historia

def iniciar_juego():
    # Mostrar la historia al inicio
    historia.imprimir_historia()
    
    # Mostrar el menú principal
    menu.menu_principal()

if __name__ == "__main__":
    iniciar_juego()
