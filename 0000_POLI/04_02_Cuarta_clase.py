#Funciones: tareas o acciones a ejecutar
#se tiene el nombre de la funcion *EN PYTHON DEBE ESTAR LA PRIMER LETRA EN MAYUSCULAS*
'''
define --> def Nombre_de_la_función (parametros o argumentos):
*sangria* contenido de la función
'''

def Operacion_Sumar (num1, num2): #significa que la funcion recibe u obtiene 2 parámetros o argumentos 
    #contenido de la función
    return num1 + num2 #devuelve, regresar, retornar un valor(es)
#si en la función se "suman" dos strings va a concatenar, si se suman dos valores numéricos los va a sumar

def Operacion_Restar (num1, num2):
    resta = num1 - num2 #No es necesario poner el Return
    print (resta)
#para invocar la función solo hace falta nombrarla 
'''En terminos generales como buena practica se recomienda usar el RETURN de forma usual'''


#FUNCION MULTIPLICAR 
def Operacion_Multiplicar (num1,num2):
    return num1 * num2

#FUNCION DIVIDIR
def Operacion_Dividir (num1,num2):
    return num1 / num2

fn1 = Operacion_Sumar(10,15.5)
fn2 = Operacion_Sumar("Dana","Paola")
Operacion_Restar (10,5)
fn3 = Operacion_Multiplicar(5,2)
fn4 = Operacion_Dividir(12,3)

print (fn1)
print (fn2)
print (fn3)
print (fn4)