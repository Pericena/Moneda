
from pickle import NONE
from Nodo import Nodo

class Arbol():
    raiz = None
    x = None

    def __init__(self):
        self.raiz = None

    def __init__(self, nivel):
        self.crearArbol(nivel)

    def getRaiz(self):
        return self.raiz

    def crearRecursivo(self,raiz,nivel):
        if(raiz is not None):
            if(nivel >= 1):
                raiz.set_hijo_derecho(Nodo("Cruz" , raiz.getProbabilidad()/2))
                raiz.set_hijo_izquierdo(Nodo("Cara" , raiz.getProbabilidad()/2))
                self.crearRecursivo(raiz.gethijoDerecho(),nivel-1)
                self.crearRecursivo(raiz.gethijoIzquierdo(),nivel-1)

    def crearArbol(self,nivel):
            self.raiz = Nodo("Probalidad",1)
            self.crearRecursivo(self.raiz, nivel) 

    def esCara(self, x):
        if(x =='Cara'):
            return -1
        else:
            return 0

    def cantidadnodoHoja(self):
        return self.cantidadHoja(self.getRaiz())
 
    def cantidadHoja(self, raiz):
        if(raiz.es_hoja()):
            return 1
        else:
            contador = 0
            contador = contador + self.cantidadHoja(raiz.gethijoIzquierdo())
            contador = contador + self.cantidadHoja(raiz.gethijoDerecho())
            return contador




    def probabilidad(self, valor , veces):
        return self.probabilidadCara(self.getRaiz(),valor,veces)

    def probabilidadCara(self, raiz, caraCruz, contador=0 ):
        if(raiz.es_hoja()):
            contador = contador + self.esCara(raiz.get_dato())
            if(contador == 0):
                return 1
            return 0
        else:
            if(raiz.get_dato() == caraCruz):
                contador = contador - 1
            y = self.probabilidadCara(raiz.gethijoIzquierdo(), caraCruz, contador)
            x = self.probabilidadCara(raiz.gethijoDerecho(), caraCruz, contador)
 
            return y + x
            
   

    