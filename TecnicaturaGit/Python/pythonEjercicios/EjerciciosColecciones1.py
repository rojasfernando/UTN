# Ejercicio 1: eliminar duplicados de la lista.
#Escriba un programa donde tenga una lista y que a continuación
#Elimine los elementos repetidosm por ultimo mostrar la lista.

#Creamos una lista
lista = [1, 2, 3, "Ariel", 7, 7, 3, "Alberto", 1, "Ariel", 2, "Alberto"]
conjunto = set(lista) # con
#lista = list(conjunto)# convertimo el conjunto en una lista
lista = list(set(lista))
print(lista)

Otros ejemplos: con otras listas, viene del grupo en youtube
#sta2 = list(set(lista1)
#print(set([1,1,2,2])
#print(list(set(lista)))
#lista = [1, 2, 2, "Perro", "Perro", 1, 1