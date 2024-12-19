from .enemigo import *
from .humano import Humano
from .orco import Orco
from .elfo import Elfo
from .enano import Enano
import random
import pymysql
from DAO.conexion import conexion




##################################################           CONTADOR DE VICTORIAS= self.__victorias        ############################################################################



class Jugador:
    __victorias = 0
    def __init__(self, victorias = 0):
        self.__victorias = victorias
        self.personaje = None # Atributo para guardar el personaje creado
    
    def contador_victorias(self):
        self.__victorias += 1
        print(f"Ganaste el combate.\nVictorias: {self.__victorias}")
        self.personaje.get_inventario().inv_restaurar_pocion()
        if self.__victorias == 2:
            self.personaje.set_nivel(2)
            print(f"""
                Haz subido al nivel 2.
                Tu vida maxima ahora es {self.personaje.get_vida_base()}.
                Se a restaurado tu vida.
                Se han restaurado tus pociones.
                """)
        elif self.__victorias == 4:
            self.personaje.set_nivel(3)
            print(f"""
                    Haz subido al nivel 3.
                    Tu vida maxima ahora es {self.personaje.get_vida_base()}.
                    Se a restaurado tu vida.
                    Se han restaurado tus pociones.
                    """)
        pass

    def get_victorias(self):
        return self.__victorias
    
    #En esta funcion se determina el nombre del personaje y se llama a la funcion elegir raza, la cual retorna el personaje(con su raza correspondiente) creada
    def crear_personaje(self):
        print("¡Bienvenido a la creación de tu personaje!")
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

        print(f"""Antes de elegir personajes tienes q saber lo siguiente:
        Tendras 6 enfrentamientos, cada uno mas dificil que el anterior. Cada 2 victorias subiras de nivel (nivel max: 3)
        Las pociones te curan un 30%/40%/50% de vida segun el nivel del jugador. Podras acceder a ellas desde el inventario.
        Las pociones se restauran cada vez q ganas una batalla.
        Los escudos te cubren un 50% del daño total. Usalo, te puede salvar la vida.
        Cada personaje tiene una probabilidad de esquivar del 20% cada vez q lo ataquen.
        Cada turno puedes realizar solo 1 accion(Atacar, defenderte o usar una de tus 2 pociones).
        Siempre partiras primero.
        Al subir de nivel, tu vida base incrementa.
        Existen 4 razas principales, cada uno con habilidades unicas:
        Humanos: tienen 10% mas de daño con cualquier arma y se curan un 7%/14%/21% mas de vida usando pociones(segun nivel).
        Elfos: 20% mas de daño con los arcos y 40%/45%/50% de probabilidad de esquivar golpes (segun nivel).
        Orcos: 40% mas de daño con hachas y no pueden esquivar golpes.
        Enanos: 100% de reduccion de daño al ocupar el escudo y realizan un 15% mas de daño con hachas.
            """)
        
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
       
    def combate(self):
        niveles_combate = [
            (lista_enemigos_lvl_1, 2),  # 2 combates con enemigos de nivel 1
            (lista_enemigos_lvl_2, 2),  # 2 combates con enemigos de nivel 2
            (lista_enemigos_lvl_3, 2)   # 2 combates con enemigos de nivel 3
        ]

        for lista_enemigos, cantidad in niveles_combate:
            for _ in range(cantidad):
                enemigo = random.choice(lista_enemigos)
                lista_enemigos.remove(enemigo)  # Eliminar al enemigo seleccionado de la lista
                print(f"\n¡Comienza el combate contra {enemigo} !\n")

                turno = 1
                while self.personaje.get_vida() > 0 and enemigo.get_vida() > 0:
                    print(f"\n=== Turno {turno} ===")
                    print(f"Tu vida: {self.personaje.get_vida()} | Vida del enemigo ({enemigo.get_nombre()}): {enemigo.get_vida()}")

                    accion_realizada = False

                    while True:
                        print("\n¿Qué deseas hacer?")
                        print("1. Atacar")
                        print("2. Defenderse")
                        print("3. abrir inventario")
                        print("4. Huir del combate (Salir al menu principal)\n")

                        opcion = self.jug_validar_opcion("Elige una opción (1-4): ", opciones=[1, 2, 3, 4])

                        if opcion == 1:  # Atacar
                            if accion_realizada:
                                print("Ya realizaste una acción principal este turno (Atacar o Defenderse).")
                            else:
                                dano = self.personaje.atacar()
                                if not enemigo.esquivar():  # El enemigo tiene la oportunidad de esquivar
                                    enemigo.modificar_vida_enemiga(dano)
                                    print(f"¡Atacaste a {enemigo.get_nombre()} y causaste {dano} de daño!")
                                else:
                                    print(f"{enemigo.get_nombre()} esquivó tu ataque.")
                                accion_realizada = True

                        elif opcion == 2:  # Defenderse
                            if accion_realizada:
                                print("Ya realizaste una acción principal este turno (Atacar o Defenderse).")
                            else:
                                reduccion = self.personaje.defender()  # Obtener defensa del escudo equipado
                                print(f"Te preparas para el próximo ataque. Reducirás el daño recibido en {reduccion*100} %.")
                                self.personaje.set_defensa_activa(reduccion)  # Activar defensa
                                accion_realizada = True

                        elif opcion == 3:
                            self.personaje.abrir_inventario()
                            
                        elif opcion == 4:  # Salir al menu principal
                            print("¡Huiste del combate! El enemigo se burla de ti mientras escapas.")
                            return

                        # Salir del bucle de acción si una acción válida fue realizada
                        if accion_realizada or opcion == 3:
                            break

                    # Turno del enemigo
                    print(f"\n=== Turno del rival ===")
                    if enemigo.get_vida() > 0:
                        # Comprobamos si el jugador esquiva
                        if not self.personaje.esquivar():  # Si no esquiva, recibe el daño
                            dano_enemigo = enemigo.atacar()

                            if self.personaje.get_defensa_activa() > 0:  # Si el jugador tiene defensa activa
                                reduccion = self.personaje.get_defensa_activa()
                                dano_enemigo *= (1 - reduccion)  # Reducir el daño basado en la defensa activa
                                dano_enemigo = max(0, dano_enemigo)  # Evitar que el daño sea negativo
                                self.personaje.set_defensa_activa(0)  # Resetear defensa activa tras reducir daño

                            self.personaje.modificar_vida(dano_enemigo)
                            print(f"{enemigo.get_nombre()} te atacó y causó {int(dano_enemigo)} de daño.")
                        else:
                            print(f"Que suerte!, esquivaste su ataque.")

                    turno += 1

                # Fin del combate
                if self.personaje.get_vida() > 0:
                    print(f"\n¡Has derrotado a {enemigo.get_nombre()}!")
                    self.contador_victorias()
                else:
                    print("\nHas sido derrotado. ¡El combate ha terminado!")
                    return  # Salir si el jugador muere
                
                
                
                
        print("""
              \nEl Último Eco de Eldoria
                Tras las nueve arduas batallas en las oscuras profundidades del Umbral de las Sombras, finalmente has llegado al final de tu camino. 
                La mazmorra, que una vez parecía interminable, ahora se encuentra en silencio, como si sus antiguos ecos se hubieran apagado con tu última victoria. 
                El aire, que antes estaba cargado de tensión y peligro, se ha despejado. Pero el viaje no ha terminado.
                El Cristal de Eldoria, la fuente de toda la magia y el equilibrio, yace ante ti, fragmentado, tal y como lo dejaron aquellos que lo buscaron antes. 
                Las piezas rotas brillan débilmente, como si aún esperaran ser reunidas para restaurar la paz, o tal vez, para desatar una nueva era de caos.
                Los reinos de Eldoria se encuentran en una encrucijada. El Rey Alaric, los elfos de los bosques eternos, 
                los orcos de Rak’thor y los enanos de las tierras de forja han sido testigos de tu poder, tu habilidad y tu decisión. Ahora, los ojos de todos se centran en ti. 
               ¿Restaurarás el cristal para devolver la prosperidad a tu reino? ¿O, tal vez, seguirás el camino de los orcos, buscando el poder absoluto? 
               ¿Protegerás la magia como lo desean los elfos, o permitirás que los enanos oculten su poder, como siempre han querido?
                En este momento, solo tú puedes decidir el destino de Eldoria. Los reinos te esperan, y sus corazones palpitantes esperan tu juicio.
              """)
        self.enviar_victorias_db()

    def enviar_victorias_db(self):
             #capturar victoria imprimir 
        print("VERIFICAR VICTORIAS",self.__victorias)
        try:
            print(f"Puntaje obtenido por el jugador: {self.__victorias}")
            with conexion.cursor() as cursor:
                insert_query = "INSERT INTO ranking (RG_puntaje) VALUES (%s)"
                cursor.execute(insert_query, (self.__victorias)) # Si el jugador existe, actualiza las victorias. Si no, inserta un nuevo registro.
                conexion.commit()
                print("Se guardo ranking correctamente en la base de datos.")#Guarda los cambios en la base de datos con commit().       
        except pymysql.MySQLError as e:
                print(f"Error al enviar victorias a la base de datos: {e}")#Maneja errores en la base de datos.

    @staticmethod        
    def mostrar_ranking():
        """
        Obtiene y muestra el ranking de jugadores desde la base de datos.
        """
        try:
            with conexion.cursor() as cursor:
                query = """
                SELECT RG_puntaje FROM ranking ORDER BY RG_puntaje DESC 
                """ #Consulta todos los jugadores ordenados por número de victorias en orden descendente.
                cursor.execute(query)
                ranking = cursor.fetchall()

                if not ranking:  # Verifica si la lista está vacía
                    print("\nNo hay jugadores en el ranking aún.")
                    return
                
                print("\n=== Ranking de Jugadores ===")    
                for i, row in enumerate(ranking, start=1):
                    print(f"{i}. Puntaje: {row[0]}")

        except pymysql.MySQLError as e:
            print(f"Error al obtener el ranking: {e}")#Maneja errores de la base de datos.
        
        except Exception as ex:
            print(f"Ocurrió un error inesperado: {ex}")


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


jugador = Jugador()
