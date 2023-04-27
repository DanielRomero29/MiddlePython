def principal():
    diccionNomyEdad = {}

    while True:
        nombre = input("Introduce un nombre: ")
        edad = input("Introduce una edad: ")

        if not edad.isdigit():
            edad = input("Introduce una edad correcta: ")
        else:
            edad = int(edad)
        diccionNomyEdad.update({nombre:edad})
        op = input("Registrado, ¿Quieres añadir otro dato? s/n: ").lower()
        if op == "n":
            break
        
    print(diccionNomyEdad)

if __name__ == "__main__" :
    principal()