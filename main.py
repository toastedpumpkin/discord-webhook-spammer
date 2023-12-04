import requests
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

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
time.sleep(1)
print(f"{Fore.MAGENTA}https://discord.gg/cHzvPFHPVd")
time.sleep(2)

wbhk = input(f"{Fore.LIGHTWHITE_EX}> webhook: ")
pyld = input(f"{Fore.LIGHTWHITE_EX}> payload: ")
print(f"{Fore.RED}awsome sauce")

def function():
    requests.post(wbhk,json={'content': pyld,})

while True:
    function()
    time.sleep(0.6)
    print(f"{Fore.GREEN}message sent")
