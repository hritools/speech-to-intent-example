__all__ = ('get_weather', )


import pyowm
from pyowm.weatherapi25.weather import Weather


_API_KEY = '774d408e2edaf12b9e9e64585c64b545'


def get_weather() -> Weather:
    try:
        owm = pyowm.OWM(_API_KEY, language='ru')
        observation = owm.weather_at_place('Innopolis,RU')
        weather = observation.get_weather()
        return weather
    except Exception:
        return None


if __name__ == '__main__':
    get_weather()