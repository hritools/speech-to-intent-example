from io import BytesIO

import speech_recognition as sr

from speechtointents.speechtointents import SpeechToTextToIntentSimple
from speechtointents.intents.tell import Weather, WhatYouCan
from intents.news import NewsIntent as News
from intents.slots.news_category import NewsCategorySlot

from pyrhvoice import RHVoice

from news import get_headlines
from weather import get_weather


def main():
    speech_to_intents = SpeechToTextToIntentSimple([WhatYouCan, News, Weather])

    rhvoice = RHVoice(default_voice='irina')

    rcgn = sr.Recognizer()
    with sr.Microphone() as mic:
        rcgn.adjust_for_ambient_noise(mic)
    
    while True:
        with sr.Microphone() as mic:
            audio = BytesIO(rcgn.listen(mic).get_wav_data())
        intent = speech_to_intents.parse(sr.AudioFile(audio))
        print(type(intent))
        print(intent.concrete_slots[0].value)
        if isinstance(intent, WhatYouCan):
            intent.help_text = speech_to_intents.help_text()

        handler = _handlers.get(type(intent))
        if handler:
            text = handler(intent)
            rhvoice.play(text)


def handle_help(intent):
    return 'Я могу рассказать вам ' + intent.help_text

def handle_weather(intent):
    weather = get_weather()
    return weather


def handle_news(intent):
    category = None
    for slot in intent.concrete_slots:
        if isinstance(slot, NewsCategorySlot):
            category = slot.value
            break

    headlines = get_headlines(category)
    text = '.\n\n'.join(headlines)
    return text

_handlers = {
    WhatYouCan: handle_help,
    News: handle_news,
    Weather: handle_weather,
}



if __name__ == '__main__':
    main()