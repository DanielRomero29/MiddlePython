#En una clase de programación hay dos alumnos, Ana y Luis, que han asistido a diferentes sesiones de clase.
#La información se encuentra en un diccionario donde las llaves son los nombres de los alumnos y los valores son tuplas con las sesiones a las que asistieron.


#1. Calcular la cantidad total de sesiones a las que asistieron Ana y Luis en conjunto.

def Ejercicio1():
    asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}

    #1
    asistenciasConjunto = asistencias["Ana"] + asistencias["Luis"]
    print(f"1 - Ana y Luis asistieron a {len(asistenciasConjunto)} sesiones entre los 2")
