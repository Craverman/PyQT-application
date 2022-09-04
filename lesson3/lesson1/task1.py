from ping3 import ping


def host_ping(ip_adresses):
    for el in ip_adresses:
        resp = ping(el)
        if resp is None:
            print(f'{el} is unavailable')
        else:
            print(f'{el} is available')


# host_ping(['google.com', 'google.ru', '123.123.123.12'])



