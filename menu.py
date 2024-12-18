
import pymysql
#import bcrypt
from argon2 import PasswordHasher
from DAO.conexion import conexion
from DTO.jugador import jugador


ph = PasswordHasher()

sesion_iniciada = False



def registro():
    print("=== Registro ===")
    nombre_usuario = input("Ingresa tu nombre de usuario: ").lower()
    correo = input("Ingresa tu correo: ")
    password = input("Ingresa tu contraseña: ")

 
    hashed_password = ph.hash(password)

    if not conexion or not conexion.open:
        print("La conexión no está activa. Revisa la configuración.")
        return

    try:
        with conexion.cursor() as cursor:

            check_query = """
            SELECT COUNT(*) FROM usuarios WHERE USU_nombre = %s
            """
            cursor.execute(check_query, (nombre_usuario,))
            result = cursor.fetchone()
            
            if result[0] > 0:
                print(f"El nombre de usuario '{nombre_usuario}' ya está registrado. Intenta con otro.")
                return
  
            insert_query = """
            INSERT INTO usuarios (USU_nombre, USU_pass, USU_correo) 
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (nombre_usuario, hashed_password, correo))
            conexion.commit()
            print("Registro exitoso. Por favor, inicia sesión.")
    except pymysql.MySQLError as e:
        print(f"Ocurrió un error al registrar el usuario: {e.args}")



def login():
    print("=== Inicio de Sesión ===")
    global sesion_iniciada
    usuario = input("Ingresa tu usuario: ").lower() 
   
    password = input("Ingresa tu contraseña: ")
 
 
    try:
        with conexion.cursor() as cursor:
            query = """
            SELECT USU_pass FROM usuarios WHERE USU_nombre = %s
            """
            cursor.execute(query, (usuario,))
            result = cursor.fetchone()

            if result:
                stored_hash = result[0].strip()  
                
                try:
                    ph.verify(stored_hash, password)
                    print("Inicio de sesión exitoso. ¡Bienvenido!")
                    sesion_iniciada = True
                except:
                    print("Usuario o contraseña incorrectos.")
            else:
                print("Usuario no encontrado.")
    except pymysql.MySQLError as e:
        print("Ocurrió un error durante el inicio de sesión:", e)



def salir():
    print("Gracias por jugar. ¡Hasta la próxima!")
    return True


def menu_principal():
    salir_juego = False
    opcion_seleccionada = False
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
            1. Crear personaje
            2. Combatir
            3. Ver Ranking
            4. Salir
            """)
            opcion = input("Selecciona una opción: ")
            if opcion == "1":
                jugador.crear_personaje()
                opcion_seleccionada = True
            elif opcion == "2":
                if opcion_seleccionada:
                    jugador.combate()
                else:
                    print("No puedes combatir sin antes crear a tu personaje")
                    
                opcion_seleccionada = False
            elif opcion == "3":
                jugador.mostrar_ranking()#Asegura que mostrar_ranking() esté definida como una función global en Jugador.py, 
                                         #Jugador, será necesario incluir self como parámetro y ajustarla en consecuencia.
            elif opcion == "4":
                salir_juego = salir()

    if conexion and conexion.open:
        conexion.close()
        print("Conexión a la base de datos cerrada.")

