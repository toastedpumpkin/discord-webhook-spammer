import requests
import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

os.system('title DWS by toastedpumpkin - session not logged in yet')
login = input(f"{Fore.LIGHTWHITE_EX}> Username: ")
os.system('title DWS by toastedpumpkin - logged in as ' + login)
print(f"{Fore.GREEN}[+] Successfully logged in.")
print(f"{Fore.LIGHTYELLOW_EX}Loading DWS...")
time.sleep(2)
os.system('cls')

print(f"{Fore.MAGENTA} █████▄     █     █░     ██████ ")           
print(f"{Fore.MAGENTA}▒██▀ ██▌   ▓█░ █ ░█░   ▒██    ▒ ")
print(f"{Fore.MAGENTA}░██   █▌   ▒█░ █ ░█    ░ ▓██▄")
print(f"{Fore.MAGENTA}░▓█▄   ▌   ░█░ █ ░█      ▒   ██▒")
print(f"{Fore.MAGENTA}░▒████▓    ░░██▒██▓    ▒██████▒▒")
print(f"{Fore.MAGENTA} ▒▒▓  ▒    ░ ▓░▒ ▒     ▒ ▒▓▒ ▒ ░")
print(f"{Fore.MAGENTA} ░ ▒  ▒      ▒ ░ ░     ░ ░▒  ░ ░")
print(f"{Fore.MAGENTA} ░ ░  ░      ░   ░     ░  ░  ░  ")  
print(f"{Fore.MAGENTA}   ░           ░             ░  ")
print(f"{Fore.MAGENTA} ░ ")
time.sleep(0.3)
if login == "toastedpumpkin" or  login == "nic":
    print(f"{Fore.LIGHTMAGENTA_EX}Welcome Back, Master.")
if login == "Paw" or login == "paw":
    print(f"{Fore.LIGHTMAGENTA_EX}lemons and demons LMAOO")
time.sleep(0.5)

wbhk = input(f"{Fore.LIGHTWHITE_EX}> Webhook: ")
pyld = input(f"{Fore.LIGHTWHITE_EX}> Payload: ")
print(f"{Fore.RED}[+] Awesome sauce.")

def function():
    requests.post(wbhk,json={'content': pyld,})

while True:
    function()
    time.sleep(0.3)
    print(f"{Fore.GREEN}[+] Message sent!")
