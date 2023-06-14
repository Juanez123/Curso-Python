# Escribir una función que reciba un número entero positivo y devuelva su factorial.


"""def Factorial():
    num = int(input("Ingrese un numero entero y postivo: "))
    if num > 0:
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
        print(factorial)
    else:
        print("El numero es negativo ERROR")


Factorial()"""

from math import factorial


def Factorial():
    num = int(input("Ingrese un numero entero y postivo: "))
    if num > 0:
        print(factorial(num))
    else:
        print("El numero es negativo ERROR")


Factorial()
