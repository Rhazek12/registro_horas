import csv
import os




# Función para registrar la actividad
def obtener_empleados():

    datos_lista = []

    with open("empleados.csv", 'r') as file:
        lector_csv = csv.DictReader(file)
        
        # Iterar sobre las filas del CSV
        for fila in lector_csv:
            # Agregar la fila a la lista como un diccionario
            datos_lista.append(fila['nombre'])

    return datos_lista

def obtener_empleados_horas():

    datos_lista = []

    with open("empleados.csv", 'r') as file:
        lector_csv = csv.DictReader(file)
        
        # Iterar sobre las filas del CSV
        for fila in lector_csv:
            # Agregar la fila a la lista como un diccionario
            datos_lista.append({
                'nombre':fila['nombre'],
                'horas':fila['horas']
                })

    return datos_lista

def agregar_empleado(nombre, horas):

    with open("empleados.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([nombre, horas])

def eliminar_empleado(nombre):

    with open("empleados.csv", 'r') as entrada, open("empleados_temp.csv", 'w', newline='') as salida:
        lector_csv = csv.DictReader(entrada)
        campos = lector_csv.fieldnames

        escritor_csv = csv.DictWriter(salida, fieldnames=campos)
        escritor_csv.writeheader()

        for fila in lector_csv:
            # Omitir la fila que deseas eliminar
            if fila['nombre'] != nombre:
                escritor_csv.writerow(fila)

    # Reemplazar el archivo original con el nuevo archivo
    os.remove("empleados.csv")
    os.rename("empleados_temp.csv", "empleados.csv")
