edad = int(input("Escribe tu edad: "))

if edad < 0:
    print ("LA EDAD INGRESADA ES INCORRECTA 'EDAD NEGATIVA'")
elif edad >=18:
    print ("LA PERSONA ES MAYOR DE EDAD, TIENE",edad,"AÑOS")
else:
    print ("LA PERSONA ES MENOR DE EDAD, TIENE",edad,"AÑOS")