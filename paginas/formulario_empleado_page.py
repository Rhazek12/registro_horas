import flet as ft
from logica.empleados_logic import *


def view_formulario(page):
    txt_nombre = ft.TextField(value="nombre", text_align="center")
    txt_horas = ft.TextField(value="1", text_align="center")
    error = ft.Text(value="", color="RED")

    def minus_click(e):
        txt_horas.value = str(int(txt_horas.value) - 1)
        page.update()

    def plus_click(e):
        txt_horas.value = str(int(txt_horas.value) + 1)
        page.update()
    def crear(e):
        if txt_nombre.value != "" and txt_horas.value != "":
            agregar_empleado(txt_nombre.value,txt_horas.value)
            page.go("/admin")
        else:
            error.value = "Error: No se pueden dejar campos vacíos."
            page.update()
    def cancelar(e):
        page.go("/admin")

    row = ft.Row(
                [
                    ft.ElevatedButton("Crear", on_click=crear),
                    ft.ElevatedButton("Cancelar", on_click=cancelar),
                ],
                alignment="center"
            )
    row2 = ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    txt_horas,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ],
                alignment="center",
            )

    page.views.append(
        ft.View(
            "/formulario",
            [
                ft.AppBar(title=ft.Text("Formulario"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.Text("Nombre:"),
                txt_nombre,
                ft.Text("Horas:"),
                row2,
                row,
                error,
                

            ],
        )
    )
    page.update()
