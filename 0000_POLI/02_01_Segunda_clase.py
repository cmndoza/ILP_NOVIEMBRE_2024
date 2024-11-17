
#PARA HACER LA IMPORTACION DE UNA LIBRERIA
import math
#DELCARACION O CREACION DE VARIABLES O CONSTANTES
numero_1 = 0
numero_2 = 0

numero_1 = float (input("ingresa un número: "))
numero_2 = float (input("ingresa otro número: "))

#Genracion de variables con asignaciones de operaciones aritmeticas <
suma = numero_1 + numero_2
resta = numero_1 + numero_2
multiplicacion = numero_1*numero_2
division = numero_1 / numero_2

potencia_1 = numero_1 ** numero_2
potencia_2 = pow(numero_1, numero_2)
cuadrado = numero_1 ** 2
cubo = pow(numero_2, 3)

raiz_cuadrada_1 = math.sqrt(16) #PARA LA UTILIZACION DE FUNCIONES ESPECIFICAS DE ALGUNAS LIBRERIAS
raiz_cuadrada_2 = pow(16, (1/2))
raiz_cubica = pow(27, (1/3))

modulo_residuo_1 = 10 % 2 #EL MÓDULO ES EL RESIDULO DEL RESULTADO DE UNA DIVISIÓN
modulo_residuo_2 = numero_1 % numero_2

print("LA SUMA ES =",  suma) #concetenacion con ,
print('LA RESTA ES = ' + str(resta)) #CON 'str' SE CONVIERTE EN STRING LA VARIABLE RESTA (CASTEO)
print(f"LA MULTIPLICACION ES = {multiplicacion}") #INTERPOLACIÓN DE TEXTO 
print("LA DIVSION ES =", division)
print("LA POTENCIA1 DE n1 ELEVADO A LA n2 = ", potencia_1)
print("LA POTENCIA2 DE n1 ELEVADO A LA n2 = ", potencia_2)
print("LA RAIZ CUADRADA DE 16 ES = ", raiz_cuadrada_1)
print("MÓDULO O RESIDUO ES = ", modulo_residuo_1)
print("MÓDULO O RESIDUO ES = ", modulo_residuo_2)
