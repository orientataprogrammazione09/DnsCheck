#!python

import socket
import time
import os, subprocess, sys

dns_1 = ["1.1.1.1", "1.0.0.1"]
dns_2 = ["8.8.8.8", "8.8.4.4"]
    

def check_conn():
    host = ["www.google.com", "www.facebook.com", "www.instagram.com"]
    port = int(80)
    try:
        for host in host:
            host_risolto = socket.gethostbyname(host)
            #print(host_risolto + host)
        host = host_risolto
        timer = int(time.perf_counter())
        s = socket.socket()
        try:
            s.connect((str(host_risolto), port))
        except socket.error as error:
            print(error)
    except socket.error as error:
        print("[!] Sei offline [!]")
#check_conn()

def dns_change_1():
    global dns_1
    
    subprocess.call('netsh interface ip set dns "Wi-Fi" static '+(dns_1[0]) + ' primary',shell=True)
    subprocess.call('netsh interface ip add dns "Wi-Fi" '+(dns_1[1])+' index=2', shell=True)

def dns_change_2():
    global dns_2
    subprocess.call('netsh interface ip set dns "Wi-Fi" static '+(dns_2[0]) + ' primary',shell=True)
    subprocess.call('netsh interface ip add dns "Wi-Fi" '+(dns_2[1])+' index=2', shell=True)
    
while True:
    print('Controllo se sei connesso....')
    check_conn()
    print('sei connesso alla rete')
    time.sleep(0.5)
    print("Avvio procedura di calcolo velocita' di dns...")
    dns_change_1()
    #subprocess.call('netsh interface ip show config', shell=True)
    os.system("ping google.com")
    print("==========================================")
    dns_change_2()
    print("==========================================")
    os.system("ping google.com")
    x = input()
    

