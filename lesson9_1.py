"""
Journald syslog      vs       Python
level                         Loggin
0: emerg                    Debug (10)
1: alert                    Info (20)
2: crit                     Warning (30)
3: err                      Error (40)
4: warning                  Critical (50)
5: notice
6: info
7: debug
"""
from ini import *
import paramiko
import json

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(host, port, user, password, look_for_keys=False)

stdin, stdout, stderr = client.exec_command("journalctl -x -o json| grep login")

temp_str = stdout.read().decode()
error = stderr.read()

temp = temp_str.split('\n')

for string in temp:
    if string:
        result = json.loads(string)
        print(result)
# print(error)

