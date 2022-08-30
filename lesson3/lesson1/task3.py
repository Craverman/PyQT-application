
from tabulate import tabulate
from task2 import host_range_ping


def host_range_ping_tab():
    tab_dict = host_range_ping('123.231.231.200', 4)
    print(tabulate([tab_dict], headers='keys', tablefmt="pipe", stralign="center"))

host_range_ping_tab()
#final task