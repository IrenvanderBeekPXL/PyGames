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
    bovenste_kaart = util.randbelow(len(util.kaarten_stapel))
    speler = -1
    while not util.is_gewonnen(bordjes[speler]):
        speler += 1
        speler %= aantal_spelers
        util.hide_show(speler)
        for i in bordjes[speler]:
            print(i)
        print("De bovenste kaart is", bovenste_kaart)
        print("Wil je vanaf de open kaarten of gesloten kaarten pakken? (o/g)")
        open_kaart = input() == "o"
        if not open_kaart:
            kaart = util.randbelow(len(util.kaarten_stapel))
            print("Jouw kaart is", kaart)
        print("Welke index kaart wil je vervangen? (bovenste is 1)")
        index = int(input()) - 1
        if open_kaart:
            bovenste_kaart = util.verander_kaart(index, bovenste_kaart, bordjes[speler])
        else:
            bovenste_kaart = util.verander_kaart(index, kaart, bordjes[speler])
    util.hide()
    print("Speler", speler, "heeft gewonnen!")
    print("Bedankt voor het spelen")


if __name__ == '__main__':
    main()
