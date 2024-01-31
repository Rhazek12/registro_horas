import flet as ft
import os
import sys

base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
logo = os.path.join(base_path, 'logoASES.png')
def view_principal(page):

    page.window_width = 500        # window's width is 200 px
    page.window_height = 600       # window's height is 200 px
    page.window_resizable = False  # window is not resizable
    page.window_maximizable = False
    page.theme = ft.theme.Theme(color_scheme_seed='RED')
    # page.window_resizable = False  # window is not resizable
    img = ft.Image(
        src=logo,
        width=400,
        height=400,
    )
    row = ft.Row(
                [
                    ft.ElevatedButton("Admin", on_click=lambda _: page.go("/login")),
                    ft.ElevatedButton("Registro", on_click=lambda _: page.go("/registro")),
                ],
                alignment="center"
            )
    row2 = ft.Row([img],alignment="center")

    page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text(""), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.Text("Bienvenido!",size=40),
                    row,
                    row2
                ],
                horizontal_alignment="center"
            ),
        )
    page.update()
