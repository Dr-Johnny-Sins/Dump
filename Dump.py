import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[97;1m [•] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/BmxmNHAMjLj5i59vqB2uKw')
tokyo=platform.architecture()[0]
if tokyo=="32bit":
    os.system('clear')
    print('\033[91;1m [•] 32 Bit Device Not Working')
elif tokyo=="64bit":
    __import__("dump64")
