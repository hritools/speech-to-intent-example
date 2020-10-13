__all__ = ('get_weather',)


from . import api
from . import text_gen


def get_weather() -> str:
    weather = api.get_weather()
    text = text_gen.generate(weather)
    return text
