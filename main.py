import flet as ft
from paginas.login_page import view_login
from paginas.registro_page import view_regsitro
from paginas.admin_page import view_admin
from paginas.principal_page import view_principal
from paginas.formulario_empleado_page import view_formulario
from paginas.formulario_empleado2_page import view_formulario2
from paginas.calcular_horas_page import view_horas_trabajadas


def main(page: ft.Page):
    page.title = "Registro de Horas"

    def route_change(route):
        page.views.clear()
        
        if page.route == "/":
            view_principal(page)
        if page.route == "/login":
            view_login(page)
        if page.route == "/registro":
            view_regsitro(page)
        if page.route == "/admin":
            view_admin(page)
        if page.route == "/formulario":
            view_formulario(page)
        if page.route == "/formulario2":
            view_formulario2(page)
        if page.route == "/horas_trabajadas":
            view_horas_trabajadas(page)
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)