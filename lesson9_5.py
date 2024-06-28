import socket

host = '127.0.0.1'
port = 54783

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
            if line[0] == 'quit':
                break
            print(f'{addr} -> {line}')
finally:
    print(f'{addr} -> сервер остановлен')
    file.close()
    conn.close()
    sock.close()
