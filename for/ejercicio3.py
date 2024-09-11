"""
3. Encontrar el elemento más grande de una lista:

Crea una función llamada elemento_mas_grande que reciba una lista de números como parámetro y devuelva el elemento más grande de la lista.

Pista: Puedes utilizar una variable para almacenar el elemento más grande encontrado hasta el momento.
"""
def mayor(lista): 
    nmayor = 0
    for num in lista:
        if num > nmayor:
            nmayor = num
    print(lista)
    print("El número mayor en la lista es: ",nmayor)

lista1 = [5,4,6,20,2,6,15,8,9,10,1]
mayor(lista1)