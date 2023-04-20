'''
En una clase de programación hay dos alumnos, Ana y Luis, que han asistido a diferentes sesiones de clase. La información se encuentra en un diccionario donde las llaves son los nombres de los alumnos y los valores son tuplas con las sesiones a las que asistieron.

```
asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}
```

Se pide:

1. Calcular la cantidad total de sesiones a las que asistieron Ana y Luis en conjunto.
2. Mostrar las sesiones a las que asistieron ambos alumnos.
3. Mostrar las sesiones a las que asistió uno de los dos alumnos, pero no a las que asistieron ambos.
4. Mostrar las sesiones a las que asistió Ana pero no Luis.
5. Mostrar las sesiones a las que asistió Luis pero no Ana.
'''

asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}
sumatorio = 0
asistieronambos = []
nottogether = []
onlyana = []
onlyluis = []

for sesiones in asistencias.values():
    sumatorio += len(sesiones)

for sesionAna in asistencias["Ana"]:
    if sesionAna not in asistencias["Luis"]:
        onlyana.append(sesionAna)
        nottogether.append(sesionAna)
    else:
        asistieronambos.append(sesionAna)

for sesionLuis in asistencias["Luis"]:
    if sesionLuis not in asistencias["Ana"]:
        onlyluis.append(sesionLuis)
        nottogether.append(sesionLuis)


print(f"Entre ambos alumnos han ido a {sumatorio} sesiones")
print(f"Ambos fueron a las sesiones {asistieronambos}")
print(f"Solo fue uno de ellos a las sesiones {nottogether}")
print(f"Ana fue sola a las sesiones {onlyana}")
print(f"Luis fue solo a las sesiones {onlyluis}")

