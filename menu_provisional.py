
usuario_registrado = {}
sesion_iniciada = False
jugador = None
enemigo = None
armas = ["Espada", "Arco", "Hacha"]
escudos = ["Ligero", "Pesado"]
razas = ["Humano", "Orco", "Elfo", "Enano"]

def intro():
    print("""
    *** Bienvenido a la Era Medieval ***
    En un mundo donde humanos, orcos, elfos y enanos luchan por el control del reino,
    tú serás el héroe que escriba su propia historia.
    """)

def registro():
    print("=== Registro ===")
    usuario = input("Ingresa tu usuario: ")
    password = input("Ingresa tu contraseña: ")
    usuario_registrado[usuario] = password
    print("Registro exitoso. Por favor, inicia sesión.")

def login():
    print("=== Inicio de Sesión ===")
    global sesion_iniciada
    usuario = input("Usuario: ")
    password = input("Contraseña: ")
    if usuario in usuario_registrado and usuario_registrado[usuario] == password:
        print("Inicio de sesión exitoso. ¡Bienvenido!")
        sesion_iniciada = True
    else:
        print("Usuario o contraseña incorrectos.")

def seleccionar_raza():
    global jugador
    print("=== Selección de Raza ===")
    for i, raza in enumerate(razas, start=1):
        print(f"{i}. {raza}")
    eleccion = int(input("Selecciona tu raza: "))
    jugador = razas[eleccion - 1]
    print(f"Has seleccionado: {jugador}")

def seleccionar_enemigo():
    global enemigo
    print("=== Selección de Enemigo ===")
    for i, raza in enumerate(razas, start=1):
        print(f"{i}. {raza}")
    eleccion = int(input("Selecciona a tu enemigo: "))
    enemigo = razas[eleccion - 1]
    print(f"Te enfrentarás a: {enemigo}")

def equipar_arma_y_escudo():
    print("=== Equipar Arma y Escudo ===")
    print("Armas disponibles:")
    for i, arma in enumerate(armas, start=1):
        print(f"{i}. {arma}")
    arma_elegida = int(input("Selecciona tu arma: "))
    print("Escudos disponibles:")
    for i, escudo in enumerate(escudos, start=1):
        print(f"{i}. {escudo}")
    escudo_elegido = int(input("Selecciona tu escudo: "))
    print(f"Has equipado {armas[arma_elegida - 1]} y {escudos[escudo_elegido - 1]}.")

def mostrar_estadisticas():
    print(f"""
    === Estadísticas del Jugador ===
    Raza: {jugador}
    Salud: 100
    Fuerza: 50
    Defensa: 30
    """)

def salir():
    print("Gracias por jugar. ¡Hasta la próxima!")
    return True


def menu_principal():
    salir_juego = False
    while not salir_juego:
        if not sesion_iniciada:
            print("\n1. Registrarse\n2. Iniciar sesión\n3. Salir")
            opcion = input("Selecciona una opción: ")
            if opcion == "1":
                registro()
            elif opcion == "2":
                login()
            elif opcion == "3":
                salir_juego = True
        else:
            print("""
            === Menú Principal ===
            1. Seleccionar raza
            2. Equipar arma y escudo
            3. Seleccionar enemigo
            4. Iniciar batalla
            5. Ver estadísticas
            6. Salir
            """)
            opcion = input("Selecciona una opción: ")
            if opcion == "1":
                seleccionar_raza()
            elif opcion == "2":
                equipar_arma_y_escudo()
            elif opcion == "3":
                seleccionar_enemigo()
            elif opcion == "4":
                print("La batalla comenzará pronto... (en desarrollo)")
            elif opcion == "5":
                mostrar_estadisticas()
            elif opcion == "6":
                salir_juego = salir()

# Inicio del juego
intro()
menu_principal()
