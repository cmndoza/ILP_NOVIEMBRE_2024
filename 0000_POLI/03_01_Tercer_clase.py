from decimal import Decimal, ROUND_HALF_UP

edad = float(input("Escribe tu edad: "))
edad = edad.quatize(Decimal('0.0'), rounding=ROUND_HALF_UP)
#edad = round(edad, 1)

#RANGAO VÁLIDO DE EDAD ENTRE 18 Y 120 AÑOS
if edad < 0 or edad > 120:
    print ("LA EDAD INGRESADA ", edad ,"ES ILÓGICA")
elif edad >=18 and edad<=120:
    print ("LA PERSONA ES MAYOR DE EDAD, TIENE",edad,"AÑOS")
elif edad < 18 and edad >= 0:
    print ("LA PERSONA ES MENOR DE EDAD, TIENE",edad,"AÑOS")
else:
    print("IMPRIME OTRA COSA")