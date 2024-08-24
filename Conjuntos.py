# Crear un conjunto de frutas
frutas = {"manzana", "naranja", "plátano"}
print("Conjunto de frutas:", frutas)

# Agregar un elemento al conjunto
frutas.add("uva")
print("Conjunto después de agregar uva:", frutas)

# Intentar agregar un duplicado (no se agregará)
frutas.add("naranja")
print("Conjunto después de intentar agregar 'naranja' de nuevo:", frutas)

# Realizar una operación de unión con otro conjunto
otras_frutas = {"cereza", "manzana", "pera"}
frutas_union = frutas.union(otras_frutas)
print("Unión de conjuntos:", frutas_union)

# Realizar una operación de intersección con otro conjunto
frutas_interseccion = frutas.intersection(otras_frutas)
print("Intersección de conjuntos:", frutas_interseccion)
