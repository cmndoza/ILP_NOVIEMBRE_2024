import math

a = float(input("DETERMINE EL VALOR DE 'a' = "))
b = float(input("DETERMINE EL VALOR DE 'b' = "))
c = float(input("DETERMINE EL VALOR DE 'c' = "))

b_cuad = int(pow(b,2))

x_raiz = float(math.sqrt(b_cuad-(4*a*c)))

x_1 = float(((b*(-1))+x_raiz)/(2*a))
x_2 = float(((b*(-1))-x_raiz)/(2*a))

#x_1 = float(((-b)-math.sqrt(b**-(4*a*c)))/(2*a))
#x_2 = float(((-b)+math.sqrt(b**-(4*a*c)))/(2*a))

print ("EL VALOR DE x1 ES =",x_1)
print ("EL VALOR DE x2 ES =",x_2)
