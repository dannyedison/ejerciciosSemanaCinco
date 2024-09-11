""""
2. Adivinar un número con intentos limitados:

Crea un programa que genere un número aleatorio entre 1 y 100, y el usuario debe adivinarlo en un máximo 
de 7 intentos. El programa debe indicar si el número ingresado es mayor o menor que el número 
secreto, y cuántos intentos le quedan. 
Si el usuario adivina el número o se quedan sin intentos, el juego termina.

Pista: Puedes utilizar un bucle "while" que se ejecute mientras los intentos sean mayores que 0 y 
el usuario no haya adivinado el número.
"""

import random

aleatorio = random.randint(1, 100)
intentos = 0
intentos_max = 7
#print("aleatorio", aleatorio)
print("Estoy pensando en un número entre 1 y 20.")
while intentos < intentos_max and not adivinado:
    ingreso = int(input("Adivinar el número entre 1  y 100: "))#ingresar numero
    intentos += 1
    if ingreso == aleatorio:
        print("¡FELICITACIONES! Has adivinado el número")
        adivinado = True
    elif ingreso < aleatorio:
        print("El número es mayor a ", ingreso, "y le quedan ", (intentos_max - intentos), "intentos")
    else:
        print("El número es menor a ", ingreso, "y le quedan ", (intentos_max - intentos), "intentos")

else:
   print("Se agotaron el número de intentos, el número era ", aleatorio)
   print("SUETE PARA LA PRÓXIMA")