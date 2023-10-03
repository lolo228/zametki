import flet as ft

def create_navigation_rails():
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        height=400,
        leading=ft.FloatingActionButton(icon=ft.icons.ADD, text='Добавить'),
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.NOTE, label='Заметки'),
            ft.NavigationRailDestination(icon=ft.icons.SEARCH, label='Поиск')
        ]
    )

    return rail

def main(page: ft.Page):
    rail = create_navigation_rails()

    page.add(ft.Row([rail, ft.VerticalDivider(width=1, color=ft.colors.GREY_50), ft.Column([ft.Text("Test!")])]))

if __name__ == '__main__':
    ft.app(target=main)