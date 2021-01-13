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
    aantal_spelers = int(input("Hoeveel spelers doen er mee? "))
    bordjes = []
    for i in range(aantal_spelers):
        bordjes.append([])
    util.shuffle(bordjes)
    bovenste_kaart = util.randbelow(len(util.kaartenstapel))
    speler = 0
    while not util.is_gewonnen(bordjes[speler]):
        pass

if __name__ == '__main__':
    main()
