def principal():
    ciudadesOrdenadas={ 
        "Ámsterdam": "Los molinos de viento",
        "Buenos Aires": "El Obelisco",
        "Johannesburgo": "El león",
        "Londres": "El Big Ben",
        "Moscú": "El Kremlin",
        "Nueva York": "La Estatua de la Libertad",
        "París": "La Torre Eiffel",
        "Sídney": "La Opera de Sídney",
        "Tokio": "La flor del cerezo",
        "Dubai": "El Burj Khalifa"
    }
    
    #Ir añadiendo a mano. 
    #while True:
    #    ciudad=input("Ciudad:")
    #    emblema=input("Emblema")
    #    ciudadesOrdenadas[ciudad]=emblema

    filtro=input("¿Por qué desea filtrar el emblema?: ")
    ciudadConFiltro = {}
    for ciudad,emblema in ciudadesOrdenadas.items():
        if emblema.startswith(filtro):
            ciudadConFiltro[ciudad]=emblema

    ciudadConFiltro1 = {ciudad:emblema  for ciudad,emblema in ciudadesOrdenadas.items() if emblema.startswith(filtro)}

    print(f"Ciudades cuyo emblema empieza con {filtro} son:")
    print(ciudadConFiltro)
    print(ciudadConFiltro1)
    

if __name__ == "__main__" :
    principal()