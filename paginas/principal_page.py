import flet as ft

def view_principal(page):

    row = ft.Row(
                [
                    ft.ElevatedButton("Admin", on_click=lambda _: page.go("/login")),
                    ft.ElevatedButton("Registro", on_click=lambda _: page.go("/registro")),
                ],
                alignment="center"
            )
    page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text(""), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.Text("Bienvenido!",size=40),
                    row
                ],
                horizontal_alignment="center"
            ),
        )
    page.update()
