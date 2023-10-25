# CLASE 4
#OPERADORES PYTHON -- f es el formato

operandoA = 50
operandoB = 70

suma: int= operandoA + operandoB
print(f"El resultado de la suma es: {suma}")

operandoc = 500
operandod = 360
suma2: int = operandoc + operandod
print(F"el resultado de la suma es: {suma2}")

resta = operandoc - operandod
print(f"el resultado es: {resta}")

modulo = operandoc % operandod
print(f"el resultado es: {modulo}")

# Rectangulo
#alto = int(input("Ingrese la altura"))
#ancho = int(input("ingrese el ancho"))
#area = alto * ancho
#perimetro = (alto + ancho) *2
#print("Área: ", area)
#print("Perímetro: ", perimetro)


# OPERADORES DE REASIGNACIÓN:
# operadores aritmétcios con reasignación

#miVariable3 = 10
#print(miVariable3)

#miVariable3 = miVariable3 + 1
#print(miVariable3)

#miVariable3 += 1
#print(miVariable3)

#OPERADORES DE COMPARACION
d = 4
b = 5
resultado = d == b
print(resultado)

# OPERADOR MAYOR O IGUAL
a = int(input("Digite un numero: "))
print(f"El residuo de la división es: {a % 2}")
if a % 2 == 0:
    print(f"El resultado que digitó: {a} ,es par.")
else:
    print(f"El número que digitó: {a} , es impar. ")

edadAdulto = 18
edadPersona = int(input("Digite su edad: "))
print(f"El residuo de la edad es: {edadPersona % 2}")

if edadPersona >= edadAdulto:
    print(f"Su edad es: {edadPersona} años, Ud. es mayor de edad.")
else:
    print(f"Su edad es: {edadPersona} años, Ud. es menor de edad.")
