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
time.sleep(2)
print(f"{Fore.MAGENTA}https://discord.gg/cHzvPFHPVd")
time.sleep(3)

wbhk = input(f"{Fore.RED}WEBHOOK: ")
pyld = input(f"{Fore.RED}MESSAGE: ")

def function():
    requests.post(wbhk,json={'content': pyld,})

while True:
    function()
    time.sleep(1)
    print("sent :3")
