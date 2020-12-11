#!/data/data/com.termux/files/usr/bin/python3
#@Author prince kumar
#date 9 dec 2020
#Version V1.0
#Start
#All import goes here
import socket
from tqdm import tqdm
import time
import os		
# make banner
b_tuple = ( 'S','T','A','R','T','I','N','G','_','T','S','C','A','N' )
for i in b_tuple:
    print(i)
    time.sleep(0.2)
os.system('clear')
print("""\033[33;1m

'########::'######:::'######:::::'###::::'##::: ##:
... ##..::'##... ##:'##... ##:::'## ##::: ###:: ##:
::: ##:::: ##:::..:: ##:::..:::'##:. ##:: ####: ##:
::: ##::::. ######:: ##:::::::'##:::. ##: ## ## ##:
::: ##:::::..... ##: ##::::::: #########: ##. ####:
::: ##::::'##::: ##: ##::: ##: ##.... ##: ##:. ###:
::: ##::::. ######::. ######:: ##:::: ##: ##::. ##:
:::..::::::......::::......:::..:::::..::..::::..::
              \033[37;1m made by prince   \033[31mV1.0
																														
""")

								      					
# Satrt coding here
#Take all input

host = input("\033[33;1m(\033[31m+\033[33m)\033[36m Enter a ip: ")
print("\n")
s_point = input("\033[31;1m(\033[32m+\033[31m)\033[35mEnter a start point: ")
print("\n")
e_point = input("\033[31;1m(\033[32m+\033[31m)\033[35mEnter a end point: ")
print("\n")
						     			 			
def scan_port(port):
	try:
			s = socket.socket()
			s.connect((host, port))
			s.close()
			return True
	except:
				return False


for i in tqdm(range(int(s_point),int(e_point)), desc ="Scanning"):
	
	if scan_port(i):
		print("open port found {}".format(i))
	else:
                pass
					      	       
