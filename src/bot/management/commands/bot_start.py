import json

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CallbackQueryHandler, Defaults

from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.cache import cache

from cities.utils import get_weather_data


class Command(BaseCommand):

    def handle(self, *args, **options):
        updater = Updater(settings.TELEGRAM__TOKEN, defaults=Defaults(run_async=True))

        updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
        updater.dispatcher.add_handler(CallbackQueryHandler(echo_inline))

        updater.start_polling()
        updater.idle()


def echo(update: Update, context: CallbackContext):
    """ Обработка текстовой команды """

    c_key = f'c:{update.effective_chat.id}'

    if update.message.text == '/start':
        text = 'Бот может подсказать погоду в вашем городе'

    elif cache.get(c_key):
        cache.delete(c_key)
        datas = get_weather_data(update.message.text)
        text = datas['error'] if datas.get('error') else f'Температура {datas["temp"]}°C\n' \
                                                         f'Давление {datas["pressure_mm"]} мм рт. ст.\n' \
                                                         f'Скорость ветра {datas["wind_speed"]}  м/с'
    else:
        return

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(
                text='Узнать погоду',
                callback_data=json.dumps({'ask_w': 1}))
            ]]))


def echo_inline(update: Update, context: CallbackContext):
    """ Обработка нажатия Inline-кнопки """

    if json.loads(update.callback_query.data).get('ask_w') == 1:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Напишите название вашего города')
        cache.set(f'c:{update.effective_chat.id}', 1, 1800)
