import os
#from Varios import principal

from Colecciones import Ejercicio1 as col1
from Colecciones import Ejercicio2 as col2
from Colecciones import Ejercicio3 as col3
from Colecciones import Ejercicio4 as col4
from Colecciones import Ejercicio5 as col5
from Comprension import Ejercicio1 as com1
from Comprension import Ejercicio2 as com2
from Comprension import Ejercicio3 as com3
from Comprension import Ejercicio4 as com4
from Comprension import Ejercicio5 as com5
from Comprension import Ejercicio6 as com6
from EjerJSON import Ejercicio1 as json1
from EjerJSON import Ejercicio2 as json2
from EjerJSON import Ejercicio3 as json3
from Classes import Ejercicio1 as cla1
from Classes import Ejercicio2 as cla2
from Classes import Ejercicio3 as cla3
from Classes import Ejercicio4 as cla4

def submenu(opcion,carpeta):
    
    if opcion == "1":
        print("Bienvenido al submenú sobre COLECCIONES")
        
        print("1-Calcular la cantidad total de sesiones a las que asistieron Ana y Luis en conjunto.")
        print("2-Mostrar las sesiones a las que asistieron ambos alumnos.")
        print("3-Mostrar las sesiones a las que asistió uno de los dos alumnos, pero no a las que asistieron ambos.")
        print("4-Mostrar las sesiones a las que asistió Ana pero no Luis.")
        print("5-Mostrar las sesiones a las que asistió Luis pero no Ana.")
    elif opcion == "2":
        print("Bienvenido al submenú sobre COMPRENSION DE LISTAS")
        
        print("1-Crear una lista que contenga las letras de una palabra, cada una en mayúscula")
        print("2-Crear un diccionario que contenga el cuadrado de cada número del 1 al 5:")
        print("3-Crear un diccionario que contenga los nombres y edades de varias personas:")
        print("4-Crear una lista que contenga los números del 1 al 20, pero reemplazando los múltiplos de 3 por 'EOI', los múltiplos de 5 por 'Cloud' y los múltiplos de ambos por 'EOICloud'")
        print("5-Crear un diccionario que contenga las palabras en una lista y la cantidad de veces que aparecen en ella.")
        print("6-Dado un texto con una lista de ciudades con su emblema mas importante, pedir las ciudades para que las entre el usuario por teclado y crear un diccionario con su ciudad y su emblema.")
    elif opcion == "3":
        print("Bienvenido al submenú sobre JSON")
        
        print("1-Generar JSON correspondiente")
        print("2-Generar JSON correspondiente")
        print("3-Generar JSON correspondiente")
    elif opcion == "4":
        print("Bienvenido al submenú sobre CLASES")
        
        print("1-Crear una clase `Lapiz` que tenga los atributos `color` (cadena de caracteres) y `grosor` (entero). El constructor debe inicializar ambos atributos con valores por defecto. Agregar un método `escribir` que imprima por pantalla la frase 'Escribiendo con un lapiz de [color] y grosor [grosor]'. Crear un objeto de la clase `Lapiz` e invocar el método `escribir`.")
        print("2-Crear una clase `Flor` que tenga los atributos `nombre` (cadena de caracteres) y `color` (cadena de caracteres). El constructor debe recibir ambos atributos como argumentos e inicializarlos. Agregar un método `mostrar_informacion` que imprima por pantalla el nombre y color de la flor. Crear dos objetos de la clase `Flor` e invocar el método `mostrar_informacion` para ambos.")
        print("3-Ejercicio 3")
        print("4-Ejercicio 4")
        
    op = input("Seleccione una opción: ")
    
    if op == "1":
        s = f"{carpeta}1.principal()"
        eval(s)
    elif op == "2":
        s = f"{carpeta}2.principal()"
        eval(s)
    elif op == "3":
        s = f"{carpeta}3.principal()"
        eval(s)
    elif op == "4":
        s = f"{carpeta}4.principal()"
        eval(s)
    elif op == "5":
        s = f"{carpeta}5.principal()"
        eval(s)
    elif op == "6":
        s = f"{carpeta}6.principal()"
        eval(s)
        

#continuar=input("Presione enter para continuar...")
    
while True:
    os.system("cls") #Limpia la pantalla en la consola

    print("Bienvenidos")
    print("Menu principal")

    print("1-Ejercicios sobre COLECCIONES")
    print("2-Ejercicios sobre COMPRENSION DE LISTAS")
    print("3-Ejercicios sobre JSON")
    print("4-Ejercicios sobre CLASES")
    
    print("0- Salir")
    
    op = input("Seleccione una opción: ")
    if op == "1":
        submenu("1","col")
    elif op == "2":
        submenu("2","com")
    elif op == "3":
        submenu("3", "json")
    elif op == "4":
        submenu("4", "cla")
    
    elif op == "0":
        print("Un placer . Nos vemos!")
        break
    
    
    
   

    
