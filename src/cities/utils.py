import requests

from django.core.cache import cache
from django.conf import settings

from cities.models import City


def get_weather_data(city: str) -> dict:
    """ Получение данных о погоде по наименованию города """

    if not city:
        return {'error': 'Укажите город'}

    cache_timeout = 1800  # 30 минут

    wkey = f'wd:{city.strip().lower()}'
    cdata = cache.get(wkey)

    if cdata:
        return cdata

    try:
        city_obj = City.objects.get(title__iexact=city)

        # используется тариф "Погода на вашем сайте"
        resp = requests.get(
            f'https://api.weather.yandex.ru/v2/informers?lat={city_obj.lat}&lon={city_obj.lon}&lang=ru_RU',
            headers={'X-Yandex-API-Key': settings.X_YANDEX_API_KEY})

        weather_data = resp.json()
        cdata = {
            'temp': weather_data['fact']['temp'],
            'pressure_mm': weather_data['fact']['pressure_mm'],
            'wind_speed': weather_data['fact']['wind_speed'],
        }

    except Exception:
        return {'error': f'Данные по городу {city} не найдены'}

    cache.set(wkey, cdata, cache_timeout)
    return cdata
