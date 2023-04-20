def principal():
    while True:
        try:
            palabra = input("Introduce una palabra: ").upper()
            if any(caracter in palabra for caracter in [' ', ',', '.', '!', '¡', '?', '¿', '=', '/', '*', '-', '+', '(', ')', '&', '%', '$', '·', '@', '|', 'º', 'ª', '<', '>', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']):
                raise ValueError
        except ValueError:
            print("Se han usado caracteres inválidos")
        else:
            break

    listaLetras = []

    for letra in palabra:
        listaLetras.append(letra)

    print(listaLetras)

if __name__ == "__main__" :
    principal()