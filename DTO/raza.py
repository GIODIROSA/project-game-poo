from inventario.armas import *
from inventario.escudos import *
from inventario.clase_inventario import inventario
from inventario.pociones import pociones
import random



class Raza:
    __nombre = ""
    __vida_base = 0
    __vida = 0
    __esquive = 0
    __raza = ""
    __nivel = 1
    __arma_equipada = None
    __escudo_equipado = None
    __inventario = None

    def __init__(self, nombre, vida_base, vida, esquive, raza, nivel=1):
        self.__nombre = nombre
        self.__vida_base = vida_base  # Vida máxima
        self.__vida = vida  # Vida actual
        self.__esquive = esquive
        self.__raza = raza
        self.__nivel = nivel
        self.__escudo_equipado = escudo_pequeño
        self.__inventario = inventario

    def __str__(self):
        return (f"{self.get_nombre()}, Raza: {self.__raza} (Nivel {self.get_nivel()}), Vida Actual {self.get_vida()}, Arma equipada: {self.__arma_equipada.get_tipo()}")

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_vida_base(self):
        return self.__vida_base

    def get_vida(self):
        return self.__vida

    def get_esquive(self):
        return self.__esquive

    def get_raza(self):
        return self.__raza

    def get_nivel(self):
        return self.__nivel
    
    def get_arma_equipada(self):
        return self.__arma_equipada
    
    def get_escudo_equipada(self):
        return self.__escudo_equipado
    
    # def get_inventario(self):
    #     return self.__inventario

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_vida(self, vida):
        self.__vida = vida

    def set_esquive(self, esquive):
        self.__esquive = esquive

    def set_raza(self, raza):
        self.__raza = raza

    def set_nivel(self, nivel):
        if 1 <= nivel <= 3:
            self.__nivel = nivel
    
    # Modificar vida cuando te atacan, entra como parametro el daño que le hacen al personaje
    def modificar_vida(self, cantidad):
        self.__vida -= cantidad
        if self.__vida <= 0:
            self.__vida = 0  # No permitir que la vida sea negativa
            print(f"{self.get_nombre()} Estas muerto: {self.__vida} puntos de vida.")
        print(f"{self.get_nombre()}, te han hecho {cantidad} puntos de daño, te quedan {self.__vida} puntos de vida.")

    #Se le ingresa como parametro un mensaje y una lista de opciones / La funcion elegir_arma() y abrir_inventario() la utilizan
    def raza_validar_opcion(self, mensaje, opciones):
        while True:
            try:
                opcion = int(input(f"{mensaje}"))
                if opcion in opciones:
                    return opcion
                else:
                    print(f" -{opcion}- no es valido, intentelo nuevamente. ")
            except ValueError:
                print("Entrada inválida. Por favor, intentelo nuevamente.")

    # Método para actualizar la vida base al subir de nivel, entra como parametro la nueva vida maxima del personaje desde la sub-clase correspondiente
    def actualizar_vida_base(self, nueva_vida_base):
        self.__vida_base, self.__vida = nueva_vida_base, nueva_vida_base
        if self.__vida > self.__vida_base:
            self.__vida = self.__vida_base  # Ajustar la vida actual si excede la base

    # #Llama a la funcion usar_pocion de la clase "pocion"
    # def usar_pocion(self):
    #     self.__inventario.__pociones.usar_pocion()

    #Se equipa un arma, se da la opcion de elegir al "JUGADOR"
    def elegir_arma(self):
        """Equipa un arma a la raza."""
        print(f"""
              Eliga una de las siguientes armas principales para equipar a tu personaje:\n
              1.-Nombre: Escalibur, Tipo: Espada, Nivel: 1, Daño: 40, Numero de golpes: 1)
              2.-Nombre: Molag'Mal, Tipo: Hacha, Nivel: 1, Daño: 40, Numero de golpes: 1)
              3.-Nombre: Arco de Ebano, Tipo: Arco, Nivel: 1, Daño: 20, Numero de golpes: 2)
              """)
        opcion = self.raza_validar_opcion("Eliga un arma: ", opciones = [1, 2, 3])
        if opcion == 1:
            self.__arma_equipada = espada
            print(f"{self.__nombre} se ha equipado el arma: {self.__arma_equipada.get_nombre()}")  
        elif opcion == 2:
            self.__arma_equipada = hacha
            print(f"{self.__nombre} se ha equipado el arma: {self.__arma_equipada.get_nombre()}")
        elif opcion == 3:
            self.__arma_equipada = arco
            print(f"{self.__nombre} se ha equipado el arma: {self.__arma_equipada.get_nombre()}")
        self.__inventario.agregar_objeto(self.__arma_equipada)
        
    def usar_pocion(self):
        # Bonificación según nivel
        if self.__vida < self.__vida_base:
            # porcentaje = pociones.get_nivel()
            if self.__pociones == 1 or self.__pociones == 2:
                porcentaje = {1: 0.20, 2: 0.30, 3: 0.40}[self.get_nivel()]
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

    #Funcion para equipar escudo
    # def elegir_escudo(self):
    #     self.__escudo_equipado = escudo_pequeño

    #Funcion encargada de equipar un arma aleatoria al enemigo
    def arma_aleatoria(self):
        armas = [espada, hacha, arco]
        self.__arma_equipada = random.choice(armas)

    #Funcion encargada de esquivar un golpe de manera aleatoria segun el % de esquive de cada personaje
    def esquivar(self):
        probabilidad_esquive = self.__esquive
        numero_aleatorio = random.uniform(0, 100)# Genera un número entre 0 y 100
        if numero_aleatorio <= probabilidad_esquive:
            print(f"{self.__nombre} esquivó el ataque.")
            return True  # Esquiva el ataque
        else:
            print(f"{self.__nombre} no pudo esquivar el ataque.")
            return False  # No esquiva el ataque

    #Obtiene el daño del arma equipada y retorna ese daño (Dependiendo del personaje, los daños aumentaran segun el arma equipada)
    def atacar(self):
        danho_ataque = self.__arma_equipada.get_danho()
        return danho_ataque

    #obtiene la defensa del escudo, devuelve un numero entero el cual posteriormente se le tomara como %, osea 30 de defensa = cubre 30% del daño
    def defender(self):
        defensa = self.__escudo_equipado.get_defensa()
        print(f"{defensa}%")

    def abrir_inventario(self):
        accion = self.__inventario.mostrar_inventario()
        if accion == 1: 
            pass
        elif accion == 2:
            self.usar_pocion()
        else:
            print(f"Saliste del inventario")
            return
                

raza = Raza()


