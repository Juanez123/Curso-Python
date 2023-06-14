# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.


def total():
    monto = float(input("ingresa el valor del producto pagado: "))
    iva = int(input("ingresa el valor del IVA: "))

    if iva != 0:
        if iva > 0:
            totalPagar = ((monto * iva) / 100) + monto
            return totalPagar
        else:
            return "El monto de iva es negativo ERROR"
    else:
        totalPagar = (monto * 0.21) + monto
        return totalPagar


print("El total de su monto es: ", total())
