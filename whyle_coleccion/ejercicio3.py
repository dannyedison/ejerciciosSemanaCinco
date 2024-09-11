"""
3. Contar vocales en una frase:

Crea un programa que pida al usuario que ingrese una frase y cuente la cantidad de vocales que contiene. 
El programa debe usar un bucle while para recorrer la frase y un contador para las vocales.

Pista: Puedes utilizar un bucle "while" que se ejecute mientras no se llegue al final de la frase.
"""
cadena = input("Ingresa una frase: ")
vocales = "aeiouAEIOU"
i = 0
contador = 0
while i < len(cadena):
    if cadena[i] in vocales:
        contador += 1
    i += 1
print("La frase tiene", contador, "vocales.")

