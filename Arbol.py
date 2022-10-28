'''
Modificar el Metodo Insertar para que este se adecue a la estructura planteado en el diseño, y crear los metodos que veas necesarios para interactuar con la interfaz grafica
'''

from Nodo import Nodo
    
class Arbol:
    __raiz = None
    
    def __init__(self):
        self.__raiz = Nodo('Moneda')
        self.__raiz.setHD(Nodo('cara'))
        self.__raiz.setHI(Nodo('cruz'))
    
    def insertarprograma(self, tipo, programa): 
            if tipo == 'cruz':
                aux = self.__raiz.getHI()
                self.__insertar1(aux, programa)
            else:
                if tipo == 'cara':
                    aux = self.__raiz.getHD()
                    self.__insertar1(aux, programa)
                
    def __insertar1(self, nodo, programa):
        if nodo.getHD() is None:
            nodo.setHD(Nodo(programa))
        elif nodo.getHI() is None:
                nodo.setHI(Nodo(programa))
        else:
            print('Campo de programas llenos')
            
    def insertarinterfaz(self, tipo, programa, interfaz):
        if tipo == 'cruz':
            aux = self.__raiz.getHI()
            aux2 = aux.getHI()
            aux =aux.getHD()
            if aux.getDato() == programa:
                if aux.getHD() is None:
                    aux.setHD(Nodo(interfaz))
                elif aux.getHI() is None:
                    aux.setHI(Nodo(interfaz))
                else:
                    print('Interfaces llenas')
            else:
                if aux2.getDato() == programa:
                    if aux2.getHD() is None:
                        aux2.setHD(Nodo(interfaz))
                    elif aux2.getHI() is None:
                        aux2.setHI(Nodo(interfaz))
                    else:
                        print('Interfaces llenas')
        else:        
            if tipo == 'cara':
                aux = self.__raiz.getHD()
                aux2 = aux.getHI()
                aux =aux.getHD()
                if aux.getDato() == programa:
                    if aux.getHD() is None:
                        aux.setHD(Nodo(interfaz))
                    elif aux.getHI() is None:
                        aux.setHI(Nodo(interfaz))
                    else:
                        print('Interfaces llenas')
                else:
                    if aux2.getDato() == programa:
                        if aux2.getHD() is None:
                            aux2.setHD(Nodo(interfaz))
                        elif aux2.getHI() is None:
                            aux2.setHI(Nodo(interfaz))
                        else:
                            print('Interfaces llenas')

    def inOrden(self):
        if self.__raiz is None:
            return
        else:
            self.__inOrden1(self.__raiz)               
    
    
    def __inOrden1(self, nodo):
        if nodo is not None:
            self.__inOrden1(nodo.getHI())
            print((nodo.getDato()))
            self.__inOrden1(nodo.getHD()) 
            
    
            
            
    def pregunta2(self, interfaz):
        ruta = self.__pregunta2(self.__raiz, interfaz)
        if ruta is not None:
            return ruta
        return "No existe : " + interfaz
    
    def __pregunta2(self, nodo, interfaz):
        if nodo is None:
            return None
        if nodo.esHoja():
            if nodo.getDato() == interfaz:
                return str(nodo.getDato())
            else:
                return None
        if nodo.getDato() == interfaz:
            return str(nodo.getDato())
        
        ruta1 = self.__pregunta2(nodo.getHI(), interfaz)
        ruta2 = self.__pregunta2(nodo.getHD(), interfaz)
        if ruta1 != None:
            return nodo.getDato() + " -> " + ruta1
        if ruta2 != None:
            return nodo.getDato() + " -> " + ruta2
        return None
    
    
    
    def mostrar(self):
        aux = self.__raiz
        aux = aux.getHD()
        aux = aux.getHI()
        aux = aux.getHI()
        return aux.getDato()
        
        
   
        
    