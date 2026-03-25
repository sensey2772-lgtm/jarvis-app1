import flet as ft

def main(page: ft.Page):
    page.title = "Jarvis Test"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.Row(
            [ft.Text("Приложение Jarvis работает!", size=25, color="blue")],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
