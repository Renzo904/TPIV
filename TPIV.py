#Problema 1
nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}, tu nombre tiene {len(nombre)} letras.")

#Problema 2
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
print(f"La suma entre ellos es {num1 + num2}")

#Problema 3
base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("Ingrese la altura del rectangulo: "))
print(f"Su perimetro es {2 * (base + altura)}.")

#Problema 4
apellido = input("Ingrese su apellido: ")
parcialuno = int(input("Ingrese la nota del primer parcial: "))
parcialdos = int(input("Ingrese la nota del segundo parcial: "))
print(f"Alumno {apellido}:")
print(f"- Primer parcial: {parcialuno}.")
print(f"- Segundo parcial: {parcialdos}.")
print(f"- Promedio: {(parcialuno + parcialdos) / 2}")

#Problema 5
base = int(input("Ingrese la base a elevar: "))
exponente = int(input("Ingrese el exponente: "))
print(f"El resultado de {base}^{exponente} es {base ** exponente}")
