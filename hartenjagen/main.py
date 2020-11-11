from secrets import randbelow
def deel_kaarten():
    nog_beschikbare_kaarten = [["K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9", "K10", "KB", "KQ", "KK", "KA"],
                               ["S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SB", "SQ", "SK", "SA"],
                               ["R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "RB", "RQ", "RK", "RA"],
                               ["H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HB", "HQ", "HK", "HA"]]
    deling = [[], [], [], []]
    for i in range(13):
        for j in range(4):
            shape = randbelow(4)
            while len(nog_beschikbare_kaarten[shape]) == 0:
                shape = randbelow(4)
            level = randbelow(len(nog_beschikbare_kaarten[shape]))
            deling[j].append(nog_beschikbare_kaarten[shape].pop(level))
    return deling


def geef_kaarten(delinglijst):
    kaarten = [[], [], [], []]
    for i in range(3, -1, -1):
        for j in range(3):
            print(delinglijst[i])
            kaarten[i].append(delinglijst[i].pop(int(input("Welke index kaart wil je doorgeven?")) - 1))
        hide_cards()
    for i in range(4):
        for j in range(3):
            delinglijst[i].append(kaarten[i][j])


def hide_cards():
    input("Press enter to hide your cards")
    for i in range(1000):
        print()
    input("Press enter to continue")


def main():
    deling = deel_kaarten()  # Elke lijst in deling is voor 1 speler
    geef_kaarten(deling)  # hier worden de kaarten doorgegeven
    strafpunten = 4 * [0]
    for i in range(4):
        if "K2" in deling[i]:
            starter = i
    for i in range(13):
        print("Round", i+1)
        pot = []
        for j in range(starter, starter - 4, -1):
            print(pot)
            if "K2" in deling[j]:
                pot.append(deling[j].pop(deling[j].index("K2")))
            else:
                print(deling[j])
                pot.append(deling[j].pop(int(input("Welk index kaart wil je neerleggen?"))-1))
                hide_cards()
        picker = starter
        letter = pot[0][0]
        highest = 2
        for j in range(4):
            # Hier hoort een systeem om te checken wie de kaarten neemt
            if pot[j][1:] == "10":
                pot[j] = pot[j][0] + ">"
            elif pot[j][1] == "A":
                pot[j] = pot[j][0] + "S"
            elif pot[j][1] == "K":
                pot[j] = pot[j][0] + "R"

            if letter == pot[j][0] and ord(pot[j][1]) > highest:
                picker = starter - j
        for j in range(4):
            if pot[j][0] == "H":
                strafpunten[picker] += 1
            elif pot[j] == "SQ":
                strafpunten[picker] += 13
    for i in range(starter, starter-4, -1):
        print("player", i, "has", strafpunten[i], "bad points")


if __name__ == '__main__':
    main()
