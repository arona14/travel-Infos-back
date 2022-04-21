from fastapi import APIRouter
from travel_infos.services.weather import WeatherServices


weather_router = APIRouter()
service = WeatherServices()


@weather_router.get("/")
async def get_forecast(city: str, country: str = None):
    return service.get_weather(city=city, country=country)