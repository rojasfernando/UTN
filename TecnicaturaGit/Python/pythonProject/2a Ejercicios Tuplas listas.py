#EJERCICIO
# Dada la siguiente tupla
# definir la tupla
#Crear una lista que solo incluya los números menores a 5
# e imprima por concola [1, 3, 2]

tupla = (13, 1, 8, 3, 2, 5, 8)
lista = [] # definimos la lista
for elemento in tupla:
    if elemento< 5:
        lista.append(elemento)
print(lista)
