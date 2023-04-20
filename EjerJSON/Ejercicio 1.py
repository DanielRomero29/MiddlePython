# # Ejercicios sobre JSON
import json
# Dados los siguientes JSON, deberá crear un programa en python, que pida la información por teclado, conforme un objeto Python y al final convierta el objeto conformado al JSON correspondiente: 

# ### Programa 1: Información sobre un usuario: 

persona = {
"nombre": input("Nombre: "),
"edad" : input("Edad: "),
"email" : input("email: "),
"trabajo" : {"empresa": input("empresa:"), "puesto": input("puesto: ")}}
print(persona)
personaJSON=json.dumps(persona)
print(personaJSON)

# El JSON generado deberá ser.
# ```
# {"nombre": "Juan", "edad": 30, "email": "juan@acme.com", "trabajo": {"empresa": "Acme Corp", "puesto": "Ingeniero de software"}}
# ```