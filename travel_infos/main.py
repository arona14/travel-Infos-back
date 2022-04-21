from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from travel_infos.routes.test import test_router
from travel_infos.routes.weather import weather_router


app = FastAPI(title='Travel Infos')

ALLOWED_HOSTS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test_router, prefix='/test')
app.include_router(weather_router, prefix='/weather')
