import os
import smtplib

"""
mimetype — Медиа тип (так же известный как
Multipurpose Internet Mail Extensions или MIME тип)
"""
import mimetypes  # используем, если анализируем
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')


def send_mail(email, subject, text, attachment=None):
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        return False

    addr_from = os.getenv('FROM')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    port = os.getenv('PORT')

    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = email
    msg['Subject'] = subject
    body = text
    msg.attach(MIMEText(body, 'plain'))

    # Вложение, если есть
    if attachment:
        with open(attachment, 'rb') as file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment)}')
        msg.attach(part)
    # Конец блока вложения

    server = smtplib.SMTP_SSL(host, int(port))
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()

    # print(f'from={addr_from}, password={password}, host={host}, port={port}')


if __name__ == '__main__':
    send_mail('', '', '')
