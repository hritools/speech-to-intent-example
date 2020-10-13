from enum import Enum


class NewsCategory(Enum):
    BUSINESS = 'business'
    ENTERTAINMENT = 'entertainment'
    GENERAL = 'general'
    HEALTH = 'health'
    SCIENCE = 'science'
    SPORTS = 'sports'
    TECHNOLOGY = 'technology'


class NewsCategorySlot:
    _VALUES = [item.value for item in NewsCategory]
    _KW_BY_VALUE = {
        NewsCategory.TECHNOLOGY: ['it', 'айти', 'технология'],
        NewsCategory.SCIENCE: ['наука'],
        NewsCategory.SPORTS: ['спорт'],
    }

    def __init__(self, value):
        self.value = value if value in NewsCategorySlot._VALUES else None

    @staticmethod
    def get_values():
        return NewsCategorySlot._VALUES

    @staticmethod
    def get_keywords_by_value(value):
        kws = NewsCategorySlot._KW_BY_VALUE.get(NewsCategory(value)) or []
        return kws

    @staticmethod
    def get_regexes_by_value(value):
        return []