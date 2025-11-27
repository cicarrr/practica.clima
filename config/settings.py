import os
from dotenv import load_dotenv

load_dotenv()

# API Key gratuita de OpenWeatherMap (Current Weather Data API - GRATIS)
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "0ec1068543b38f4f3bb57d3067274b2d")

# URLs para API gratuita (Current Weather Data 2.5 - NO requiere suscripción)
BASE_URL = "https://api.openweathermap.org/data/2.5"
GEOCODING_URL = "https://api.openweathermap.org/geo/1.0"

# URLs para One Call API 3.0 (REQUIERE suscripción de pago)
# ONE_CALL_URL = "https://api.openweathermap.org/data/3.0/onecall"

# Configuración de la app
APP_TITLE = "Clima App"
DEFAULT_CITY = "Medellín"

