# Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras

for i in range(1, 11):
    print(i)

num1 = int(input("Ingresar primer numero: "))
num2 = int(input("Ingresar Segundo numero: "))

"""for i in range(num1, num2 + 1):
    print(i)"""

if num1 <= num2:
    for i in range(num1, num2 + 1):
        print(i)
else:
    for i in range(num2, num1 + 1):
        print(i)
