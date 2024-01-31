import flet as ft
import csv
import os
import sys

base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Usa rutas relativas para acceder a tus archivos
csv_config = os.path.join(base_path, 'config.csv')
logo = os.path.join(base_path, 'logoASES.png')
def view_login(page):

    page.window_width = 500        # window's width is 200 px
    page.window_height = 600       # window's height is 200 px
    page.window_resizable = False  # window is not resizable
    page.window_maximizable = False
    img = ft.Image(
        src=logo,
        width=200,
        height=200,
    )
    row2 = ft.Row([img],alignment="center")
    txt_nombre = ft.TextField(value="" )
    txt_psswrd = ft.TextField(value="",password=True, can_reveal_password=True)
    error = ft.Text(value="", color="RED")

    def ingresar(e):
        with open(csv_config, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            validador = False
            for fila in lector_csv:
                nombre = fila[0]
                contrasena = fila[1]
                if txt_nombre.value == nombre and txt_psswrd.value == contrasena:
                    validador = True
        if validador:
            page.go("/admin")
            page.update()
        else:
            error.value = "Error: Contraseña o usuario erroneos."
            page.update()
    def cancelar(e):
        page.go("/")

    row = ft.Row(
                [
                    ft.ElevatedButton("Ingresar", on_click=ingresar),
                    ft.ElevatedButton("Cancelar", on_click=cancelar),
                ],
                alignment="center"
            )
    page.views.append(
        ft.View(
            "/login",
            [
                ft.AppBar(title=ft.Text("Login"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.Text("Nombre:"),
                txt_nombre,
                ft.Text("Contraseña:"),
                txt_psswrd,
                row,
                error,
                row2,

                
                

            ],

            horizontal_alignment="center"
        )
    )
    page.update()
