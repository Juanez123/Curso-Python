'''Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final'''

Practica1 = float(input("Ingrese el valor de la practica 1: "))
Practica2 = float(input("Ingrese el valor de la practica 2: "))
Practica3 = float(input("Ingrese el valor de la practica 3: "))
ExamenParcial = float(input("Ingrese el valor del examen parcial: "))
ExamenFinal = float(input("Ingrese el valor del examen final: "))

PromedioPractica = (Practica1 + Practica2 + Practica3)/3

PromedioFinal = (PromedioPractica + 2*ExamenParcial + 3*ExamenFinal) /6

print("El promedio de practica del estudiante es de:\n ", PromedioPractica, "\n Y el promedio final es de:\n ",PromedioFinal)