import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    for i in range(100):
        page.controls.append(ft.TextButton(f'Test{i}'))
    
    page.scroll = "always"
    page.update()

ft.app(target=main)