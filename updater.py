import platform
import os

infof = open("info.txt", 'rw')
info = []
for i in infof:
    info.append(i.strip())
if info[1] == "not_installed" and platform.system() == "Linux":
    print("installing updater...")
    os.system("sudo apt-get install wget")