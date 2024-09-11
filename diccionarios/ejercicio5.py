"""
5. Buscar una palabra en un diccionario:

Crea una función llamada buscar_palabra que reciba un diccionario de palabras y definiciones como parámetro y 
una palabra a buscar. La función debe devolver la definición de la palabra si está presente en el diccionario, 
o un mensaje indicando que la palabra no se encontró.

Pista: Puedes utilizar la función get() para obtener el valor asociado a una clave en el diccionario.
"""

def buscar_palabra(diccionario, clave):
    definicion = diccionario.get(clave, print(f"La palabra '{clave}' no se encontró en el diccionario."))
    return definicion

diccionario =  {
    'Mamerto':'Le gusta vivir de los demás',
    'Mosca': 'Ponerse atento',
    'Teso':'Muy bueno para algo',
    'Memo':'Muy lento',
    'Pailas':'Ya perdió'
}

palabra_buscar = input("ingresar la palabra a buscar: ")
print("La definición de la palabra es: ", buscar_palabra(diccionario, palabra_buscar))
