import requests
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(f"{Fore.MAGENTA}________           ___       __           ________ ")           
print(f"{Fore.MAGENTA}|\   ____\         |\  \     |\  \        |\   ____\ ")
print(f"{Fore.MAGENTA}\ \  \___|_        \ \  \    \ \  \       \ \  \___|_ ")
print(f"{Fore.MAGENTA} \ \_____  \        \ \  \  __\ \  \       \ \_____  \   ")
print(f"{Fore.MAGENTA}  \|____|\  \        \ \  \|\__\_\  \       \|____|\  \  ")
print(f"{Fore.MAGENTA}    ____\_\  \        \ \____________\        ____\_\  \ ")
print(f"{Fore.MAGENTA}  |\_________\        \|____________|       |\_________\ ")
    
time.sleep(3)

wbhk = input("webhook: ")
pyld = input("payload: ")
lolsponsor = ("**https://github.com/toastedpumpkin/discord-webhook-spammer**")

def function():
    requests.post(wbhk,json={'content': pyld,})
    requests.post(wbhk,json={'content': lolsponsor,})

while True:
    function()
    time.sleep(1)
    print("sent :3")
