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
time.sleep(0.3)
print(f"{Fore.MAGENTA}https://discord.gg/cHzvPFHPVd")
time.sleep(0.7)

wbhk = input(f"{Fore.LIGHTWHITE_EX}> webhook: ")
pyld = input(f"{Fore.LIGHTWHITE_EX}> payload: ")
lmao = ("awesome sauce 😈, you've just been webhook spammed")
print(f"{Fore.RED}awesome sauce")

requests.post(wbhk,json={'content': lmao,})

def function():
    requests.post(wbhk,json={'content': pyld,})

while True:
    function()
    time.sleep(0.2)
    print(f"{Fore.GREEN}message sent")
