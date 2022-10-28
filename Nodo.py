'''
Diseñar una estructura nodo que soporte la estructura planteada en el diseño e implementar los metodos y atributos que crean que son necesarios para su implementacion
'''
class Nodo:
        def __init__(self, dato):
            self.__HD = None
            self.__HI = None
            self.__dato = dato
 
        
        def getDato(self):
            return self.__dato
        def setDato(self, dato):
            self.__dato = dato
        def getHI(self):
            return self.__HI
        def setHI(self, node):
            self.__HI = node
        def getHD(self):
            return self.__HD
        def setHD(self,node):
            self.__HD = node
        
        def cantidadHijos(self):
            a = 0
            if self.__HI is not None:
                a = a + 1
            if self.__HD is not None:
                a = a + 1
            return a

        def esHoja(self):
            if self.cantidadHijos() == 0:
                return True
            return False
