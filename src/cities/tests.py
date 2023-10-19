from django.test import TestCase
from django.core.cache import cache

from cities.utils import get_weather_data


class CityTest(TestCase):
    fixtures = ['cities/fixtures/datas.json']

    def test_valid_city(self):
        """ Кейс: запрос погоды для существующего города """

        city = 'Рыбинск'

        datas = get_weather_data(city)
        self.assertIn('temp', datas, 'Нет данных по температуре')
        self.assertIn('pressure_mm', datas, 'Нет данных по давлению')
        self.assertIn('wind_speed', datas, 'Нет данных по скорости ветра')

        wkey = f'wd:{city.strip().lower()}'
        self.assertTrue(cache.get(wkey), 'Данные по городу не закешированы')

    def test_invalid_city(self):
        """ Кейс: запрос погоды для несуществующего города """

        city = 'nonononono'

        datas = get_weather_data(city)
        self.assertIn('error', datas, 'Нет сообщения об ошибке поиска по несуществующему городу')

        wkey = f'wd:{city.strip().lower()}'
        self.assertFalse(cache.get(wkey), 'Найдены закешированные данные по несуществующему городу')
