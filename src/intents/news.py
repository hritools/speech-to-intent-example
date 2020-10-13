from . import BaseIntent
from .slots.news_category import NewsCategorySlot


class NewsIntent(BaseIntent):
    KEYWORD = 'news'

    @staticmethod
    def help_text():
        return 'новости'

    @staticmethod
    def get_keywords():
        return ['новости']

    @staticmethod
    def get_slots():
        return [NewsCategorySlot]