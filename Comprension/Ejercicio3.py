def principal():
    nombre = ""
    dic_personas = {}
    while nombre != "0":
        while True:
            try:
                nombre = input("Escribe un nombre: ")
                edad = input("Escribe una edad: ")
                if type(edad) != type(int) or edad < 0:
                    raise ValueError
            except ValueError:
                print("La edad debe ser un entero positivo")
            else:
                break

        dic_personas[nombre] = edad

    print(dic_personas)

if __name__ == "__main__" :
    principal()