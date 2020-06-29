import socket
import time


def check_conn():
    host = ["www.google.com", "www.facebook.com", "www.instagram.com"]
    port = int(53)
    for host in host:
        host_risolto = socket.gethostbyname(host)
        print(host_risolto + host)
    host = host_risolto
    timer = int(time.perf_counter())
    s = socket.socket()
    try:
        s.connect((str(host_risolto), port))
    except socket.error as error:
        print(error)


check_conn()
