#Arreglos y listas
'''
nombre_Del_Arreglo = [elementos/valores]
'''

#ENTRADA DE DATOS 
nombres = ["Christopher", "Pablo", "Eduardo", "Carlos", "Paola"]
edades = [20,30,45,12,18]
arreglo_lista = [10, 5.7, "Hola", True]


#Proceso de modificación de arreglos
nombres[0] = "Christopher Chong Salazar"
edades[1] = 50
arreglo_lista[3] = False

nombres.append("Andrea")
edades.append(15)
arreglo_lista.append("ILP")

'''Ordenar elementos en el arreglo'''
nombres.sort()
edades.sort()

'''para limpiar los elementos de una lista'''
nombres.clear()

print(nombres)
print(edades)
print(arreglo_lista)