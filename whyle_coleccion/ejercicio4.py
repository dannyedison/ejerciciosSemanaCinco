"""
4. Calculadora básica:

Crea un programa que simule una calculadora básica. El usuario debe poder ingresar dos números y 
seleccionar una operación (+, -, *, /). El programa debe realizar la operación y mostrar el resultado. 
Utiliza un bucle while para que la calculadora funcione hasta que el usuario decida salir.

Pista: Puedes utilizar un bucle "while" que se ejecute hasta que el usuario ingrese una opción para salir.
"""

numero_uno = int(input("Igresar el primer número: "))
numero_dos = int(input("Igresar el segundo número: "))

while True:
    print("+")
    print("-")
    print("*")
    print("/")
    print("0 para terminar")
    opcion = input("Seleccione una opción): ")

    if opcion == '+':
        print("El resultado de la suma es: ",numero_uno + numero_dos)
    elif opcion == '-':
        print("El resultado de la resta es: ",numero_uno - numero_dos)
    elif opcion == '*':
        print("El resultado de la multiplicación es: ",numero_uno * numero_dos)
    elif opcion == '/':
        print("El resultado de la división es: ",numero_uno / numero_dos)
    elif opcion == '0':
        print("Terminó la aplicación ")
        break
    else:
        print("Opción no válida, intente nuevamente.")