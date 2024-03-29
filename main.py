from datetime import datetime
import threading
from time import sleep
import json
import os
try:
    import tls_client
    from colorama import Fore, init, Back
    from pystyle import Write, Colors
    import sys
except:
    os.system("pip install tls_client")
    os.system("pip install colorama")
    os.system("pip install pystyle")
    os.system("pip install sys")

print_lock = threading.Lock()

def time_rn():
    current_datetime = datetime.now()
    current_hour = current_datetime.hour
    current_minute = current_datetime.minute 
    return ("{:02d}:{:02d}".format(current_hour, current_minute))

class OperaGX:
    def __init__(self):
        self.session = tls_client.Session(
        client_identifier="chrome122")
    
    def getData(self, session_gx: str):
        self.session_gx = session_gx

        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cookie": f"SESSION_TYPE=user; SESSION={self.session_gx}",
            "Origin": "https://www.opera.com",
            "Referer": "https://www.opera.com/",
            "Sec-Ch-Ua": '"Not A(Brand";v="99", "Opera GX";v="107", "Chromium";v="121"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
        }
        try:
            r = self.session.get("https://api.gx.me/profile/token", headers=headers)
            self.auth = r.json()['data']
        except:
            i = OperaGX()
            i.getData(self.session_gx)

    def getNitro(self):
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Authorization": self.auth,
            "Origin": "https://www.opera.com",
            "Referer": "https://www.opera.com/",
            "Sec-Ch-Ua": '"Not A(Brand";v="99", "Opera GX";v="107", "Chromium";v="121"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
        }
        try:
            nitro = self.session.post("https://discord.opr.gg/v2/direct-fulfillment", headers=headers)
            nitroGift = nitro.json()['token']
            nitro = f"https://discord.com/billing/partner-promotions/1180231712274387115/{nitroGift}"

            with open("nitro.txt",'a') as f:
                f.write(f"{nitro}\n")

            with print_lock:
                print(f"{Fore.MAGENTA}[{Fore.RESET}{time_rn()}{Fore.MAGENTA}] {Fore.BLUE}GEN{Fore.RESET} Received Nitro ", end="")
                Write.Print(f"[{nitro[0:60]}...{nitro[-10:]}]" + "\n", Colors.red_to_white, interval=0.000)
        except Exception as e:
            with print_lock:
                print(f"{Fore.MAGENTA}[{Fore.RESET}{time_rn()}{Fore.MAGENTA}] {Fore.RED}GEN{Fore.RESET} Failed ", end="")
                Write.Print(f"[{e}]" + "\n", Colors.red_to_white, interval=0.000)
                sleep(1)


icon = ("""
     ▒█████   ██▓███  ▓█████  ██▀███   ▄▄▄           ▄████ ▒██   ██▒
    ▒██▒  ██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▒████▄        ██▒ ▀█▒▒▒ █ █ ▒░
    ▒██░  ██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄     ▒██░▄▄▄░░░  █   ░
    ▒██   ██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██    ░▓█  ██▓ ░ █ █ ▒ 
    ░ ████▓▒░▒██▒ ░  ░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒   ░▒▓███▀▒▒██▒ ▒██▒
    ░ ▒░▒░▒░ ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░    ░▒   ▒ ▒▒ ░ ░▓ ░
      ░ ▒ ▒░ ░▒ ░      ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░     ░   ░ ░░   ░▒ ░
    ░ ░ ░ ▒  ░░          ░     ░░   ░   ░   ▒      ░ ░   ░  ░    ░  
        ░ ░              ░  ░   ░           ░  ░         ░  ░    ░  
                                                                """)
Write.Print(f"{icon}" + "\n", Colors.red_to_white, interval=0.000)

try:
    with open("config.json",'r') as fart:
        data = json.load(fart)
        num_threads = data['numThreads']
        operaSession = data['sessionID']
        
except Exception as e:
    print(f"{Fore.MAGENTA}[{Fore.RESET}{time_rn()}{Fore.MAGENTA}] {Fore.RED}ERR{Fore.RESET} Please setup ur config.json! ", end="")
    Write.Print(f"[{e}]" + "\n", Colors.red_to_white, interval=0.000)
    sleep(5)
    sys.exit()

def get():
    i = OperaGX()
    i.getData(operaSession)
    i.getNitro()

threads = []

while True:
    for i in range(int(num_threads)):
        thread = threading.Thread(target=get, name=f"LordTheBest")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
