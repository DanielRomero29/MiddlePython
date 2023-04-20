def principal():
    import json
    # ### Programa 2: Transacción financiera:
    transaccion = {
    "id": input("Id: "),
    "fechayhora" : input("Fecha y Hora: "),
    "monto" : input("Monto: "),
    "tipo" : input("Tipo: "),
    "producto" : {"nombre": input("Nombre:"), "Precio": input("Precio: "), "Descripcion": input("Descripcion: ")}}
    print(transaccion)
    transaccionJSON=json.dumps(transaccion)
    print(transaccionJSON)

    # El JSON generado deberá ser.
    # ```
    # {"id": 123456789, "fechayhora": "2023-04-18T12:30:00Z", "monto": 500.25, "tipo": "compra", "producto": {"nombre": "Smartphone", "precio": 450.00, "descripcion": "Un teléfono inteligente de última generación"}}
    # ```
if __name__=="__main__":
   principal()