#pedir el nivel de agua de un tinaco y devolver un mensaje con base en la respuesta
nivel_de_agua = int(input("Indique el nivel de agua: "))

if nivel_de_agua < 0:
    print("FUGA EN CISTERNA DE AGUA")
elif nivel_de_agua == 0:
    print("ENCENDER BOMBA DE AGUA")
elif nivel_de_agua > 0 and nivel_de_agua <= 2:
    print("ACELERAR BOMBA DE AGUA")
elif nivel_de_agua > 2 and nivel_de_agua <= 4:
    print("BOMBA TRABAJADNO")
elif nivel_de_agua > 4 and nivel_de_agua < 6:
    print("DESACELERAR BOMBA")
elif nivel_de_agua == 6:
    print("APAGAR BOMBA DE AGUA")
elif nivel_de_agua > 6:
    print("DESBORDAMIENTO DE AGUA EN CISTERNA")
else:
    print ("VALOR INVÁLIDO, FAVOR DE VERIFICAR")
