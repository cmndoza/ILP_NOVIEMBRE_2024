from datetime import date

año_nacimiento = int(input("¿EN QUÉ AÑO NACIÓ, USTED? R= "))
hoy = date.today()
año_hoy = int(hoy.year)
#edad = año_hoy - año_nacimiento
#edad = int (0)
edad = int(año_hoy - año_nacimiento)
#fecha_en_texto = '{}/{}/{}'.format(hoy.day, hoy.month, hoy.year)

print ("CONSIDERANDO QUE NACIÓ EN",año_nacimiento,", AL PRESENTE AÑO USTED TIENE",edad, "AÑOS DE EDAD")

