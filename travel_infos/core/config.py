import os
import dotenv


dotenv.load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

WEATHER_URL = os.environ.get("WEATHER_URL")
DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
RAPIDAPI_HOST = os.environ.get("RAPIDAPI_HOST")
RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")
