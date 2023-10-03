import flet as ft

class Ui:
    def __init__(self, page: ft.Page):
        self.page = page

        self.rail = ft.NavigationRail(
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.ADD, text="Добавить"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.BOOKMARK,
                label="Заметки"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SEARCH,
                label='Поиск'
            )
        ],
        on_change=lambda e: self.rail_change(e.control.selected_index)
        )

        page.add(
        ft.Row(
            [
                self.rail,
                ft.VerticalDivider(width=1),
                ft.Column([ft.Container(
                    theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
                    theme_mode=ft.ThemeMode.DARK,
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    padding=10,
                    content=ft.Column([ft.Text("Header"), ft.Text("Some baze text asdfsdfsdfs;dflsdfsdf sdk fjs jsdflkj sdkfjs dlfkjsldfjsdkf jsdlkfj slkfj sldkfjskd jfslkdj flskjf sdlfjsdfkj skdjflskjdfksdfj lsdjf skldjf lskjdfklsdjfsldfjsldkfjsldfkj sdlkfj skfj sdf'jklfvndfjbndjfngkjdfngkdfgnj dfngjn")], scroll=ft.ScrollMode.ALWAYS, expand=True),
                    height=150,
                    width=250,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS_WITH_SAVE_LAYER,
                    border_radius=10
                )], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
            )
        )

    def rail_change(self, e):#Обработка мультистраничности
        if e == 0:
            self.page.views.append(
                ft.View(
                    "/notes",
                    [
                        ft.IconButton(icon=ft.icons.EXIT_TO_APP, on_click=self.view_close),
                        ft.Text("notes")
                    ]
                )
            )

            self.page.update()
            
        else:
            self.page.views.append(
                ft.View(
                    "/search",
                    [
                        ft.IconButton(icon=ft.icons.EXIT_TO_APP, on_click=self.view_close),
                        ft.Text("Search")
                    ]
                )
            )

            self.page.update()

    def view_close(self, e):#Обработка кнопки закрытия страницы
        self.page.views.pop()
        self.page.update()

def main(page: ft.Page):
    app = Ui(page)

ft.app(target=main)


# def create_navigation_rails(page):
#     rail = ft.NavigationRail(
#         selected_index=0,
#         label_type=ft.NavigationRailLabelType.ALL,
#         min_width=100,
#         min_extended_width=400,
#         leading=ft.FloatingActionButton(icon=ft.icons.ADD, text="Добавить"),
#         group_alignment=-0.9,
#         destinations=[
#             ft.NavigationRailDestination(
#                 icon=ft.icons.BOOKMARK,
#                 label="Заметки"
#             ),
#             ft.NavigationRailDestination(
#                 icon=ft.icons.SEARCH,
#                 label='Поиск'
#             )
#         ],
#         on_change=lambda e: Rail_change(e.control.selected_index, page)
#     )

#     return rail

# def back_view(page):
#     print(page.views)
#     page.views.clear()
#     page.update()
#     print('Я почистил views!')

# def Rail_change(e, page):
#     if e == 0:
#         page.views.append(
#             ft.View(
#                 "/notes",
#                 [
#                     ft.Text("notes")
#                 ]
#             )
#         )
#     else:
#         page.views.clear()
#         page.views.append(
#             ft.View(
#                 "/search",
#                 [
#                     ft.IconButton(icon=ft.icons.EXIT_TO_APP, on_click=lambda e: page.views.clear()),
#                     ft.Text("Search")
#                 ]
#             )
#         )

#     page.update()


# def main(page: ft.Page):
#     rail = create_navigation_rails(page)

#     page.add(
#         ft.Row(
#             [
#                 rail,
#                 ft.VerticalDivider(width=1),
#                 ft.Column([ft.Container(
#                     theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
#                     theme_mode=ft.ThemeMode.DARK,
#                     bgcolor=ft.colors.SURFACE_VARIANT,
#                     padding=10,
#                     content=ft.Column([ft.Text("Header"), ft.Text("Some baze text asdfsdfsdfs;dflsdfsdf sdk fjs jsdflkj sdkfjs dlfkjsldfjsdkf jsdlkfj slkfj sldkfjskd jfslkdj flskjf sdlfjsdfkj skdjflskjdfksdfj lsdjf skldjf lskjdfklsdjfsldfjsldkfjsldfkj sdlkfj skfj sdf'jklfvndfjbndjfngkjdfngkdfgnj dfngjn")], scroll=ft.ScrollMode.ALWAYS, expand=True),
#                     height=150,
#                     width=250,
#                     clip_behavior=ft.ClipBehavior.ANTI_ALIAS_WITH_SAVE_LAYER,
#                     border_radius=10
#                 )], alignment=ft.MainAxisAlignment.START, expand=True),
#             ],
#             expand=True,
#         )
#     )


# if __name__ == '__main__':
#     ft.app(target=main)