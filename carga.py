import time
import os 
from colorama import Fore, Back, Style

espacios = 10
espacio = " "
for i in range(1,10):
    print(f'[',f'{Fore.GREEN}{"█"*i}{espacio*espacios}',f"{Fore.WHITE}",f"{i} / 10]")
    espacios -= 1
    os.system("cls")