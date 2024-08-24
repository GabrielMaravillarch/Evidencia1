# Crear un diccionario con información de una persona
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print("Diccionario de persona:", persona)

# Acceder a un valor por su clave
print("Nombre de la persona:", persona["nombre"])

# Agregar un nuevo par clave-valor
persona["profesión"] = "Ingeniero"
print("Diccionario después de agregar 'profesión':", persona)

# Modificar un valor en el diccionario
persona["edad"] = 31
print("Diccionario después de modificar la edad:", persona)

# Eliminar un par clave-valor
del persona["ciudad"]
print("Diccionario después de eliminar 'ciudad':", persona)
