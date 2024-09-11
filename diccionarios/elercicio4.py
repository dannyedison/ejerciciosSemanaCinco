"""
4. Crear un diccionario de palabras y sus definiciones:

Crea un programa que permita al usuario ingresar una palabra y su definición, y almacene esta información en un 
iccionario. El programa debe permitir al usuario agregar varias palabras y sus definiciones. 
Finalmente, el programa debe mostrar el diccionario con todas las palabras y sus definiciones.

Pista: Puedes utilizar un bucle "while" para que el programa siga pidiendo datos hasta que el usuario decida salir.
"""

diccionario = {}
while True:
    print("1 - Para ingresar término")
    print("2 - Para mostrar el diccionario")
    print("0 - Para terminar")
    opcion = input("Seleccione una opción): ")

    if opcion == '1':
        palabra = input("Ingrese la palabra: ")
        definicion = input("Ingrese su definición: ")
        diccionario[palabra] = definicion
    elif opcion == '2':
        for clave, valor in diccionario.items():
            print(f"{clave}: {valor}")
        print("Terminó la aplicación ")
    elif opcion == '0':
        print("Terminó la aplicación ")
        break
    else:
        print("Opción no válida, intente nuevamente")