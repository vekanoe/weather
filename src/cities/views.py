from django.http import JsonResponse

from cities.utils import get_weather_data


def weather(request):
    return JsonResponse(get_weather_data(request.GET.get('city', None)), json_dumps_params={'ensure_ascii': False})
