import flet as ft
from logica.empleados_logic import *
from paginas.formulario_empleado_page import view_formulario
from logica.registro_logic import calcular_horas_trabajadas

def view_admin(page):

    if (page.window_maximizable == False):
        page.window_width = 800       # window's width is 200 px
        page.window_height = 600      # window's height is 200 px
        page.window_resizable = False # window is not resizable
        page.window_maximizable = True

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
    cv = ft.Column([dt],scroll=True,width=page.window_width - 100,alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,)
    rv = ft.Row([cv], scroll=ft.ScrollMode.ALWAYS, expand=1,vertical_alignment=ft.CrossAxisAlignment.START,alignment="center")
    

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
                rv,
                row,
            ],
        )
    )
    page.update()
