#Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla

tupla = ('Enero','Febero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')

OpcionMes = int(input("escribe un numero: "))
'''OpcionMes -= 1

print("Tu mes es: ", tupla[OpcionMes])'''
print("Tu mes es: ", tupla[OpcionMes-1])
