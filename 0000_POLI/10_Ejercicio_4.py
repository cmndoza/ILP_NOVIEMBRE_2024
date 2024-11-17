import math

celsius = int (input("Ingrese el valor del grados Celsius que desea convertir = "))
kelvin = int (input("Ingrese el valor del grados Kelvin que desea convertir = "))
fahrenheit = int (input("Ingrese el valor del grados Fahrenheit que desea convertir = "))

de_celsius_a_kelvin = float (celsius + 273.15)
de_celsius_a_fahrenheit = float (((9*celsius)/5) + 32)

de_fahrenheit_a_celsius = float((5*(fahrenheit-32))/9)
de_fahrenheit_a_kelvin = float(((5*(fahrenheit-32))/9)+273.15)

de_kelvin_a_celsius = float(kelvin-273.15)
de_kelvin_a_fahrenheit = float((((kelvin-273.15)*9)/5)+32)

print(celsius,"GRADOS CENTIGRADOS EQUIVALEN A", de_celsius_a_kelvin,"GRADOS KELVIN")
print(celsius,"GRADOS CENTIGRADOS EQUIVALEN A", de_celsius_a_fahrenheit,"GRADOS FAHRENHEIT")
print(fahrenheit,"GRADOS CENTIGRADOS EQUIVALEN A", de_fahrenheit_a_celsius,"GRADOS CENTIGRADOS")
print(fahrenheit,"GRADOS CENTIGRADOS EQUIVALEN A", de_fahrenheit_a_kelvin,"GRADOS KELVIN")
print(kelvin,"GRADOS CENTIGRADOS EQUIVALEN A", de_kelvin_a_celsius,"GRADOS CENTIGRADOS")
print(kelvin,"GRADOS CENTIGRADOS EQUIVALEN A", de_kelvin_a_fahrenheit,"GRADOS FAHRENHEIT")