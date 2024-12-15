from enemigo import *

class Jugador:
    __victorias = 0
    def __init__(self, victorias = 0):
        self.__victorias = victorias
        self.personaje = None # Atributo para guardar el personaje creado
    
    def contador_victorias(self):
        self.__victorias += 1
        pass

    #En esta funcion se determina el nombre del personaje y se llama a la funcion elegir raza, la cual retorna el personaje(con su raza correspondiente) creada
    def crear_personaje(self):
        print("¡Bienvenido a la creación de tu personaje!")
        
        # Seleccionar nombre
        nombre = input("Ingrese el nombre de su personaje: ").strip()
        while not nombre:
            print("El nombre no puede estar vacío.")
            nombre = input("Ingrese el nombre de su personaje: ").strip()

        # Seleccionar raza
        print("\nSeleccione una raza para su personaje:")
        print("1. Humano")
        print("2. Orco")
        print("3. Elfo")
        print("4. Enano")
        self.elegir_raza(nombre)
        #Selecciona el arma del personaje llamando al metodo "elegir_arma()" de la clase "Raza"
        self.personaje.elegir_arma()
        print(f"\nTu personaje está listo: {self.personaje}")
        print(f"""
              Consejos: 
              Cada turno puedes realizar solo 1 accion(Atacar, defenderte o usar pocion(maximo 2)).
              Las pociones se restauran cada vez q ganas una batalla.
              Al subir de nivel, tu vida base incrementa al igual que el daño de tus armas,
              y ademas, dependiendo de tu raza, tus habilidades especiales se ven mejoradas.
              Si tienes suerte puedes esquivar el golpe.
              Siempre partiras primero.
              """)
        return self.personaje

    #Entra como parametro el "nombre" del personaje a crear y se le asigna al personaje creado eligiendo una opcion de raza
    def elegir_raza(self, nombre):
        raza_opcion = self.jug_validar_opcion("Eliga una opcion entre el 1 y el 4: ", opciones = [1, 2, 3, 4])
        if raza_opcion == 1:
            self.personaje = Humano(nombre)
            print(f"Has seleccionado: Humano. Bienvenido {nombre}, el valiente.")
        elif raza_opcion == 2:
            self.personaje = Orco(nombre)
            print(f"Has seleccionado: Orco. Bienvenido {nombre}, el feroz.")
        elif raza_opcion == 3:
            self.personaje = Elfo(nombre)
            print(f"Has seleccionado: Elfo. Bienvenido {nombre}, el ágil.")
        elif raza_opcion == 4:
            self.personaje = Enano(nombre)
            print(f"Has seleccionado: Enano. Bienvenido {nombre}, el resistente.")
       
    # def combate(self):
    #     print(f"Tu primer enemigo a enfrentar es: {enemigo_actual_lvl_1}")
    #     while True:
    #         self.menu_jugador()

        
    #     pass
        

    #Se le ingresa como parametro un mensaje y una lista de opciones / menu_jugador() y elegir_raza() la utilizan
    def jug_validar_opcion(self, mensaje, opciones):
        while True:
            try:
                opcion = int(input(f"{mensaje}"))
                if opcion in opciones:
                    return opcion
                else:
                    print(f" -{opcion}- no es valido, intentelo nuevamente. ")
            except ValueError:
                print("Entrada inválida. Por favor, intentelo nuevamente.")

    def menu_jugador(self):
        while True:
            print(f"""**Menu**
                  1.-Atacar
                  2.-Defenderse
                  3.-Usar Pocion (Cuentas con 2 pociones)
                  4.-Abrir inventario
                  5.-Salir al menu principal""")
            opcion = self.jug_validar_opcion("Eliga una opcion entre el 1 y el 5: ", opciones = [1, 2, 3, 4, 5])
            if opcion == 1:
                dahno_ataque = self.personaje.atacar()
                print(dahno_ataque)
            elif opcion == 2:
                defensa = self.personaje.defender()
                print(defensa)
            elif opcion == 3:
                print(self.personaje.get_vida())
                self.personaje.usar_pocion()
            elif opcion == 4:
                self.personaje.abrir_inventario()

                
            
                


################################################ MENU DE COMBATE ###################################################

print(f"El Umbral de las Sombras")
print(f"""Al cruzar el oscuro umbral de la mazmorra, el aire se vuelve pesado, cargado de un aroma metálico y húmedo. 
Una tenue luz titilante proviene de antorchas desgastadas, apenas iluminando los antiguos grabados en las paredes 
que narran historias de conquistas olvidadas y sacrificios sombríos.
Un eco lejano de pasos resonantes advierte que no están solos. 
En esta oscura profundidad, los ojos de criaturas desconocidas brillan en la penumbra, observando, esperando. 
Serán nueve los enemigos que enfrentarán, cada uno más letal y astuto que el anterior, surgidos al azar de los misterios que yacen ocultos.
El destino es incierto, pero una cosa es segura: solo quienes enfrenten el desafío con valentía y estrategia saldrán con vida de esta prisión olvidada.
¿Listos para desenvainar sus armas y probar su temple? La mazmorra no tiene piedad, y sus secretos no se entregan sin lucha
      """)


jugador = Jugador()
jugador.crear_personaje()
# jugador.menu_jugador()