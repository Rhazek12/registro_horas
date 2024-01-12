import flet as ft
from logica.empleados_logic import *
from paginas.formulario_empleado_page import view_formulario
from logica.registro_logic import calcular_horas_trabajadas

def view_admin(page):

    lista_opciones = obtener_empleados_horas()
    lista_rows = []
    for i in lista_opciones:
        nombre = str(i['nombre']) 
        horas = str(i['horas'])
        row_dt = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(nombre)),
                        ft.DataCell(ft.Text(horas)),
                    ],
                )
        lista_rows.append(row_dt)
    
    dt = ft.DataTable(
        columns=[
                ft.DataColumn(ft.Text("Nombre")),
                ft.DataColumn(ft.Text("Horas"), numeric=True),
            ],
            rows=lista_rows
    )
    

    row = ft.Row(
                [
                    ft.ElevatedButton("Agregar empleado", on_click=lambda _: page.go("/formulario")),
                    ft.ElevatedButton("Eliminar empleado", on_click=lambda _: page.go("/formulario2")),
                    ft.ElevatedButton("Horas Trabajadas", on_click=lambda _: page.go("/horas_trabajadas")),
                ],
                alignment="center"
            )
    page.views.append(

        ft.View(
            "/admin",
            [
                ft.AppBar(title=ft.Text("Panel del Administrador"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                ft.Text("Lista de empleados: ",size=30),
                dt,
                row,
            ],
        )
    )
    page.update()
