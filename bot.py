import requests

TOKEN = '5961004367:AAHumxmRNJgbt3W4qc2QdqvOy3SS8LydV6Q'


def getUpdates():
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    return response.json()['result'][-1]

def sendButton(chat_id):
    text = 'Welcome to our bot\n\npress the button for dog photo'
    btn = {
        'text': 'dog'
    }
    keyboard = [
        [btn]
    ]
    payload = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': {
            'keyboard': keyboard
        }
    }
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage', json=payload)
    

def getPhoto():
    response = requests.get('https://random.dog/woof.json')
    return response.json()['url']

def sendPhoto(chat_id):
    url = getPhoto()
    payload = {
        'chat_id': chat_id,
        'text': 'dog',
        'photo': url
    }
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/sendPhoto', json=payload)


last_update = getUpdates()
last_msg = last_update['message']['text']
chat_id = last_update['message']['from']['id']


if last_msg == '/start':
    sendButton(chat_id)
elif last_msg == 'dog':
    sendPhoto(chat_id)
