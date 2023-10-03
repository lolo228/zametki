import flet as ft

class Ui:
    def __init__(self, page: ft.Page):
        self.page = page

        self.page.add(
            ft.Column([
                ft.Row([
                    ft.FloatingActionButton(icon=ft.icons.ADD, text='Добавить заметку', on_click=self.add_note, expand=True)
                ], expand=True),
                ft.Row([
                    ft.TextField(label='Поиск', expand=True),
                    ft.IconButton(icon=ft.icons.SEARCH)
                ], expand=True),
                ft.Row([
                    ft.Container(
                    theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
                    theme_mode=ft.ThemeMode.DARK,
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    padding=10,
                    content=ft.Column([ft.Text("Header"), ft.Text("Some baze text asdfsdfsdfs;dflsdfsdf sdk fjs jsdflkj sdkfjs dlfkjsldfjsdkf jsdlkfj slkfj sldkfjskd jfslkdj flskjf sdlfjsdfkj skdjflskjdfksdfj lsdjf skldjf lskjdfklsdjfsldfjsldkfjsldfkj sdlkfj skfj sdf'jklfvndfjbndjfngkjdfngkdfgnj dfngjn")], scroll=ft.ScrollMode.ALWAYS, expand=True),
                    height=150,
                    width=250,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS_WITH_SAVE_LAYER,
                    border_radius=10
                    )
                ], wrap=True)
            ], expand=True)
        )

    def add_note(self, e):
        def close_dlg(e):
            self.dialog.open = False
            self.page.update()

        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Добавление записки"),
            content=ft.Column([
                ft.TextField(label="Заголовок записки"),
                ft.TextField(label="Текст записки"),
                ft.ElevatedButton(text="Создать", on_click=close_dlg)
            ])
        )

        self.page.dialog = self.dialog 
        self.dialog.open = True
        self.page.update()

def main(page: ft.Page):
    app = Ui(page)

ft.app(target=main)