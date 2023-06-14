cadena = "Te quiero solo como amigo"
cadena2 = "arroz"

# Imprimir los dos primeros caracteres.
print(cadena [0:2])

# Imprimir los tres últimos caracteres.
print(cadena [-3:])

# Imprimir dicha cadena cada dos caracteres. Ej: Si la cadena fuera "recta" deberia imprimir rca
print(cadena [::2]) 

# Dicha cadena en sentido inverso. Ej: Si la cadena fuera Hola mundo! deberia imprimir !odnum aloH
print(cadena2 [::-1])

# Imprimir la cadena en un sentido y en sentido inverso. Ej: Si la cadena es "reflejo" imprime reflejoojelfer.  
print(cadena + cadena [::-1])