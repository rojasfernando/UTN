#lista = Ariel, Liliana, Natalia, OSvaldo

nombres = ["Naty", "Osvaldo", "Lily","Ariel"]
#print(nombres)
#print(nombres[0])
#print(nombres[1])
#print(nombres[3])
#print(nombres[-1])
#print(nombres[-2])
print(nombres)
print(nombres[0:2])# solo muestra el indice 0, 1 pero no el indice 2

#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3])
#Desde el indice indicado hasta el final
print(nombres[1: ])

#modificar el valor
nombres[2]= "Liliana"
print(nombres)
nombres[0] = "Natalia"
print(nombres)
for nombre in nombres: #nombre es singular, la lista es plural.
    print(nombres)
else:
    print("se acabaron los elementos de la lista")

#Preguntamos cuantos elementos tiene
print(len(nombres))# le pasamos como parámetro la lista

#agregamos un elemento
nombres.append("Marcelo")
print(nombres)
nombres.append("Fernando")
print(nombres)
nombres.append("Valeria Cecilia")
print(nombres)

#Insertan un nuevo elemento en un indice especifico
nombres.insert(1, "Alberto")
print(nombres)
nombres.insert(3, "Debora")
print(nombres)
nombres.insert(4, "Martina")
print(nombres)

#Eliminamos elemntos
nombres.remove("Alberto")
print(nombres)
nombres.remove("Valeria Cecilia")
print(nombres)

#Eliminar el ultimos elemnto
nombres.pop()
print(nombres)
nombres.pop()
print(nombres)

#Eliminar un undice especifico
del nombres[2] # del siginifica delete (eliminar)
print(nombres)
del nombres[0]
print(nombres)

#Eliminar, borrar y limpiar todos los elmentos
nombres.clear()
print(nombres)

#>eliminar lista
del nombres
print(nombres) # muestra error por que fue elminada la lista, osea esta bien.
