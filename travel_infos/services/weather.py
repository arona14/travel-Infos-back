from travel_infos.clients.weather_client import weather_client


class WeatherServices:
    
    @staticmethod
    def get_forecast(city: str, country: str):
        return weather_client.get_forecast(city, country)
