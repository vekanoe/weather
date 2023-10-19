#### Разворот приложения:

перейти в папку с файлами установки
 
    cd weather/deploy


создать файл со значениями переменных окружения

    cp .env.dist .env
    
    
В файле .env отредактируйте параметры подключения к базам данных по необходимости и обязательно укажите:

    X_YANDEX_API_KEY - ключ доступа к API Яндекс.Погоды, тариф "Погода на вашем сайте"
    TELEGRAM__TOKEN - токен вашего бота в Telegram 


создать/запустить контейнеры

    docker-compose up -d  --build


#### Предустановленные данные

С помощью django-команды load_cities в базу загружен справочник городов и их координат. 


#### Эндпойнт API:

/weather?city=<city_name> - данные по погоде указаного в <city_name> города
    

#### Запуск Telegram-бота:

Бот стартует автоматически вместе со всем проектом с помощью команды bot_start.


#### Запуск тестов:

docker-compose exec web python manage.py test
