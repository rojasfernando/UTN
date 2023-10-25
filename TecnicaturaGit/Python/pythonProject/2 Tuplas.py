# TUPLAS PARTE 1
# Definimos una Tupla
cocina = ("cuchara", "cuchillo", "Tenedor")
print(len(cocina))

#Acceder a un elemento, para esto utilizamos corchetes no parentesis.
print(cocina[0])

#mostrar la manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])

#Ejemplo
verduras = ("papa", "cebolla", "batata")
print(verduras[0:3])# Una tupla necesite aunque sea un elemento la coma, de lo contrario sería un
# tipo string o cadena.

# TUPLAS PARTE 2
# Recorremos los elementos de una tupla
for cocinar in cocina: # print esta usando \n para saltos de líneas
    print(cocinar, end=" ") # Usamos end= para eliminar los saltos de líneas

cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)
print("\n", cocina)