import flet as ft
from logica.empleados_logic import *
from paginas.formulario_empleado_page import view_formulario
from logica.registro_logic import calcular_horas_trabajadas
from datetime import datetime


def view_horas_trabajadas(page):

    dt = ft.DataTable()
    date_picker_inicio = ft.DatePicker(
        value=datetime.strptime('2024-01-1 00:00:00', '%Y-%m-%d %H:%M:%S'),
        first_date=datetime(2024, 1, 1),
    )
    date_picker_fin = ft.DatePicker(
        value=datetime.strptime('2030-01-1 00:00:00', '%Y-%m-%d %H:%M:%S'),
        first_date=datetime(2024, 1, 1),
    )
    page.overlay.append(date_picker_inicio)
    page.overlay.append(date_picker_fin)
    date_button_inicio = ft.ElevatedButton(
        "Pick Date",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: date_picker_inicio.pick_date(),
    )
    date_button_fin = ft.ElevatedButton(
        "Pick Date",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: date_picker_fin.pick_date(),
    )

    def funcion_grande():
       lista_rows = []
       list_horas = calcular_horas_trabajadas(date_picker_inicio.value,date_picker_fin.value)
       for i in list_horas:
        nombre = str(i['nombre']) 
        horas = str(i['horas_trabajadas'])
        row_dt = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(nombre)),
                        ft.DataCell(ft.Text(horas)),
                    ],
                )
        lista_rows.append(row_dt)
    
        dt.columns =[
                    ft.DataColumn(ft.Text("Nombre")),
                    ft.DataColumn(ft.Text("Horas Trabajadas"), numeric=True),
                ]
        dt.rows=lista_rows
        page.update()


    row = ft.Row(
                [
                    ft.ElevatedButton("calcular horas", on_click=lambda _:funcion_grande()),
                    ft.ElevatedButton("Volver", on_click=lambda _: page.go("/admin")),
                ],
                alignment="center"
            )
    row2 = ft.Row(
                [
                    ft.Text("Fecha Inicio: ",size=20),
                    date_button_inicio,
                ],
            )
    row3 = ft.Row(
                [
                    ft.Text("Fecha Fin: ",size=20),
                    date_button_fin,
                ],
            )
    page.views.append(

        ft.View(
            "/horas_trabajadas",
            [
                ft.AppBar(title=ft.Text("Contador de Horas"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                ft.Text("Selecciona los límites: ",size=30),
                row2,
                row3,
                row,
                dt,
            ],
        )
    )
    page.update()
