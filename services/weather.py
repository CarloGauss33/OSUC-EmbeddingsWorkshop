from Py_Weather import get_weather

def get_weather_info(city):
    """ This method gets the current weather info in the city """
    weather = get_weather(city)
    return weather