import requests
from config.settings import WEATHER_API_KEY, BASE_URL, GEOCODING_URL


class WeatherService:
    def __init__(self):
        self.api_key = WEATHER_API_KEY

    def get_coordinates(self, city_name):
        """Obtiene las coordenadas de una ciudad"""
        try:
            url = f"{GEOCODING_URL}/direct"
            params = {
                "q": city_name,
                "limit": 1,
                "appid": self.api_key
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            if data:
                return data[0]["lat"], data[0]["lon"]
            return None, None
        except Exception as e:
            print(f"Error obteniendo coordenadas: {e}")
            return None, None

    def get_weather(self, city_name):
        """Obtiene el clima actual de una ciudad"""
        try:
            lat, lon = self.get_coordinates(city_name)
            if not lat or not lon:
                return None

            url = f"{BASE_URL}/weather"
            params = {
                "lat": lat,
                "lon": lon,
                "appid": self.api_key,
                "units": "metric",
                "lang": "es"
            }

            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error obteniendo clima: {e}")
            return None

    def get_forecast(self, city_name, days=5):
        """Obtiene el pronóstico de varios días"""
        try:
            lat, lon = self.get_coordinates(city_name)
            if not lat or not lon:
                return None

            url = f"{BASE_URL}/forecast"
            params = {
                "lat": lat,
                "lon": lon,
                "appid": self.api_key,
                "units": "metric",
                "lang": "es"
            }

            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error obteniendo pronóstico: {e}")
            return None