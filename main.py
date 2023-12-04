import requests
import ctypes
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
time.sleep(2)
print(f"{Fore.MAGENTA}https://discord.gg/cHzvPFHPVd")
time.sleep(3)

wbhk = input(f"{Fore.LIGHTWHITE_EX}> webhook: ")
pyld = input(f"{Fore.LIGHTWHITE_EX}> payload: ")

def function():
    requests.post(wbhk,json={'content': pyld,})

while True:
    function()
    time.sleep(0.8)
    print("sent :3")
