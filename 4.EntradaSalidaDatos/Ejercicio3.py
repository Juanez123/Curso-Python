# Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas.

Vocal = input("Vocal en minuscula: ")
Consonante = input("Letra en Mayuscula: ")

Vocal = Vocal.lower()
Consonante = Consonante.upper()

print("La consonante fue: {}\nLa vocal fue: {}".format(Consonante,Vocal))