import flet as ft
from logica.empleados_logic import *


def view_formulario2(page):
    lista_opciones = obtener_empleados()
    opciones = []

    for elemento in lista_opciones :
        opciones.append(ft.dropdown.Option(elemento))
    
    txt_nombre = ft.Dropdown(options= opciones)
    error = ft.Text(value="", color="RED",text_align="center")

    def eliminar(e):
        if txt_nombre.value != None:
            eliminar_empleado(txt_nombre.value)
            page.go("/admin")
        else:
            error.value = "Error: Debes seleccionar un empleado."
            page.update()
    def cancelar(e):
        page.go("/admin")
    
    row = ft.Row(
                [
                    ft.ElevatedButton("Eliminar", on_click=eliminar),
                    ft.ElevatedButton("Cancelar", on_click=cancelar),
                ],
                alignment="center"
            )

    page.views.append(
        ft.View(
            "/formulario2",
            [
                ft.AppBar(title=ft.Text("Formulario"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.Text("Selecciona un empleado:"),
                txt_nombre,
                row,
                error,
                

            ],
        )
    )
    page.update()
