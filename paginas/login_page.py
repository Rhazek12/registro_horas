import flet as ft
import csv

def view_login(page):
    txt_nombre = ft.TextField(value="" )
    txt_psswrd = ft.TextField(value="",password=True, can_reveal_password=True)
    error = ft.Text(value="", color="RED")

    def ingresar(e):
        with open("config.csv", 'r') as archivo_csv:
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

                
                

            ],

            horizontal_alignment="center"
        )
    )
    page.update()
