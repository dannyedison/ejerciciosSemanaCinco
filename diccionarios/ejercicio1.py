"""
1. Crear un diccionario de alumnos y sus notas:

Crea un programa que permita al usuario ingresar el nombre y la nota de un alumno, y almacene esta información en un diccionario. 
El programa debe permitir al usuario agregar varios alumnos y sus notas. Finalmente, el programa debe mostrar el diccionario con 
todos los alumnos y sus notas.

Pista: Puedes utilizar un bucle "while" para que el programa siga pidiendo datos hasta que el usuario decida salir.
"""

calificaciones = {}
while True:
    print("1 - Para ingresar nombre y nota")
    print("2 - Para mostrar nombres y notas")
    print("0 - Para terminar")
    opcion = input("Seleccione una opción): ")

    if opcion == '1':
        nombre = input("Ingrese nombre del estudiante: ")
        nota = input("Ingrese la nota: ")
        calificaciones[nombre] = nota
    elif opcion == '2':
        for nombre, nota in calificaciones.items():
            print(f"{nombre}: {nota}")
        print("Terminó la aplicación ")
    elif opcion == '0':
        print("Terminó la aplicación ")
        break
    else:
        print("Opción no válida, intente nuevamente")