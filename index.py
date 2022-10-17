import os
import telegram
import requests
import time

from dotenv import load_dotenv

load_dotenv()

CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN'))

HEADERS = {'Authorization': f'OAuth {os.getenv("PRACTICUM_TOKEN")}'}
YP_ENDPOINT = os.getenv('YP_ENDPOINT')


def main(event, context):
    params = {'from_date': int(time.time()) - 600}
    homework = requests.get(YP_ENDPOINT, headers=HEADERS, params=params)
    if homework.status_code == 200:
        homework = homework.json()
        if 'homeworks' in homework and homework['homeworks']:
            homework = homework['homeworks'][0]
            message = (
                f'Work status "{homework["lesson_name"]}" '
                f'changed to "{homework["status"]}", '
                f'reviewer comment: "{homework["reviewer_comment"]}"'
            )
            bot.send_message(CHAT_ID, text=message[:255])
    return {
        'statusCode': 200,
        'body': 'its alive',
    }
