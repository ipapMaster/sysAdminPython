import json
import configparser
import requests


def form_of_words(num, text_forms):
    num = abs(num) % 100
    ending = num % 10
    if 10 < num < 20:
        return text_forms[2]
    if 1 < ending < 5:
        return text_forms[1]
    if ending == 1:
        return text_forms[0]
    return text_forms[2]


config = configparser.ConfigParser()
config.read('valute.conf')
cbr_url = config.get('general', 'cbr_url')
response = requests.get(cbr_url)
if response.status_code == 200:
    # print('Ok')
    text = response.text
    response.close()
    json_dict = json.loads(text)
    print('Дата:', '.'.join(json_dict['Timestamp'][:10].split('-')[::-1]))
    print('Курс доллара', end=': ')
    rate = json_dict['Valute']['USD']['Value']
    print(rate, form_of_words(int(rate),
                              ('рубль', 'рубля', 'рублей')))
else:
    print('Сервер вернул неверный ответ.')
