#En una clase de programación hay dos alumnos, Ana y Luis, que han asistido a diferentes sesiones de clase.
#La información se encuentra en un diccionario donde las llaves son los nombres de los alumnos y los valores son tuplas con las sesiones a las que asistieron.


#2. Mostrar las sesiones a las que asistieron ambos alumnos.

def principal():

    asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}

    asistenciasAna = set(asistencias["Ana"])
    asistenciasLuis = set(asistencias["Luis"])
    asistenciasComun = asistenciasAna.intersection(asistenciasLuis)
    print()
    print(f"2 - Las sesiones a las que asistieron ambos fueron las sesiones: {asistenciasComun}")