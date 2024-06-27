import socket

host = 'localhost'
port = 5678

sock = socket.socket()
sock.bind((host, port))
sock.listen(5)
conn, addr = sock.accept()
file = conn.makefile()
print('Получаем данные с', addr)

try:
    while True:
        line = file.readline()
        if line:
            line = line.rsplit()
            if line == 'quit':
                break
            print(f'{addr} -> {line}')
finally:
    print(f'{addr} -> сервер остановлен')
    file.close()
    conn.close()
    sock.close()