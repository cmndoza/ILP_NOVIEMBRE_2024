from datetime import datetime, timedelta

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

# Crear un delta de 10 días
#delta = timedelta(days=10)
