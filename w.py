# w

import os
import sys
import requests
import webbrowser as web
from colorama import Fore

def __web__():
    os.system("clear")
    time.sleep(2)
    try:
        print(Fore.YELLOW + "Hellow . Welcome ;) ")
        time.sleep(2)
        target = input(Fore.GREEN + "\n[" + Fore.RED + "!"+Fore.GREEN + "]" + Fore.RED + " ~ " + Fore.YELOW + "Pleass Enter Your Address Target " + Fore.BLUE  + "==>  ")
        if target == "" or None:
            try:
                time.sleep(2)
                print(Fore.YELLOW + "[!] " + Fore.RED + "Error : Your Targert Is None ;(")
                time.sleep(1)
                sys.exit()
            except:
                pass
        s = socket.gethostbyname(target)
        time.sleep(2)
        print(Fore.BLUE + "[" + Fore.RED + "+" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Your Ip Target :  " + s)
        time.sleep(2)
        site = "http://" + target
        r = requests.get(site)
        if r.status_code == 200:
            try:
                time.sleep(1)
                print(Fore.BLUE + "\n[" + Fore.RED + "+" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.GREEN + target + Fore.YELLOW + " > " + Fore.BLUE + "Found ;)")
                time.sleep(1)
            except:
                pass
        else:
            try:
                time.sleep(1)
                print(Fore.BLUE + "\n[" + Fore.RED + "+" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.RED + target + Fore.YELLOW + " > " + Fore.BLUE + "Found ;)")
                time.sleep(1)
                sys.exit()
            except:
                pass
        i = input(Fore.GREEN + "\n1: Open WebSite  2 : Link webSite \nPleass Enter Your Number 1 Or Number 2 ==> ")
        if i == "" or None:
            try:
                time.sleep(1)
                print(Fore.RED + "\nNot Found ;(")
                time.sleep(1)
                sys.exit()
            pass
        if i == 1:
            try:
                time.sleep(1)
                print(Fore.GREEN + "\nOk Pleass 5 Sec Wail Latter ;)")
                time.sleep(1)
                print(Fore.GREEN + "Ok Pleass 4 Sec Wail Latter ;)")
                time.sleep(1)
                print(Fore.GREEN + "Ok Pleass 3 Sec Wail Latter ;)")
                time.sleep(1)
                print(Fore.GREEN + "Ok Pleass 2 Sec Wail Latter ;)")
                time.sleep(1)
                print(Fore.GREEN + "Ok Pleass 1 Sec Wail Latter ;)")
                time.sleep(1)
                web.open(site)
                sys.exit()
            except:
                pass
        if i == 2:
            try:
                time.sleep(1)
                print(Fore.GREEN + "\nOk Pleass 5 Sec Wail Latter ;)")
                time.sleep(1)
                print(Fore.GREEN + "Ok Pleass 4 Sec Wail Latter ;)")
                time.sleep(1)
                print(Fore.GREEN + "Ok Pleass 3 Sec Wail Latter ;)")
                time.sleep(1)
                print(Fore.GREEN + "Ok Pleass 2 Sec Wail Latter ;)")
                time.sleep(1)
                print(Fore.GREEN + "Ok Pleass 1 Sec Wail Latter ;)")
                time.sleep(1)
                print(Fore.BLUE + "[" + Fore.RED + "*" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "\nYour Link WebSite : " + Fore.GREEN + site) 
                time.sleep(2)
                sys.exit()
            except:
                pass
    except:
        pass
__web__()
