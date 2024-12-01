import os

iteracion = int (0)
acumulado = int (0)

captura = int(input("Capture un número: "))
salida = 1

while (salida == 1):
    os.system('cls')
    if captura > 0:
        iteracion = iteracion + 1
        acumulado = acumulado + captura
        captura = int(input("Capture un número: "))
        salida = 1
    else:
        salida = 0
        promedio = int(acumulado/iteracion)
        print("Se realizaron", iteracion, "capturas de datos que sumaron un total de", acumulado, "unidades")
        print ("El promedio del ejercicio anterior es:", promedio)

