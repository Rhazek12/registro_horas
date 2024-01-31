import tkinter as tk
from tkinter import ttk
import csv
from datetime import datetime, timedelta
import os
import sys
import shutil

# Obtén la ruta al escritorio del usuario
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Construye la ruta al archivo 'registro_actividades.csv' en el escritorio
csv_registro = os.path.join(desktop_path, 'registro_actividades.csv')

# Verificar la existencia del directorio y crearlo si no existe
if not os.path.exists(desktop_path):
    os.makedirs(desktop_path)

# Verificar la existencia del archivo y crearlo si no existe
if not os.path.exists(csv_registro):
    with open(csv_registro, 'w', newline='') as file:
        writer = csv.writer(file)
        # Escribe la cabecera si es necesario
        writer.writerow(['nombre', 'fecha', 'hora', 'tipo'])

# Resto del código...

# Función para registrar la actividad
def registrar_actividad(nombre_dato, tipo):
    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")

    if nombre_dato != "":
        # Escribir en el archivo CSV
        with open(csv_registro, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([nombre_dato, fecha, hora, tipo])

def ultimo_registro(data_nombre):
    ultimo_registro = None
    with open(csv_registro, 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)

        for fila in lector_csv:
            nombre = fila[0]
            tipo = fila[3]

            if nombre == data_nombre:
                ultimo_registro = tipo

    return ultimo_registro

def calcular_horas_trabajadas(fecha_inicio, fecha_fin):
    lista_final = []
    with open(csv_registro, 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv, None)
        trabajadores = {}

        for fila in lector_csv:
            nombre = fila[0]
            fecha = fila[1]
            hora = fila[2]
            llegada = fila[3] == 'True'

            fecha_hora = datetime.strptime(f'{fecha} {hora}', '%Y-%m-%d %H:%M:%S')

            if nombre not in trabajadores:
                trabajadores[nombre] = {'entradas': [], 'salidas': [], 'horas_trabajadas': 0}
            if fecha_hora >= fecha_inicio and fecha_fin >= fecha_hora:
                if llegada:
                    trabajadores[nombre]['entradas'].append(fecha_hora)
                else:
                    trabajadores[nombre]['salidas'].append(fecha_hora)

    # Calcular el tiempo total trabajado para cada empleado
    for nombre, datos in trabajadores.items():
        total_tiempo_trabajado = timedelta()

        # Asegurarse de que haya entradas y salidas
        if len(datos['entradas']) == len(datos['salidas']):
            for entrada, salida in zip(datos['entradas'], datos['salidas']):
                tiempo_trabajado = salida - entrada
                total_tiempo_trabajado += tiempo_trabajado

            # Agregar el tiempo total trabajado al diccionario de datos
            datos['horas_trabajadas'] = total_tiempo_trabajado.total_seconds() / 3600  # Convertir a horas
            lista_final.append({'nombre': nombre, 'horas_trabajadas': round(datos["horas_trabajadas"], 2)})

    return lista_final
