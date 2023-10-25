#Ejercicio 2: operaciones en conjunto con lisgas
#escriba un  programa que tena 2 listas y que a continuacion
#cree las siguientes listas (en la que nos deben haber repeticion.
# 1 listas de palabras que aparecen en listas
# 2 Listas de palabtas que aparecen en la pri,era lista, pero no en la segunda.
# 3 lsitas de palabras qiue aárecen en ña segunda lista, péro no en la primera
# 4 listas de palabras que aparecen en ambas lista

lista1 = [1, 2, 3, 4, 5, 4, 5, 4, 3, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]

#Eliminar los elemntos repertidos de ambas liostras con conkuntos

conjunto1 = set(lista1)
conjunto2 = set(lista2)
interseccion = list(conjunto1&conjunto2)# mostramos elementos que muestran en ambas lista

union = list( conjunto1 | conjunto2)# unimos los dos conjuntos
solo1 = list(conjunto1 - conjunto2) #solo muestra 1
solo2 = list( conjunto2 - conjunto1) # solo muestra 2
print(f"lista de palabras que aparecen en la lisytas: {union}")
print(f"lista de palabras que aparecen en la primer lista, pero no en la segunda: {solo1}")
print(f"lista de palabras que aparecen en la primer lista, pero no en la segunda: {solo2}")
print(f"lista de plabras que aparecen en ambas listas:{interseccion}")

