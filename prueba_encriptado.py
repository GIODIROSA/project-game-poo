from argon2 import PasswordHasher

# Inicializa el hasher de Argon2
ph = PasswordHasher()

# Simula la creación de un hash (esto normalmente lo haces al registrar una contraseña)
stored_hash = ph.hash("sofia123")  # Genera el hash para "sofia123"


# Contraseña ingresada por el usuario
password_input = "sofia123"
print("password_input", password_input)



# Verificar la contraseña contra el hash almacenado
try:
    ph.verify(stored_hash, password_input)
    print("Contraseña verificada correctamente")
except Exception as e:
    print("Contraseña incorrecta:", str(e))
