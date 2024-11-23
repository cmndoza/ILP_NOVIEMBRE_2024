numero = int(input("Introduzca el número a evaluar:"))
if numero > 0 and numero < 100:
    for numero in range(1, 101):
        if numero % 2 == 0:
            print (numero)
elif numero < 0 and numero > (-100):
    for numero in range(1, 101):
        if numero % 2 != 0:
            numero_form = numero * (-1)
            print (numero_form)
else:
    print ("No válido")

