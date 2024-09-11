"""
1. Sumar todos los elementos de una lista:

Crea una función llamada suma_elementos que reciba una lista de números como parámetro y devuelva la suma de todos sus elementos.

Pista: Puedes utilizar una variable para acumular la suma dentro del bucle "for".
"""

def suma_lista(lista):
    suma = 0
    for contenido in lista:
        suma += contenido
    print(lista)
    print("la suma de la lista es ",suma)

lista1 =[5,9,7,4]
suma_lista(lista1)
