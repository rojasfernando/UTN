import math
#dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = [] #Definimos la lista
#Filtramos los elementos menores a 5 de la tupla
for elemnto in tupla:
    if elemnto < 5:
        lista.append(elemnto)
print(lista)

# Ejercicio de matematicas
# Para sacar la raiz cuandrada de uin número positivo
numero = int(input("Digite un numero positivo"))
while numero < 0:
    print ("Error -> DEBERÍA SER UN NUMERO POSOTIVO")
    numero = int(input("Digite un número positivo"))
print(f"\0")

# TODOS LOS EJERCICIOS VAN EN LA CARPETA O PROYECTO "LECCIÓN 4"