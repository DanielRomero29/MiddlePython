#En una clase de programación hay dos alumnos, Ana y Luis, que han asistido a diferentes sesiones de clase.
#La información se encuentra en un diccionario donde las llaves son los nombres de los alumnos y los valores son tuplas con las sesiones a las que asistieron.

#4. Mostrar las sesiones a las que asistió Ana pero no Luis.


def principal():

    asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}
    
    #4

    asistenciasAna = set(asistencias["Ana"])
    asistenciasLuis = set(asistencias["Luis"])

    asistenciasUnicasAna = []
    for x in asistenciasAna:
        if x not in asistenciasLuis:
            asistenciasUnicasAna.append(x)

    print()
    print(f"4 - Las sesiones a las que asistió Ana pero no Luis fueron las sesiones: {asistenciasUnicasAna}")

    #4B

    asistenciasUnicasAna2 = [x for x in asistenciasAna if x not in asistenciasLuis]

    print()
    print(f"4B - Las sesiones a las que asistió Ana pero no Luis fueron las sesiones: {asistenciasUnicasAna2}")