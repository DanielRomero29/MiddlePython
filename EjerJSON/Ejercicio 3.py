import json
# ### Programa 3: Información medica de paciente:

paciente = {
"nombre": input("Nombre: "),
"apellido" : input("Apellido: "),
"edad" : input("Edad: "),
"peso" : input("altura: "),
"historial_medico" : {"alergias": [input("Alergias: ")], "problemas_cardiacos": input("Problemas Cardiacos: "), "medicamentos": [{"nombre" : input("Nombre del medicamento: "), "dosis" : input("Dosis: ")}, {"nombre" : input("Nombre del medicamento: "), "dosis" : input("Dosis: ")}], "ultima_revision" : input("Ultima Revision"), "proximo_turno" : input("Fecha Proximo Turno: ")}}
print(paciente)
pacienteJSON=json.dumps(paciente)
print(pacienteJSON)

# El JSON generado deberá ser:

# ```
# {"nombre": "Pedro", "apellido": "Pérez", "edad": 45, "peso": 80.5, "altura": 1.75, "historial_medico": {"alergias": ["penicilina", "mariscos"], "problemas_cardiacos": false, "medicamentos": [{"nombre": "Ibuprofeno", "dosis": "200mg"}, {"nombre": "Paracetamol", "dosis": "500mg"}]}, "ultima_revision": "2022-10-01", "proximo_turno": "2023-05-15"}
# ```

# **NOTA: **Para comprobar los programas anteriores, cree un programa en python, que pida un JSON como texto y lo convierta en un objeto Python y lo muestre por pantalla.


