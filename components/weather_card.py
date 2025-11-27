import flet as ft
from utils.helpers import get_weather_icon, format_temperature, capitalize_first


class WeatherCard(ft.Column):
    def __init__(self):
        super().__init__()

        # Crear los controles como atributos de la clase
        self.city_title = ft.Text(
            "Selecciona una ciudad",
            size=24,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER
        )

        self.weather_icon = ft.Text("🌤️", size=60)
        self.temperature = ft.Text("--°C", size=48, weight=ft.FontWeight.BOLD)
        self.description = ft.Text("--", size=16)

        self.feels_like = ft.Text("--°C", size=16, weight=ft.FontWeight.BOLD)
        self.humidity = ft.Text("--%", size=16, weight=ft.FontWeight.BOLD)
        self.wind_speed = ft.Text("-- km/h", size=16, weight=ft.FontWeight.BOLD)

        # Aquí defines el contenido directamente
        self.controls = [
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        self.city_title,
                        ft.Divider(),

                        ft.Row([
                            ft.Column([self.weather_icon],
                                      horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            ft.Column([
                                self.temperature,
                                self.description,
                            ]),
                        ], alignment=ft.MainAxisAlignment.SPACE_AROUND),

                        ft.Divider(),

                        ft.Row([
                            ft.Column([
                                ft.Text("Sensación", size=12, color=ft.Colors.GREY_600),
                                self.feels_like,
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),

                            ft.Column([
                                ft.Text("Humedad", size=12, color=ft.Colors.GREY_600),
                                self.humidity,
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),

                            ft.Column([
                                ft.Text("Viento", size=12, color=ft.Colors.GREY_600),
                                self.wind_speed,
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                    ]),
                    padding=20,
                    border_radius=10,
                ),
                elevation=5,
            )
        ]

    def update_weather(self, weather_data):
        """Actualiza la tarjeta con datos del clima"""
        if not weather_data:
            return

        city_name = weather_data.get("name", "")
        country = weather_data.get("sys", {}).get("country", "")
        temp = weather_data.get("main", {}).get("temp", 0)
        feels_like = weather_data.get("main", {}).get("feels_like", 0)
        humidity = weather_data.get("main", {}).get("humidity", 0)
        wind_speed = weather_data.get("wind", {}).get("speed", 0)
        description = weather_data.get("weather", [{}])[0].get("description", "")
        icon_code = weather_data.get("weather", [{}])[0].get("icon", "")

        self.city_title.value = f"{city_name}, {country}"
        self.weather_icon.value = get_weather_icon(icon_code)
        self.temperature.value = format_temperature(temp)
        self.description.value = capitalize_first(description)
        self.feels_like.value = format_temperature(feels_like)
        self.humidity.value = f"{humidity}%"
        self.wind_speed.value = f"{wind_speed * 3.6:.1f} km/h"

        self.update()
