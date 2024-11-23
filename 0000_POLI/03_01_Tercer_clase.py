edad = int(input("Escribe tu edad: "))

#RANGAO VÁLIDO DE EDAD ENTRE 18 Y 120 AÑOS
if edad < 0 or edad > 120:
    print ("LA EDAD INGRESADA ", edad ,"ES ILÓGICA")
elif edad >=18 and edad<=120:
    print ("LA PERSONA ES MAYOR DE EDAD, TIENE",edad,"AÑOS")
elif edad < 18 and edad >= 0:
    print ("LA PERSONA ES MENOR DE EDAD, TIENE",edad,"AÑOS")
else:
    print("IMPRIME OTRA COSA")