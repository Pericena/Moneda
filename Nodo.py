'''
Diseñar una estructura nodo que soporte la estructura planteada en el diseño e implementar los metodos y atributos que crean que son necesarios para su implementacion
'''
class Nodo():
 

    def __init__(self, dato, p):
        self.dato = dato
        self.probabilidad = p
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        
    def set_dato(self, dato):
        self.dato = dato

    def setprobabilidad(self, p):
        self.probabilidad = p

    def set_hijo_izquierdo(self, hijoIzq):
        self.hijoIzquierdo = hijoIzq

    def set_hijo_derecho(self, hijoDer):
        self.hijoDerecho = hijoDer

    def get_dato(self):
        return self.dato
    
    def getProbabilidad(self):
        return self.probabilidad

    def gethijoIzquierdo(self):
        return self.hijoIzquierdo

    def gethijoDerecho(self):
        return self.hijoDerecho

    def es_hoja(self):
        return self.hijoDerecho is None and self.hijoIzquierdo is None
