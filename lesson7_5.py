from sys import platform
import time
from subprocess import run, PIPE

host_addr = '172.28.202.1'
counter = 0


def ping_ip(host):
    param = '-n' if platform.lower() == 'win32' else '-c'
    command = f'ping {param} 1 {host}'
    response = run(command, stdout=PIPE)
    return response


# stackoverflow
while True:
    response = ping_ip(host_addr)

    if response.returncode == 0:
        print(response.stdout.decode('cp866'))
        print('Код ответа:', response.returncode)
        counter = 0
    else:
        counter += 1
        print(counter)
        if counter > 10:
            counter = 0
            print('Отправлена почта. Сервер не отвечает')
    time.sleep(1)
