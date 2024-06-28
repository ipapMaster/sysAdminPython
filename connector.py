# Наследование (inheritance)
# Расширение функциональности
class IpAddress:  # superclass (базовый или суперкласс)
    def __init__(self, ip='127.0.0.1', port=80):
        self._ip = ip  # protected
        self._port = port  # protected

    def ping_once(self):
        return 'Пинганули один раз'


class UserAuth(IpAddress):
    def __init__(self, ip, port, login, password):
        super().__init__(ip, port)
        self.__login = login
        self.__password = password

ua = UserAuth('192.168.0.1', 3000, 'admin', '12345')

print(ua._ip)



