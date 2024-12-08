import pymysql
import constantes

# Configuración de conexión
host = "localhost"     
user = "dragons"       
password = "okidoki"
database = "dungeon_and_dragons" 


try:
    conexion = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("¡Conexión exitosa!")


    with conexion.cursor() as cursor:
    
        cursor.execute("SELECT VERSION();")
        version = cursor.fetchone()
        print(f"Versión de MySQL: {version[0]}")

except pymysql.MySQLError as e:
    print("Ocurrió un error al conectar a MySQL:", e)

finally:
 
    if 'conexion' in locals() and conexion.open:
        conexion.close()
        print("Conexión cerrada.")
