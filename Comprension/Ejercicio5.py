def principal():
    listapalabras = input("Escribe un texto: ").split()
    diccionario = {}

    for palabra in listapalabras:
        if palabra in diccionario.keys():
            diccionario[palabra] = diccionario[palabra]+1
        else:
            diccionario[palabra] = 1

    print(diccionario)

if __name__ == "__main__" :
    principal()