# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

Edad = int(input("Ingrese su edad: "))
i = 1
 
while i <= Edad:
    print("Has cuamplido: {} años".format(i))
    i += 1    