# python Project installer
import subprocess
import sys


def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.PIPE)
    return_code = subprocess.getstatusoutput([sys.executable, "-m", "pip", "install", package])
    return return_code


colorama_install = install('colorama')
if colorama_install[0] == 0:
    from colorama import Fore, init
    init()
    init(autoreset=True)
    print(Fore.GREEN+"[+]"+Fore.Cyan+"Install Successful")
else:
    print("[-] Installation unsuccessful \n Please refer to Readme.txt")
