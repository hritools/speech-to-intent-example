__all__ = ('generate', )


import random

from .api import Weather
from utils.text import word_ending_by_number


_PLUS_TEMP_PHRASES = ('{temp} градус{ending} выше нуля', '{temp} градус{ending} тепла', 'плюс {temp}')
_MINUS_TEMP_PHRASES = ('{temp} градус{ending} ниже нуля', '{temp} градус{ending} мороза', 'минус {temp}')
_ZERO_TEMP_PHRASES = ('{temp} градус{ending}', 'около нуля')


def generate(weather :Weather) -> str:
    temperature = int(weather.get_temperature()['temp'] - 273.15)
    status = weather.get_detailed_status()
    temp_phrase = _choose_temp_phrase(temperature)
    return f'{temp_phrase}. \n {status}.\n'


def _choose_temp_phrase(temp :int) -> str:
    if temp > 0:
        phrases = _PLUS_TEMP_PHRASES
    elif temp < 0:
        phrases = _MINUS_TEMP_PHRASES
    else:
        phrases = _ZERO_TEMP_PHRASES

    phrase = random.choice(phrases).format(temp=temp, ending=word_ending_by_number(temp))
    return phrase