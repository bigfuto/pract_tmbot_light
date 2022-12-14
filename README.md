## Practicum python telegram bot light

Serverless Telegram бот на python для API Практикум.Домашка

работающий в Yandex Cloud Functions.

#### Что делает:

Запрашивает у API работы с timestamp минус 10 минут от текущего времени, если 

появилась работа, то отправляет сообщение в чат.

#### Как запустить:

В Cloud Functions нужно создать функцию, назвать ее, выбрать интерпритатор python. 

Далее нужно перенести файлы бота в созданную функцию:

`index.py` - основная функция.
`requirements.txt` - зависимости.

Для этого можно вручную в редакторе создать файлы и скопировать в них

содержимое или воспользоваться загрзкой zip архива (с диска или Object Storage).

Стоит обратить внимание на то, что при скачивании архива с github, файлы 

находятся в директории, а для установки зависимостей `requirements.txt`,

вероятно, должен быть в корне.

После загрузки файлов следует объявить переменные окружения и указать

точку входа, в данном случае - `index.main`.

Для проверки работоспособности можно перейти на вкладку `Тестирование` и запустить 

тест (шаблон и данные указывать не нужно), если результаты теста положительные,

то можно включить запуск приложения по расписанию.

Для этого нужно открыть вкладку `Триггеры`, создать триггер, указать название,

выбрать тип - `Таймер`, настроить таймер (cron выражение `*/10 * ? * * *`),

выбрать функцию и сервисный аккаунт (или создать, нажав на соответствующую кнопку).

После этого функция будет запускаться по настроенному таймеру.

Подробнее о Cloud Functions в [документации](https://cloud.yandex.ru/docs/functions/quickstart/)


#### Переменные окружения:

`PRACTICUM_TOKEN` - токен API Практикум.Домашка.

`TELEGRAM_TOKEN` - токен телеграм бота.

`TELEGRAM_CHAT_ID` - чат id.

`YP_ENDPOINT` - эндпоинт API Практикум.Домашка.
