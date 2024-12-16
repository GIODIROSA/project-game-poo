from .pociones import pociones

class Inventario:
    __objetos = []
    __pociones = pociones

    def __init__(self):
        self.__objetos = []  # Lista para almacenar objetos (armas, escudos, pociones, etc.)
        self.__objetos.append(self.__pociones)

    # def menu_inventario(self):
    #     print("")

    def get_inventario(self):
        return self.__objetos

    def get_pociones(self):
        return self.__pociones
    
    def agregar_objeto(self, objeto):
        """Agrega un objeto al inventario."""
        self.__objetos.append(objeto)
        # print(f"Se agregó {objeto.get_nombre()} al inventario.")

    def eliminar_objeto(self, objeto):
        """Elimina un objeto del inventario si está presente."""
        if objeto in self.__objetos:
            self.__objetos.remove(objeto)
            print(f"Se eliminó {objeto.get_nombre()} del inventario.")
        else:
            print(f"{objeto.get_nombre()} no está en el inventario.")

    def mostrar_inventario(self):
        """Muestra todos los objetos en el inventario."""
        if not self.__objetos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for i, objeto in enumerate(self.__objetos, start=1):
                print(f"{i}. {objeto.get_nombre()} - {objeto.get_tipo()}")
        while True:
            print(f"""**Accion en el inventario: **
                  1.-Usar Pocion (Cuentas con {self.__pociones} pociones)
                  2.-Salir del inventario""")
            opcion = self.inv_validar_opcion("Eliga una opcion entre el 1 y el 3: ", opciones = [1, 2])
            if opcion == 1:
                return 1
            elif opcion == 2:
                return 2

    def inv_restaurar_pocion(self):
        self.__pociones.restaurar_pociones()

    def inv_restar_pocion(self):
        self.__pociones.restar_pocion()

    def inv_validar_opcion(self, mensaje, opciones):
        while True:
            try:
                opcion = int(input(f"{mensaje}"))
                if opcion in opciones:
                    return opcion
                else:
                    print(f" -{opcion}- no es valido, intentelo nuevamente. ")
            except ValueError:
                print("Entrada inválida. Por favor, intentelo nuevamente.")

    # def obtener_objeto(self, indice):
    #     """Obtiene un objeto del inventario basado en el índice."""
    #     if 0 <= indice < len(self.objetos):
    #         return self.objetos[indice]
    #     else:
    #         print("Índice fuera de rango.")
    #         return None


inventario = Inventario()
# inventario.mostrar_inventario()