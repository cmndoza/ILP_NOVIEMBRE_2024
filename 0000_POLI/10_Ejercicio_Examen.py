import time
import os

aciertos = int (0)
errores = int (0)

def Cintillo_general():
    print("*****Examen final de ILP******")
    print("Elija una de las opciones que se muestran, digitando la letra de la opción deseada")
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/")

def Pregunta_uno():
    os.system('cls')
    Cintillo_general()
    print("1. Herramienta de programación, parecido al lenguaje español utilizado para crear código.")
    print("a) IDE")
    print("b) Pseudocódigo")
    print("c) Compilador")
    print("d) ANSI / ISO") 

def Pregunta_dos():
    os.system('cls')
    Cintillo_general()
    print("2. Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados.")
    print("a) Información")
    print("b) Datos")
    print("c) Programa")
    print("d) Código") 

def Pregunta_tres():
    os.system('cls')
    Cintillo_general()
    print("3. Instituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo.")
    print("a) IEE")
    print("b) IDE")
    print("c) ANSI / ISO")
    print("d) VSCode") 

def Pregunta_cuatro():
    os.system('cls')
    Cintillo_general()
    print("2. Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados.")
    print("a) Información")
    print("b) Datos")
    print("c) Programa")
    print("d) Código") 

def Pregunta_cinco():
    os.system('cls')
    Cintillo_general()
    print("5. Conjunto de elementos que se relacionan para cumplir una función determinada.")
    print("a) Estructura")
    print("b) Datos")
    print("c) Operación")
    print("d) Sistema") 

def Pregunta_seis():
    os.system('cls')
    Cintillo_general()
    print("6. Componente de un IDE que se encarga de traducir el código fuente a código máquina.")
    print("a) Depurador")
    print("b) Editor de Texto")
    print("c) Terminal de Salida")
    print("d) Compilador/Intérprete") 

def Pregunta_siete():
    os.system('cls')
    Cintillo_general()
    print("7. Elemento que se usa para almacenar una cantidad donde cambia su valor.")
    print("a) Constante")
    print("b) Variable")
    print("c) Libreria")
    print("d) Tipo de Dato") 

def Pregunta_ocho():
    os.system('cls')
    Cintillo_general()
    print("8. Conjunto de símbolos, letras, números que no tienen un significado.")
    print("a) Datos")
    print("b) Estructura")
    print("c) Información")
    print("d) Sistema") 

def Pregunta_nueve():
    os.system('cls')
    Cintillo_general()
    print("9. Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento.")
    print("a) Filosofía")
    print("b) Sociología")
    print("c) Lógica")
    print("d) Argumentación") 

def Pregunta_diez():
    os.system('cls')
    Cintillo_general()
    print("10. Medida, patrón, modelo o norma universal para realizar una actividad o producir un objeto.")
    print("a) Evento")
    print("b) Estándar")
    print("c) Calidad")
    print("d) Productividad") 

def Pregunta_once():
    os.system('cls')
    Cintillo_general()
    print("11. Conjunto de elementos ordenados que componen y son la base de algo físico o no físico.")
    print("a) Estructura")
    print("b) Sistema")
    print("c) Objeto")
    print("d) Virtual") 

def Pregunta_doce():
    os.system('cls')
    Cintillo_general()
    print("12. Conjunto de instrucciones (código) que indican a la computadora tareas a realizar.")
    print("a) Operaciones/Cálculos")
    print("b) Sintaxis")
    print("c) Programa de Computadora")
    print("d) Comando") 


Cintillo_general()
time.sleep(3)
Pregunta_uno ()
respuesta = input("Digite la letra de la respuesta:")
if (respuesta == "b" or respuesta == "B"):
    aciertos = aciertos + 1
else:
    errores = errores + 1

Pregunta_dos ()
respuesta = input("Digite la letra de la respuesta:")
if (respuesta == "a" or respuesta == "A"):
    aciertos = aciertos + 1
else:
    errores = errores + 1

Pregunta_tres ()
respuesta = input("Digite la letra de la respuesta:")
if (respuesta == "c" or respuesta == "C"):
    aciertos = aciertos + 1
else:
    errores = errores + 1

Pregunta_cuatro ()
respuesta = input("Digite la letra de la respuesta:")
if (respuesta == "d" or respuesta == "D"):
    aciertos = aciertos + 1
else:
    errores = errores + 1

Pregunta_cinco ()
respuesta = input("Digite la letra de la respuesta:")
if (respuesta == "d" or respuesta == "D"):
    aciertos = aciertos + 1
else:
    errores = errores + 1

Pregunta_seis ()
respuesta = input("Digite la letra de la respuesta:")
if (respuesta == "d" or respuesta == "D"):
    aciertos = aciertos + 1
else:
    errores = errores + 1

Pregunta_siete ()
respuesta = input("Digite la letra de la respuesta:")
if (respuesta == "b" or respuesta == "B"):
    aciertos = aciertos + 1
else:
    errores = errores + 1

Pregunta_ocho ()
respuesta = input("Digite la letra de la respuesta:")
if (respuesta == "b" or respuesta == "B"):
    aciertos = aciertos + 1
else:
    errores = errores + 1

Pregunta_nueve ()
respuesta = input("Digite la letra de la respuesta:")
if (respuesta == "c" or respuesta == "C"):
    aciertos = aciertos + 1
else:
    errores = errores + 1

Pregunta_diez ()
respuesta = input("Digite la letra de la respuesta:")
if (respuesta == "d" or respuesta == "D"):
    aciertos = aciertos + 1
else:
    errores = errores + 1

Pregunta_once ()
respuesta = input("Digite la letra de la respuesta:")
if (respuesta == "b" or respuesta == "B"):
    aciertos = aciertos + 1
else:
    errores = errores + 1

Pregunta_doce ()
respuesta = input("Digite la letra de la respuesta:")
if (respuesta == "d" or respuesta == "D"):
    aciertos = aciertos + 1
else:
    errores = errores + 1
time.sleep(2)

calificacion = (aciertos / 12) * 10

os.system('cls')
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(1)
print("....")
time.sleep(1)
print(".....")
time.sleep(1)
print("......")
time.sleep(1)
print(".......")
time.sleep(1)

os.system('cls')
print("La prueba ha terminado, el resultado es el siguiente")
print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print("De un total de 12 preguntas ha acertado en", aciertos, "con" , errores,"errores, lo cual implica que su calificacion es", calificacion)

