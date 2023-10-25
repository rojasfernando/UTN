#Repaso de set o conjunto
#Para definir un conjunto
conjunto2 = set()
conjunto1 = {"Bye" ,}
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el 3 no está en el conjunto1.

#Como hacer la igualdad de don conjuntos
print(conjunto1 == conjunto2) #Nos devuelve como respuesta un booleano

#Operaciones en conjunto
conjunto3 = conjunto1 | conjunto2 # La línea une los dos conjutno
print(conjunto3)

#Intersección
conjunto3 = conjunto1 & conjunto2 # Es el elemento que tienen en común.
print(conjunto3) ## Tiene que salir "Hola", no sale. Ver el signo de interseccion.

# Conjunto de que deben unirse
conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2.
print(conjunto3) ## No salió

conjunto3 = conjunto2 - conjunto1 #Alrevés.
print(conjunto3) ## No salio

# Diferencia simtétrica
conjunto3 = conjunto2 ^ conjunto1 #alt 94
print(conjunto3)