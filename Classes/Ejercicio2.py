def principal():
    # 2. Crear una clase `Flor` que tenga los atributos `nombre` (cadena de caracteres) y `color` (cadena de caracteres). El constructor debe recibir ambos atributos como argumentos e inicializarlos. Agregar un método `mostrar_informacion` que imprima por pantalla el nombre y color de la flor. Crear dos objetos de la clase `Flor` e invocar el método `mostrar_informacion` para ambos.
    class Flor:
        nombre=""
        color=""
        def __init__(self, nombre, color):
            self.nombre = nombre
            self.color = color
        def mostrar_informacion(self):
            print(f"La flor es {self.nombre} y es de color {self.color}")

    flor1 = Flor("Tulipan", "Rojo")
    flor2 = Flor("Girasol", "Amarilla")
    flor1.mostrar_informacion()
    flor2.mostrar_informacion()
if __name__=="__main__":
   principal()