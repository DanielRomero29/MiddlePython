#En una clase de programación hay dos alumnos, Ana y Luis, que han asistido a diferentes sesiones de clase.
#La información se encuentra en un diccionario donde las llaves son los nombres de los alumnos y los valores son tuplas con las sesiones a las que asistieron.

#3. Mostrar las sesiones a las que asistió uno de los dos alumnos, pero no a las que asistieron ambos.



def Ejercicio3():

    asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}

    #3

    asistenciasAna = set(asistencias["Ana"])
    asistenciasLuis = set(asistencias["Luis"])
    asistenciasUnAlumno = []
    
    for x in asistenciasAna:
        if x not in asistenciasLuis:
            asistenciasUnAlumno.append(x)

    for x in asistenciasLuis:
        if x not in asistenciasAna:
            asistenciasUnAlumno.append(x)

    asistenciasUnAlumno.sort()
    print()
    print(f"3 - Las sesiones a las que solo asistió uno de los alumnos y no ambos fueron las sesiones: {asistenciasUnAlumno}")


    #3B
    asistenciasUnAlumno2 = [x for x in asistenciasAna if x not in asistenciasLuis]
    asistenciasUnAlumno3 = [x for x in asistenciasLuis if x not in asistenciasAna]
    asistenciasUnAlumnoFinal = asistenciasUnAlumno2 + asistenciasUnAlumno3

    asistenciasUnAlumnoFinal.sort()
    print()
    print(f"3B - Las sesiones a las que solo asistió uno de los alumnos y no ambos fueron las sesiones: {asistenciasUnAlumnoFinal}")