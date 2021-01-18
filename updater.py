def check_md5(other_md5, zip_name):
    from hashlib import md5
    m = md5()
    with open(zip_name, "r") as f:
        data = f.read()  # read file in chunk and call update on each chunk if file is large.
        m.update(data)
        zip_md5 = m.hexdigest()
    return other_md5 == zip_md5

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
if input("Do you want to update to a beta version? (Y/n)") == "n":
    print("Updating... Please do not turn off your computer")
    os.system("wget -q --tries=inf http://iren.be/soepweb4/computer/downloads/TerminalGames-update.zip")
    os.system("wget -q tries=inf http://iren.be/soepweb4/computer/downloads/update-md5.txt")
    txt = open("update-md5.txt", "r")
    print("Checking download...")
    while not check_md5(txt.read().strip(), "TerminalGames-update.zip"):
        print("Download corrupted. Retrying...")
        os.system("rm TerminalGames-update.zip")
        txt.close()
        os.system("rm update-md5.txt")
        os.system("wget -q --tries=inf http://iren.be/soepweb4/computer/downloads/TerminalGames-update.zip")
        print("Checking download...")
        os.system("wget -q tries=inf http://iren.be/soepweb4/computer/downloads/update-md5.txt")
        txt = open("update-md5.txt", "r")
    print("Installing update...")
    os.system("\cp -R TerminalGames-update.zip updates")
    os.system("rm TerminalGames-update.zip")
    os.system("unzip updates/TerminalGames-update")
    os.system("\cp -r TerminalGames-main ..")
    os.system("rm updates/TerminalGames-update.zip")
else:
    print("Updating... Please do not turn off your computer")
    os.system("wget -q --tries=inf http://iren.be/soepweb4/computer/downloads/TerminalGames-update-b.zip")
    os.system("wget -q tries=inf http://iren.be/soepweb4/computer/downloads/update-b-md5.txt")
    txt = open("update-b-md5.txt", "r")
    print("Checking download...")
    while not check_md5(txt.read().strip(), "TerminalGames-update-b.zip"):
        print("Download corrupted. Retrying...")
        os.system("rm TerminalGames-update-b.zip")
        txt.close()
        os.system("rm update-b-md5.txt")
        os.system("wget -q --tries=inf http://iren.be/soepweb4/computer/downloads/TerminalGames-b-update.zip")
        print("Checking download...")
        os.system("wget -q tries=inf http://iren.be/soepweb4/computer/downloads/update-b-md5.txt")
        txt = open("update-b-md5.txt", "r")
    print("Installing update...")
    os.system("\cp -R TerminalGames-update-b.zip updates")
    os.system("rm TerminalGames-update-b.zip")
    os.system("unzip updates/TerminalGames-update-b")
    os.system("\cp -r TerminalGames-main ..")
    os.system("rm updates/TerminalGames-update-b.zip")
os.system("python3 main.py")
