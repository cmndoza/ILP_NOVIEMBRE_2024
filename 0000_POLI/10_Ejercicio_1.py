import math
import statistics

calificacion_parcial_1 = 0
calificacion_parcial_2 = 0
calificacion_parcial_3 = 0
promedio_curso = 0

calificacion_parcial_1 = int(input("Calificacion 1 ="))
calificacion_parcial_2 = int(input("Calificacion 2 ="))
calificacion_parcial_3 = int(input("Calificacion 3 ="))
float (promedio_curso)

promedio_curso = statistics.mean([calificacion_parcial_1,calificacion_parcial_2,calificacion_parcial_3])

print("EL PROMEDIO DEL CURSO ES =", promedio_curso)
if promedio_curso > 6:
    print("EL ESTADO DEL CURSO ES: APROBADO")
else:
    print("EL ESTADO DEL CURSO ES: REPROBADO")
