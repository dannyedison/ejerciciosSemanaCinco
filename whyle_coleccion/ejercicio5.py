"""
5. Crear una lista de números pares:

Crea un programa que cree una lista con todos los números pares entre 1 y 100. Utiliza un 
bucle while para recorrer los números del 1 al 100 y agregar los pares a la lista.

Pista: Puedes utilizar un bucle "while" que se ejecute mientras el contador sea menor o igual a 100.
"""

lista1 = []
i = 1

while i <= 100:
    if i % 2 == 0:
            lista1.append(i)
    i += 1
print(lista1)

