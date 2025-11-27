import flet as ft


class SearchBar(ft.Row):
    def __init__(self, on_search):
        super().__init__()

        self.on_search = on_search
        self.alignment = ft.MainAxisAlignment.START

        # Campo de búsqueda
        self.search_field = ft.TextField(
            hint_text="Buscar ciudad...",
            prefix_icon=ft.Icons.SEARCH,
            on_submit=self.search_city,
            expand=True
        )

        # Botón de búsqueda
        self.search_button = ft.IconButton(
            icon=ft.Icons.SEARCH,
            on_click=self.search_city,
            tooltip="Buscar"
        )

        # Asignar controles al Row
        self.controls = [
            self.search_field,
            self.search_button
        ]

    def search_city(self, e):
        city = self.search_field.value.strip()
        if city:
            self.on_search(city)
