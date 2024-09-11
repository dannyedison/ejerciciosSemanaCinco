"""
1. Eliminar duplicados de una lista:

Crea un programa que reciba una lista de números como entrada y devuelva una nueva 
lista con los mismos números pero sin duplicados.

Pista: Puedes utilizar un conjunto (set) para almacenar los elementos únicos de la 
lista.
"""
def eliminar_duplicados(lista):  
    conjunto1 = set(lista)
    lista_nueva = list(conjunto1)
    return lista_nueva

lista1 = [5,1,2,7,4,20,6,7,8,9,1]
print("Lista inicial: ", lista1)
print("Lista sin duplicados: ", eliminar_duplicados(lista1))