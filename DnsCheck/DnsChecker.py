import socket
import time
import sys



def check_conn():
    host = ["www.google.com","www.facebook.com","www.instagram.com"]
    port = int(53)
    for host in host:
        host_risolto = socket.gethostbyname(host)
        print(host_risolto)
    host = host_risolto
    timer = int(time.perf_counter())
    s = socket.socket()

    s.connect((str(host), int(port)))



check_conn()
