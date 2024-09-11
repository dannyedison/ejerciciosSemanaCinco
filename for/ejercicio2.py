""""
2. Contar la cantidad de elementos pares en una lista:

Crea una función llamada contar_pares que reciba una lista de números como parámetro y devuelva la cantidad de elementos pares que contiene.

Pista: Dentro del bucle "for", puedes verificar si cada elemento es divisible por 2.
"""
def pares(lista): 
    cantidad = 0
    for num in lista:
        if num % 2 == 0:
            cantidad += 1
        print(lista)
        print("La cantidad de pares en la lista es: ",cantidad)


lista1 = [5,4,6,2,6,8,9,10,1]
pares(lista1)