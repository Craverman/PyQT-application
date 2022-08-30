from task1 import host_ping


def host_range_ping(ip, counter):
    iplist = []
    last_digit = (int(ip.split('.')[3]))

    for el in range(counter):
        host_list = ip.split('.')[:-1]
        last_digit += 1
        host_list.append(str(last_digit))
        host = '.'.join(host_list)
        iplist.append(host)
    return iplist


# host_ping((host_range_ping('123.231.231.200', 4)))