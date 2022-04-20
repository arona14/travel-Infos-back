from fastapi import APIRouter
from travel_infos.services.weather import WeatherServices


test_router = APIRouter()
service = WeatherServices()


@test_router.get("/")
async def get_forecast(city: str, country: str):
    return service.get_forecast(city=city, country=country)