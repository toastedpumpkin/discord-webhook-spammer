import requests
import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

pcname = (os.getenv('COMPUTERNAME'))
os.system('title DWS by toastedpumpkin - thanks for using this tool ' + pcname)

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
print(f"{Fore.MAGENTA}by toastedpumpkin - https://discord.gg/cHzvPFHPVd")
time.sleep(0.5)

wbhk = input(f"{Fore.LIGHTWHITE_EX}> webhook: ")
pyld = input(f"{Fore.LIGHTWHITE_EX}> payload: ")
print(f"{Fore.RED}[+] Awesome sauce.")

def function():
    requests.post(wbhk,json={'content': pyld,})

while True:
    function()
    time.sleep(0.3)
    print(f"{Fore.GREEN}[+] Message sent!")
