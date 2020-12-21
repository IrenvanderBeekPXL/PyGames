import platform
import os

infof = open("info.txt", 'r+')
info = []
for i in infof:
    info.append(i.strip())
if info[0] == "not_installed" and platform.system() == "Linux":
    print("installing updater...")
    print("Asking for sudo rights... Please type the sudo password")
    os.system("sudo apt-get install wget")
    os.system("sudo apt-get install unzip")
    infof.write("installed")
    info[0] = "installed"
    print("Installed updater")
infof.close()

print("Updating... Please do not turn off your computer")
os.system("wget -q --tries=inf http://iren.be/soepweb4/computer/downloads/TerminalGames-update.zip")
os.system("\cp -R TerminalGames-update.zip updates")
os.system("rm TerminalGames-update.zip")
os.system("unzip updates/TerminalGames-update")
os.system("mv *.* ..")
os.system("rm updates/TerminalGames-update.zip")
os.system("python3 main.py")
