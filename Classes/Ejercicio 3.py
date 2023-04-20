# 3. Dada la siguiente lista de productos. 
class Producto:
    nombre = ""
    precio = ""
    stock = ""
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

item1 = Producto("Leche", "2.50", "10")
item2 = Producto("Huevos", "1.50", "20")
item3 = Producto("Pan", "1.00", "15")
productos_lista = [{"nombre": item1.nombre, "precio" : item1.precio, "stock" : item1.stock},
                   {"nombre": item2.nombre, "precio" : item2.precio, "stock" : item2.stock},
                   {"nombre": item3.nombre, "precio" : item3.precio, "stock" : item3.stock}]

print(productos_lista)
#    ```
#    productos_lista = [
#        {"nombre": "Leche", "precio": 2.50, "stock": 10},
#        {"nombre": "Huevos", "precio": 1.50, "stock": 20},
#        {"nombre": "Pan", "precio": 1.00, "stock": 15}
#    ]
#    ```

#    Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de productos.
