import flet as ft
from services.weather_service import WeatherService
from components.weather_card import WeatherCard
from components.search_bar import SearchBar
from config.settings import APP_TITLE, DEFAULT_CITY


class WeatherApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.weather_service = WeatherService()
        self.weather_card = WeatherCard()

        self.setup_page()
        self.build_ui()

        # Cargar clima por defecto
        self.search_weather(DEFAULT_CITY)

    def setup_page(self):
        """Configura la página principal"""
        self.page.title = APP_TITLE
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 20
        self.page.scroll = ft.ScrollMode.ADAPTIVE

    def build_ui(self):
        """Construye la interfaz de usuario"""
        # Título de la app
        title = ft.Text(
            APP_TITLE,
            size=32,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER
        )

        # Barra de búsqueda
        search_bar = SearchBar(on_search=self.search_weather)

        # Indicador de carga
        self.loading = ft.ProgressRing(visible=False)

        # Mensaje de error
        self.error_mesagge = ft.Text(
            "",
            color=ft.Colors.RED,
            text_align=ft.TextAlign.CENTER,
            visible=False
        )

        # Agregar todos los controles a la página
        self.page.add(
            ft.Column([
                title,
                ft.Divider(),
                search_bar,
                ft.Container(
                    content=self.loading,
                    alignment=ft.alignment.center,
                    height=50
                ),
                self.error_message,
                self.weather_card,
            ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20)
        )

    def search_weather(self, city_name):
        """Busca el clima de una ciudad"""
        self.show_loading(True)
        self.hide_error()

        # Obtener datos del clima
        weather_data = self.weather_service.get_weather(city_name)

        if weather_data:
            self.weather_card.update_weather(weather_data)
        else:
            self.show_error(f"No se pudo obtener el clima de '{city_name}'. Verifica el nombre de la ciudad.")

        self.show_loading(False)

    def show_loading(self, show):
        """Muestra/oculta el indicador de carga"""
        self.loading.visible = show
        self.page.update()

    def show_error(self, message):
        """Muestra un mensaje de error"""
        self.error_message.value = message
        self.error_message.visible = True
        self.page.update()

    def hide_error(self):
        """Oculta el mensaje de error"""
        self.error_message.visible = False
        self.page.update()


def main(page: ft.Page):
    WeatherApp(page)


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port=8550)