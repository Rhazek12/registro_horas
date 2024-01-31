import csv
import os
import sys
import shutil

# Obtén la ruta al escritorio del usuario
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Construye la ruta a los archivos en el escritorio
csv_empleados_csv_original = os.path.join(desktop_path, 'empleados.csv')
csv_empleados_csv_temp = os.path.join(desktop_path, 'empleados_temp.csv')

# Verificar la existencia del directorio y crearlo si no existe
if not os.path.exists(desktop_path):
    os.makedirs(desktop_path)

# Verificar la existencia de los archivos y crearlos si no existen
if not os.path.exists(csv_empleados_csv_original):
    with open(csv_empleados_csv_original, 'w', newline='') as file:
        writer = csv.writer(file)
        # Escribe la cabecera si es necesario
        writer.writerow(['nombre', 'horas'])

if not os.path.exists(csv_empleados_csv_temp):
    with open(csv_empleados_csv_temp, 'w', newline='') as file:
        writer = csv.writer(file)
        # Escribe la cabecera si es necesario
        writer.writerow(['nombre', 'horas'])

# Función para registrar la actividad
def obtener_empleados():
    datos_lista = []

    with open(csv_empleados_csv_original, 'r') as file:
        lector_csv = csv.DictReader(file)
        
        # Iterar sobre las filas del CSV
        for fila in lector_csv:
            # Agregar la fila a la lista como un diccionario
            datos_lista.append(fila['nombre'])

    return datos_lista

def obtener_empleados_horas():
    datos_lista = []

    with open(csv_empleados_csv_original, 'r') as file:
        lector_csv = csv.DictReader(file)
        
        # Iterar sobre las filas del CSV
        for fila in lector_csv:
            # Agregar la fila a la lista como un diccionario
            datos_lista.append({
                'nombre': fila['nombre'],
                'horas': fila['horas']
            })

    return datos_lista

def agregar_empleado(nombre, horas):

    with open(csv_empleados_csv_original, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nombre, horas])

def eliminar_empleado(nombre):

    with open(csv_empleados_csv_original, 'r') as entrada, open(csv_empleados_csv_temp, 'w', newline='') as salida:
        lector_csv = csv.DictReader(entrada)
        campos = lector_csv.fieldnames

        escritor_csv = csv.DictWriter(salida, fieldnames=campos)
        escritor_csv.writeheader()

        for fila in lector_csv:
            # Omitir la fila que deseas eliminar
            if fila['nombre'] != nombre:
                escritor_csv.writerow(fila)

    # Reemplazar el archivo original con el nuevo archivo
    os.remove(csv_empleados_csv_original)
    os.rename(csv_empleados_csv_temp, csv_empleados_csv_original)
