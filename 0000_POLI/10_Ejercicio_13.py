import random
import string
import os
from datetime import datetime, timedelta
#para presentar un menú
def Mostrar_Menu():
    print("******** MENÚ *********")
    print("a) Mostrar información del estado de Hidalgo")
    print("b) Mostrar información del estado de Oaxaca")
    print("c) Mostrar información del estado de México")
    print("d) Mostrar información del estado de Querétaro")
    print("d) Mostrar información de la Ciudad de México")

def Info_Hidalgo():
    print("La población del estado de Hidalgo es de 3.083 millones de habitantes")
    print("Cuenta con una extensión territorial de 20,821 km²")

def Info_Oaxaca():
    print("La población del estado de Hidalgo es de 4.132 millones de habitantes")
    print("Cuenta con una extensión territorial de 93,757 km²")

def Info_Edomex():
    print("La población del estado de Hidalgo es de 16.990 millones de habitantes")
    print("Cuenta con una extensión territorial de 22,351 km²")

def Info_Queretaro():
    print("La población del estado de Hidalgo es de 2.368 millones de habitantes")
    print("Cuenta con una extensión territorial de 11,699 km²")

def Info_CDMX():
    print("La población del estado de Hidalgo es de 9.209 millones de habitantes")
    print("Cuenta con una extensión territorial de 1,485 km²")


respuesta = "si"

while (respuesta == "si" or respuesta == "SI" or respuesta == "S" or respuesta == "s" or respuesta == "y" or respuesta == "Y"):
    #Para mostrar el menú se debe invocar la función:
    os.system('cls')
    Mostrar_Menu ()
    opcion = input("Elige una opción del menú: ")

    if (opcion == "a" or opcion == "A" or opcion == "a)" or opcion == "A)"):
        Info_Hidalgo()
    elif (opcion == "b" or opcion == "B" or opcion == "b)" or opcion == "B)"):
        Info_Oaxaca()
    elif (opcion == "c" or opcion == "C" or opcion == "c)" or opcion == "C)"):
        Info_Edomex()
    elif (opcion == "d" or opcion == "D" or opcion == "d)" or opcion == "D)"):
        Info_Queretaro()
    elif (opcion == "e" or opcion == "E" or opcion == "e)" or opcion == "E)"):
        Info_CDMX()
    else:
        print("Opción no válida")

    respuesta = input("¿Quiere obterner información de otro estado?: ")

