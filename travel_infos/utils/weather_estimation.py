import re


def get_day_weather_prediction(pred):
    #pattern = re.compile("s(?P<hour>dd):dd:dd")
    #t = pattern.search(pred['dt_txt'])
    t = re.search(r'\d{2}:\d{2}:\d{2}', pred['dt_txt']).group()
    if int(t.split(':')[0]) >= 10 and int(t.split(':')[0]) <= 19:    
            return True
    return False

def get_day_weather(city_forecast):
    return list(filter(get_day_weather_prediction, city_forecast['list']))

def travel_estimator(day_weather):
    estimation = {}
    estimation['clear_sky_count'] = 0
    estimation['av_temp'] = 0
    for prediction in day_weather:
        estimation['av_temp'] += prediction['main']['temp']
        if prediction['weather'][0]['description'] in ['clear sky', 'few clouds']:
            estimation['clear_sky_count'] += 1
        estimation['av_temp'] = round(estimation['av_temp'] / len(day_weather), 2)
        estimation['av_temp_cels'] = round(estimation['av_temp'] - 273.15, 2)
    return estimation
