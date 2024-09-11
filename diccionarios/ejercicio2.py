"""
2. Calcular el promedio de las notas de un diccionario:

Crea una función llamada promedio_notas que reciba un diccionario de alumnos y notas como parámetro y devuelva 
el promedio de todas las notas.

Pista: Puedes utilizar un bucle "for" para recorrer las notas del diccionario y calcular la suma de todas las notas.
"""

def promedio_notas(calificaciones):
    suma = 0.0
    for alumno in calificaciones:
        suma += alumno['nota']
    promedio = suma / len(calificaciones)
    return promedio

calificaciones =[ {'nombre': 'Camila', 'nota': 5.0},
    {'nombre': 'Carlos', 'nota': 4.5},
    {'nombre': 'Johana', 'nota': 3.2},
    {'nombre': 'Marcela', 'nota': 2.4},
    {'nombre': 'Andres', 'nota': 3.8}
]

print("El número de alumnos es: ", len(calificaciones))
print("El promedio de notas es: ", promedio_notas(calificaciones))