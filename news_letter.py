import os

from mail_sender import send_mail

email = 'some@mail.ru'
subject = 'Проверка'
body = 'Это текст сообщения для проверки'

attachment = os.path.join(os.path.dirname(__file__), 'файл для отправки')

send_mail(email, subject, body, attachment)
