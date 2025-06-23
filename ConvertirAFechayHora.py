from datetime import datetime

def convertir_timestamp_microsegundos(timestamp_microsegundos):
    segundos = int(timestamp_microsegundos)
    microsegundos = int((timestamp_microsegundos - segundos) * 1_000_000)
    
    fecha_hora = datetime.utcfromtimestamp(segundos).replace(microsecond=microsegundos)
    fecha_hora_formateada = fecha_hora.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    return fecha_hora_formateada

# Ejemplo de uso con el timestamp 1705909862.437446
timestamp_microsegundos = 1705920700.215722
fecha_hora_legible = convertir_timestamp_microsegundos(timestamp_microsegundos)

print("Fecha y hora:", fecha_hora_legible)
