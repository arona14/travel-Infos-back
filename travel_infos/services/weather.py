from travel_infos.clients.weather_client import weather_client
from travel_infos.utils.weather_estimation import get_day_weather, travel_estimator


class WeatherServices:
    
    @staticmethod
    def get_forecast(city: str, country: str):
        return weather_client.get_forecast(city, country)

    @staticmethod
    def get_weather(city: str, country: str = None):
        forecast_data = weather_client.get_forecast(city, country)
        day_weather = get_day_weather(forecast_data)
        travel_rating = travel_estimator(day_weather)
        return travel_rating
