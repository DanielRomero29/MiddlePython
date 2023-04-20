# 4. Dada la siguiente lista de alumnos. 
import statistics
class Alumnos:
    nombre = ""
    apellido = ""
    edad = ""
    notas = []
    total= 0
    def __init__(self, nombre, apellido, edad, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.notas = notas
    def media(self):
        for i in self.notas:
            self.total += int(i)
        print(self.total/len(self.notas))

item1 = Alumnos("Juan", "Perez", "20",["7","8","9"])
item2 = Alumnos("Maria", "Gonzalez", "22",["6","9","10"])
item3 = Alumnos("Pedro", "Garcia", "21",["5","7","8"])
alumnos_lista = [{"nombre": item1.nombre, "apellido" : item1.apellido, "edad" : item1.edad, "notas" : item1.notas},
                   {"nombre": item2.nombre, "apellido" : item2.apellido, "edad" : item2.edad, "notas" : item2.notas},
                   {"nombre": item3.nombre, "apellido" : item3.apellido, "edad" : item3.edad, "notas" : item3.notas}]
item1.media()
print(alumnos_lista)
#    ```
#    alumnos_lista = [
#        {"nombre": "Juan", "apellido": "Pérez", "edad": 20, "notas": [7, 8, 9]},
#        {"nombre": "María", "apellido": "González", "edad": 22, "notas": [6, 9, 10]},
#        {"nombre": "Pedro", "apellido": "García", "edad": 21, "notas": [5, 7, 8]} ]
#    ```

#    Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de alumnos.

#    La clase deberá tener un método que incorpore el promedio de las notas del alumno.

# ​	