def get_weather_icon(weather_code):
    """Devuelve un emoji según el código del clima"""
    weather_icons = {
        "01d": "☀️", "01n": "🌙",
        "02d": "⛅", "02n": "☁️",
        "03d": "☁️", "03n": "☁️",
        "04d": "☁️", "04n": "☁️",
        "09d": "🌧️", "09n": "🌧️",
        "10d": "🌦️", "10n": "🌧️",
        "11d": "⛈️", "11n": "⛈️",
        "13d": "❄️", "13n": "❄️",
        "50d": "🌫️", "50n": "🌫️"
    }
    return weather_icons.get(weather_code, "🌤️")

def format_temperature(temp):
    """Formatea la temperatura"""
    return f"{int(temp)}°C"

def capitalize_first(text):
    """Capitaliza la primera letra"""
    return text.capitalize() if text else ""