import flet as ft
from DataWork import DataStore


class Ui:

    def __init__(self, page: ft.Page):

        # Создаём экземпляр класса, для работы с базой данных
        self.data_store = DataStore()

        all_notes = self.data_store.get_table_data()

        # Создаём список с контейнерами/заметками
        notes_list = []
 
        if all_notes != []:
            for note in all_notes:
                contain = self.create_note_container(note[0], note[1])

                notes_list.append(contain)

        # Инициализируем страницу | список заметок | Поле для поиска
        self.page = page 

        self.notes_space = ft.Row(notes_list, wrap=True)

        self.search_field = ft.TextField(label='Поиск', expand=True)

        # Добавляем в страницу все элементы
        self.page.add(
            ft.Column([
                ft.Row([
                    ft.FloatingActionButton(icon=ft.icons.ADD, text='Добавить заметку', on_click=self.add_note_button_handler, expand=True)
                ], expand=True),
                ft.Row([
                    self.search_field,
                    ft.IconButton(icon=ft.icons.SEARCH, on_click=self.notes_search)
                ], expand=True),
                self.notes_space
            ], expand=True)
        )

    def create_note_container(self, header, body):
        # Функция для создания контейнеров/div`ов

        return ft.Container(
                    theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
                    theme_mode=ft.ThemeMode.DARK,
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    padding=10,
                    content=ft.Column([
                        ft.Row([
                            ft.Text(header, size=15, weight=ft.FontWeight.W_500),
                            ft.PopupMenuButton(
                                items=[ft.PopupMenuItem(
                                    icon=ft.icons.DELETE,
                                    text="Удалить",
                                    on_click=lambda e: self.delete_note(e, header)
                                )]
                        )], scroll=ft.ScrollMode.ALWAYS),
                        ft.Text(body)
                    ], scroll=ft.ScrollMode.ALWAYS),
                    height=150,
                    width=250,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS_WITH_SAVE_LAYER,
                    border_radius=10,
                    data=header
                )
    
    def delete_note(self, e, note_header):
        # Функция для удаления заметок

        self.data_store.remove_note(note_header)

        # Ищем нужный контейнер для удаления
        for contain in self.notes_space.controls:
            if contain.data == note_header:
                self.notes_space.controls.remove(contain)

        self.page.update()

    def notes_search(self, e):
        # Функция для поиска заметок

        keywoard = self.search_field.value
        
        found_notes = self.data_store.search_note(keywoard)

        self.notes_space.controls.clear()

        # Создаём список с найденными заметками
        for notes in found_notes:
            contain = self.create_note_container(notes[0], notes[1])

            self.notes_space.controls.append(contain)

        self.page.update()

    def alert_banner(self):
        # Функция для создания и обработки действий баннера

        def close_banner(e):
            self.page.banner.open = False,
            self.page.update()

        banner = ft.Banner(
            bgcolor=ft.colors.AMBER_100,
            leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
            content=ft.Text("Ошибка, нельзя создать заметку с пустой строкой!", color=ft.colors.BLACK),
            actions=[
                ft.TextButton("OK", on_click=close_banner)
            ]
        )

        # Открываем баннер
        self.page.banner = banner
        self.page.banner.open = True
        self.page.update()

    def add_note_button_handler(self, e):
        # Обработка кнопки добавления новых заметок

        # Обработка кнопки создания заметки
        def create_button_handler(e):
            note_header = header_field.value
            note_body = body_field.value

            if not (note_header and note_body):
                dialog.open = False
                self.page.update()

                self.alert_banner()

            else:
                self.data_store.add_note([note_header, note_body])

                note_container = self.create_note_container(note_header, note_body)

                self.notes_space.controls.append(note_container)

                dialog.open = False
                self.page.update()

        header_field = ft.TextField(label="Заголовок заметки")
        body_field = ft.TextField(label="Текст заметки")

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Добавление заметки"),
            content=ft.Column([
                header_field,
                body_field,
                ft.ElevatedButton(text="Создать", on_click=create_button_handler)
            ], expand=True)
        )

        self.page.dialog = dialog 
        dialog.open = True
        self.page.update()


def main(page: ft.Page):
    app = Ui(page)


if __name__ == '__main__':
    ft.app(target=main)
