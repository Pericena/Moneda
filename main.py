from Arbol import Arbol
arbolito=Arbol()
arbolito.insertarprograma('cruz','C#')
arbolito.insertarinterfaz('cruz','C#','Android')
arbolito.insertarprograma('cruz', 'Netbeans')
arbolito.insertarinterfaz('cruz', 'Netbeans', 'Cuadro')
arbolito.insertarprograma('cara','Python')
arbolito.insertarinterfaz('cara', 'Python', 'Web')
arbolito.inOrden()
print(arbolito.pregunta2('Python'))
#aqui estaba probando mis funciones