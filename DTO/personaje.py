

class Personaje:
     __nombre= ""
     __nivel = 1
     __salud= 100

     def getNombre(self):
          return self.__nombre
     
     def getNivel(self):
          return self.__nivel
     
     def getSalud(self):
          return self.__salud
     
     def setNombre(self, nombre):
          self.__nombre = nombre

     def setNivel(self, nivel):
          self.__nivel = nivel

     def setSalud(self, salud):
          self.__salud = salud


     def atacar(self):
          pass
     def defender(self):
          pass
     def curar(self):
          pass
