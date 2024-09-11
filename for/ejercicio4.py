"""
4. Crear una nueva lista con los elementos de otra lista multiplicados por 2:

Crea una función llamada multiplicar_elementos que reciba una lista de números como parámetro y devuelva una nueva lista con los elementos de la lista original multiplicados por 2.

Pista: Puedes crear una nueva lista vacía y agregar los elementos multiplicados por 2 dentro del bucle "for".
"""

def copia(lista): 
    lista_nueva = []
    for num in lista:
        lista_nueva.append(num*2)
        
    print(lista)
    print("La lista nueva es ", lista_nueva)

lista1 = [5,4,6,20,2,6,15,8,9,10,1]
copia(lista1)
