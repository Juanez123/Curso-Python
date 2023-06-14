#Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
# Extraño <--> Tamaño
# Desligado <--> Amigo
# Riman <--> Cuerpo
# Sol <--> Lol

Palabra1 = input("Ingresa la primer palabra: ")
Palabra2 = input("Ingresa la segunda palabra: ")

if len(Palabra1) < 3 or len(Palabra2) < 3:
    print("No rima, porque tiene menos de dos caracteres")
elif Palabra1[-3 : ] == Palabra2[-3 : ]:
    print("Las palabras riman")
elif Palabra1[-2 : ] == Palabra2[-2 : ]:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")