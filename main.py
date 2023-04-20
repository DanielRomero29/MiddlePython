import os
#from Varios import principal

from Colecciones import Ejercicio1
from Colecciones import Ejercicio2
from Colecciones import Ejercicio3
from Colecciones import Ejercicio4
from Colecciones import Ejercicio5
from Comprension import Ejercicio1
from Comprension import Ejercicio2
from Comprension import Ejercicio3
from Comprension import Ejercicio4
from Comprension import Ejercicio5
from Comprension import Ejercicio6
from EjerJSON import Ejercicio1
from EjerJSON import Ejercicio2
from EjerJSON import Ejercicio3
from Classes import Ejercicio1
from Classes import Ejercicio2
from Classes import Ejercicio3
from Classes import Ejercicio4

def submenu(opcion,carpeta):
    
    if opcion == "1":
        print("Bienvenido al submenú sobre COLECCIONES")
        
        print("1-Ejercicios sobre COLECCIONES")
        print("2-Ejercicios sobre COMPRENSION DE LISTAS")
        print("3-Ejercicios sobre JSON")
        print("4-Ejercicios sobre CLASES")
    elif opcion == "2":
        print("Bienvenido al submenú sobre COMPRENSION DE LISTAS")
        
        print("1-Ejercicios sobre COLECCIONES")
        print("2-Ejercicios sobre COMPRENSION DE LISTAS")
        print("3-Ejercicios sobre JSON")
        print("4-Ejercicios sobre CLASES")
        print("1-Ejercicios sobre COLECCIONES")
        print("2-Ejercicios sobre COMPRENSION DE LISTAS")
    elif opcion == "3":
        print("Bienvenido al submenú sobre JSON")
        
        print("1-Ejercicios sobre COLECCIONES")
        print("2-Ejercicios sobre COMPRENSION DE LISTAS")
        print("3-Ejercicios sobre JSON")
    elif opcion == "4":
        print("Bienvenido al submenú sobre CLASES")
        
        print("1-Ejercicios sobre COLECCIONES")
        print("2-Ejercicios sobre COMPRENSION DE LISTAS")
        print("3-Ejercicios sobre JSON")
        print("4-Ejercicios sobre CLASES")
        
    op = input("Seleccione una opción: ")
    
    if op == "1":
        carpeta.Ejercicio1.principal()
    elif op == "2":
        carpeta.Ejercicio2.principal()
    elif op == "3":
        carpeta.Ejercicio3.principal()
    elif op == "4":
        carpeta.Ejercicio4.principal() 
    elif op == "5":
        carpeta.Ejercicio5.principal() 
    elif op == "6":
        carpeta.Ejercicio6.principal() 
        

    continuar=input("Presione enter para continuar...")
    
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
        submenu("1","Colecciones")
    elif op == "2":
        submenu("2","Comprension")
    elif op == "3":
        submenu("3", "EjerJSON")
    elif op == "4":
        submenu("4", "Classes")
    
    elif op == "0":
        print("Un placer . Nos vemos!")
        break
    
    
    
   

    
