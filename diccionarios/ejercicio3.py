"""
3. Encontrar al alumno con la nota más alta:

Crea una función llamada alumno_con_mejor_nota que reciba un diccionario de alumnos y notas como parámetro 
y devuelva el nombre del alumno con la nota más alta.

Pista: Puedes utilizar un bucle "for" para recorrer las notas del diccionario y encontrar la nota más alta.
"""
def alumno_con_mejor_nota(calificaciones):
    nota_temporal = 0.0
    nombre_temporal =' '
    for alumno in calificaciones:
        if nota_temporal <= alumno['nota']:
            nombre_temporal = alumno['nombre']
            nota_temporal = alumno['nota']

    return nombre_temporal

calificaciones =[ {'nombre': 'Camila', 'nota': 5.0},
    {'nombre': 'Carlos', 'nota': 4.5},
    {'nombre': 'Johana', 'nota': 3.2},
    {'nombre': 'Marcela', 'nota': 2.4},
    {'nombre': 'Andres', 'nota': 3.8}
]

print("El número de alumnos es: ", len(calificaciones))
print("El alumno con la nota más alta es: ", alumno_con_mejor_nota(calificaciones))