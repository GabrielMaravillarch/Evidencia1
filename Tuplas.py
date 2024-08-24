# Crear una tupla de coordenadas
coordenadas = (10, 20)
print("Tupla de coordenadas:", coordenadas)

# Acceder a elementos de la tupla
x, y = coordenadas
print(f"Coordenadas: x = {x}, y = {y}")

# Intentar modificar un elemento de la tupla (esto causará un error)
# coordenadas[0] = 15  # Descomenta esta línea para ver el error de inmutabilidad

# Crear una nueva tupla (ya que no se puede modificar la existente)
nueva_coordenada = (15, 20)
print("Nueva tupla de coordenadas:", nueva_coordenada)
