import requests
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(f"{Fore.MAGENTA}▓█████▄     █     █░     ██████ ")           
print(f"{Fore.MAGENTA}▒██▀ ██▌   ▓█░ █ ░█░   ▒██    ▒ ")
print(f"{Fore.MAGENTA}░██   █▌   ▒█░ █ ░█    ░ ▓██▄")
print(f"{Fore.MAGENTA}░▓█▄   ▌   ░█░ █ ░█      ▒   ██▒")
print(f"{Fore.MAGENTA}░▒████▓    ░░██▒██▓    ▒██████▒▒")
print(f"{Fore.MAGENTA} ▒▒▓  ▒    ░ ▓░▒ ▒     ▒ ▒▓▒ ▒ ░")
print(f"{Fore.MAGENTA} ░ ▒  ▒      ▒ ░ ░     ░ ░▒  ░ ░")
print(f"{Fore.MAGENTA} ░ ░  ░      ░   ░     ░  ░  ░  ")  
print(f"{Fore.MAGENTA}   ░           ░             ░  ")
print(f"{Fore.MAGENTA} ░ ")

time.sleep(3)

wbhk = input(f"{Fore.RED}WEBHOOK: ")
pyld = input(f"{Fore.RED}MESSAGE: ")
lolsponsor = ("LMAO THIS WEBHOOK HAS BEEN SPAMMED BY TOASTEDPUMPKIN'S DWS")

def function():
    requests.post(wbhk,json={'content': pyld,})
    requests.post(wbhk,json={'content': lolsponsor,})

while True:
    function()
    time.sleep(1)
    print("sent :3")
