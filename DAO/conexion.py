import pymysql
from decouple import config

host = config('HOST')
user = config('USER')
password = config('PASSWORD')
database = config('DATABASE')

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
    conexion = None
