from sys import platform
import time
from subprocess import run, PIPE

host_addr = 'google.com'
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
    else:
        counter += 1
        if counter > 10:
            counter = 0
            # отправить sms, почту....
    time.sleep(1)
