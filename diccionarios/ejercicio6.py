def promedio_notas(calificaciones):
    suma = 0.0
    numero_alumnos = 0
    for calificacion in calificaciones.items():
        suma += calificacion['nota']
        numero_alumnos += 1
    promedio = suma / numero_alumnos
    return promedio

calificaciones = {'nombre': 'Camila', 'nota': 5.0,
    'nombre': 'Carlos', 'nota': 4.5,
    'nombre': 'Johana', 'nota': 3.2,
    'nombre': 'Marcela', 'nota': 2.4,
    'nombre': 'Andres', 'nota': 3.8}


print("El número de alumnos es: ", len(calificaciones))
print("El promedio de notas es: ", promedio_notas(calificaciones))


# def alumno_con_mejor_nota(calificaciones):
#     nota_temporal = 0.0
#     nombre_temporal =' '
#     for alumno in calificaciones:
#         if nota_temporal <= alumno['nota']:
#             nombre_temporal = alumno['nombre']
#             nota_temporal = alumno['nota']

#     return nombre_temporal

# calificaciones =[ {'nombre': 'Camila', 'nota': 5.0},
#     {'nombre': 'Carlos', 'nota': 4.5},
#     {'nombre': 'Johana', 'nota': 3.2},
#     {'nombre': 'Marcela', 'nota': 2.4},
#     {'nombre': 'Andres', 'nota': 3.8}
# ]

# print("El número de alumnos es: ", len(calificaciones))
# print("El alumno con la nota más alta es: ", alumno_con_mejor_nota(calificaciones))