# Планировщик 0 * * * * my_script
import threading
from subprocess import run, PIPE
from sys import platform
import schedule
import time

host_addr = '172.28.202.1'
counter = 0


def ping_ip(host):
    param = '-n' if platform.lower() == 'win32' else '-c'
    command = f'ping {param} 1 {host}'
    response = run(command, stdout=PIPE)
    return response


def job(ip):
    ping_ip(ip)


def run_thread(job_func):
    new_thread = threading.Thread(target=job_func)
    new_thread.start()


schedule.every(2).second.do(job)
schedule.every(10).minute.do(run_thread, job)

while True:
    schedule.run_pending()
    time.sleep(1)
