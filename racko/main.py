import util
import time


def main():
    print("Er is een bordje kaarten...")
    time.sleep(2)
    print("En de volgorde klopt niet...")
    time.sleep(2)
    if not input("Lossen jullie het op? (Y/n) ") == "Y":
        msg = "Error, players do not want to solve the issue"
        raise ConnectionRefusedError(msg)
