import random
import string
import os
#para presentar un menú
def Mostrar_Menu():
    print("******** MENÚ *********")
    print("a) Mostrar una lista de 3 servicios de pasaje con sus estrellas de calificación")
    print("b) Calcular la nómina de un empleado en ENERO del 2024")
    print("c) Generar una contraseña con el número de caracteres pedidos menor o igual a 5, si es mayor que 5 mostrar mensaje de error")
    print("d) Pedir al usuario su nombre, primer ap., segundo ap. y edad e imprimir un saludo con sus datos")

def Lista_Transportes():
    Lista_pasajes = ["Metro","Avión","Metrobús"]
    Lista_calificaciones = [3,4,5]
    print(Lista_pasajes, Lista_calificaciones)

def Calcular_Nomina ():
    print("Nómina")

def Generar_contraseña(numero_caracteres):
    if (numero_caracteres <= 5):
        longitud_contraseña = string.ascii_letters + string.digits + string.punctuation
        #contraseña = "12345"
        contraseña = ''.join(random.choice(longitud_contraseña) for _ in range(numero_caracteres))
        return contraseña
        #Generar la contraseña
    elif (numero_caracteres > 5):
        return "ERROR"
        #print("ERROR de captura")

def Saludo_Bienvenida ():
    nombre = str(input("Introduzca su nombre: "))
    primer_apellido = str(input("Introduzca su primer apellido: "))
    segundo_apellido = str(input("Introduzca su segundo apellido: "))
    edad = str(input("Introduzca su Edad: "))
    print ("Estimado " + nombre + " " + primer_apellido + " " + segundo_apellido + " con base en tu edad, " + edad + " años, puedes tener acceso a ...")


respuesta = "si"

while (respuesta == "si" or respuesta == "SI" or respuesta == "S" or respuesta == "s"):
    #Para mostrar el menú se debe invocar la función:
    os.system('cls')
    Mostrar_Menu ()
    opcion = input("Elige una opción del menú: ")

    if (opcion == "a" or opcion == "A" or opcion == "a)" or opcion == "A)"):
        Lista_Transportes()
    elif (opcion == "b" or opcion == "B" or opcion == "b)" or opcion == "B)"):
        Calcular_Nomina()
    elif (opcion == "c" or opcion == "C" or opcion == "c)" or opcion == "C)"):
        longitud_contraseña = int(input("¿Cuántos caracteres?"))
        print(Generar_contraseña(longitud_contraseña))
    elif (opcion == "d" or opcion == "D" or opcion == "d)" or opcion == "D)"):
        Saludo_Bienvenida()
    else:
        print("Opcioón on válida")

    respuesta = input("¿Quieres continuar?: ")

