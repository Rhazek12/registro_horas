import flet as ft
from logica.registro_logic import *
from logica.empleados_logic import obtener_empleados

def view_regsitro(page):
    lista_opciones = obtener_empleados()
    opciones = []
    error = ft.Text(value="", color="RED")
    for elemento in lista_opciones :
        opciones.append(ft.dropdown.Option(elemento))
    
    txt_nombre = ft.Dropdown(options= opciones)

    def ingreso(e):
        if txt_nombre.value == None :
            error.value = "Error: Debe seleccionar un nombre."
            page.update()
        else:
            if ultimo_registro(txt_nombre.value) == 'True':
                error.value = "Error: Su último registro tambien es un Ingreso, seleccione otra opción."
                page.update()
            else:
                registrar_actividad(txt_nombre.value,True)
                page.go("/")
                page.update()
            

    def salida(e):
        if txt_nombre.value == None :
            error.value = "Error: Debe seleccionar un nombre."
            page.update()
        else:
            if ultimo_registro(txt_nombre.value) == 'False' or ultimo_registro(txt_nombre.value) == None:
                error.value = "Error: Su último registro tambien es una Salida o no tiene registros, seleccione otra opción."
                page.update()
            else:
                registrar_actividad(txt_nombre.value,False)
                page.go("/")
                page.update()

    row = ft.Row(
                [
                    ft.ElevatedButton("Ingreso", on_click=ingreso),
                ft.ElevatedButton("Salida", on_click=salida),
                ],
                alignment="center"
            )
    page.views.append(
        ft.View(
            "/registro",
            [
                ft.AppBar(title=ft.Text("Registro"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                ft.Text("Selecciona tu Nombre: "),
                txt_nombre,
                row,
                error,
            ],
        )
    )
    page.update()
