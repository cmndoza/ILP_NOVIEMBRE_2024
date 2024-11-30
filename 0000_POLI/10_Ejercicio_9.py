import random
import string
import os
from datetime import datetime, timedelta
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
    fecha_inicio_str = "01/05/2023"
    fecha_fin_str = "31/05/2023"
    fecha_inicio = datetime.strptime(fecha_inicio_str, "%d/%m/%Y")
    fecha_fin = datetime.strptime(fecha_fin_str, "%d/%m/%Y")
    #creación del valor correspondiente al día cero, formato delta, para poder operarse
    dia_cero = timedelta(days=1)
    # Calcular la diferencia en días
    extension_dias = (fecha_fin - fecha_inicio) + dia_cero
    # Convertir a entero
    extension_dias = int(extension_dias.days)
    pago = int(250)
    pago_mensual = pago * extension_dias
    #Para darle formato de moneda con dos decimales
    pago_formateado = f"${pago_mensual:.2f}"

    print("Con base en los días que tiene el mes trabajado,",extension_dias, " días, el pago correspondiente de nómina es:", pago_formateado)
    #print("Nómina")

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

while (respuesta == "si" or respuesta == "SI" or respuesta == "S" or respuesta == "s" or respuesta == "y" or respuesta == "Y"):
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

