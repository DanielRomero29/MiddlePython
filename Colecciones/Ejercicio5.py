#En una clase de programación hay dos alumnos, Ana y Luis, que han asistido a diferentes sesiones de clase.
#La información se encuentra en un diccionario donde las llaves son los nombres de los alumnos y los valores son tuplas con las sesiones a las que asistieron.


#5. Mostrar las sesiones a las que asistió Luis pero no Ana.


def Ejercicio5():
    
    asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}
    
    #5

    asistenciasAna = set(asistencias["Ana"])
    asistenciasLuis = set(asistencias["Luis"])

    asistenciasUnicasLuis = []
    for x in asistenciasLuis:
        if x not in asistenciasAna:
            asistenciasUnicasLuis.append(x)

    print()
    print(f"5 - Las sesiones a las que asistió Luis pero no Ana fueron las sesiones: {asistenciasUnicasLuis}")


    #5B

    asistenciasUnicasLuis2 = [x for x in asistenciasLuis if x not in asistenciasAna]

    print()
    print(f"5B - Las sesiones a las que asistió Luis pero no Ana fueron las sesiones: {asistenciasUnicasLuis2}")