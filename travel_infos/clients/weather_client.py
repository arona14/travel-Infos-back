import json
from travel_infos.clients.base_client import BaseClient
from travel_infos.core.config import RAPIDAPI_HOST, WEATHER_URL, RAPIDAPI_KEY



class WeatherClient(BaseClient):
    def __init__(self, end_point, rapid_api_host, rapid_api_key):
        super().__init__(end_point)
        self.rapid_api_host = rapid_api_host
        self.rapid_api_key = rapid_api_key
        self.read_headers = {"X-RapidAPI-Host": self.rapid_api_host, "X-RapidAPI-Key": self.rapid_api_key}
    
    def get_forecast(self, city: str, country: str = None):
        params = {}
        if country:
            params['q'] = city + ',' + country
        else:
            params['q'] = city
        response = self.get_request(f'/forecast', self.read_headers, params=params)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            error = response.content
            print(error)
            #raise ProjectError(error, 'Projects')

print('base url...', WEATHER_URL)
weather_client = WeatherClient(WEATHER_URL, RAPIDAPI_HOST, RAPIDAPI_KEY)
