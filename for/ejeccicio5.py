"""
5. Invertir una lista:

Crea una función llamada invertir_lista que reciba una lista como parámetro y devuelva una nueva lista con los elementos de la lista original invertidos.

Pista: Puedes agregar los elementos de la lista original en orden inverso a la nueva lista.
"""

def invertir_lista(lista):
    lista_nueva = []
    x = len(lista)-1
    for num in lista:
        if x >= 0:
            lista_nueva.append(lista[x])
            x -= 1
        
    return lista_nueva

lista1 = [0,1,2,3,4,5,6,7,8,9,10]
print("La lista inicial es :", lista1)
print("La nueva lista invertida es ",invertir_lista(lista1))
