from secrets import randbelow
from time import sleep
def schud_kaarten():
    nog_beschikbare_kaarten = [["K2 ", "K3 ", "K4 ", "K5 ", "K6 ", "K7 ", "K8 ", "K9 ", "K10", "KB ", "KQ ", "KK ", "KA "],
                               ["S2 ", "S3 ", "S4 ", "S5 ", "S6 ", "S7 ", "S8 ", "S9 ", "S10", "SB ", "SQ ", "SK ", "SA "],
                               ["R2 ", "R3 ", "R4 ", "R5 ", "R6 ", "R7 ", "R8 ", "R9 ", "R10", "RB ", "RQ ", "RK ", "RA "],
                               ["H2 ", "H3 ", "H4 ", "H5 ", "H6 ", "H7 ", "H8 ", "H9 ", "H10", "HB ", "HQ ", "HK ", "HA "],
                               ["K2 ", "K3 ", "K4 ", "K5 ", "K6 ", "K7 ", "K8 ", "K9 ", "K10", "KB ", "KQ ", "KK ", "KA "],
                               ["S2 ", "S3 ", "S4 ", "S5 ", "S6 ", "S7 ", "S8 ", "S9 ", "S10", "SB ", "SQ ", "SK ", "SA "],
                               ["R2 ", "R3 ", "R4 ", "R5 ", "R6 ", "R7 ", "R8 ", "R9 ", "R10", "RB ", "RQ ", "RK ", "RA "],
                               ["H2 ", "H3 ", "H4 ", "H5 ", "H6 ", "H7 ", "H8 ", "H9 ", "H10", "HB ", "HQ ", "HK ", "HA "]]
    spelbord = [[], [], [], [], [], [], [], []]
    for i in range(13):
        for j in range(8):
            shape = randbelow(8)
            while len(nog_beschikbare_kaarten[shape]) == 0:
                shape = randbelow(8)
            level = randbelow(len(nog_beschikbare_kaarten[shape]))
            spelbord[j].append(nog_beschikbare_kaarten[shape].pop(level))
    return spelbord

def goed_geraden(spelbord, veld1, veld2):
    if (spelbord[veld1[1]][veld1[0]] == spelbord[veld2[1]][veld2[0]]):
        return True
    else:
        return False

def print_bord(spelbord, veld):
    veld = [int(veld[2:]), int(veld[0])]
    print("  ", end="")
    for i in range(9):
        print(" " + str(i+1), end="   ")
    for i in range(9, 13):
        print(" " + str(i+1), end="  ")
    print()
    for i in range(len(spelbord)):
        print(i + 1, end=" ")
        for j in range(len(spelbord[i])):
            if (j + 1 == veld[0]) and (i + 1 == veld[1]):
                print(spelbord[i][j], end="  ")
            elif spelbord[i][j] == "":
                print("  ", end="   ")
            else:
                print("veld", end=" ")
        print()
    print()


def main():
    spelbord = schud_kaarten()
    print("Het spelbord bevat 52 kaarten...")
    sleep(1)
    print("Maar er zijn er 2 helemaal door elkaar geschud...")
    sleep(1)
    if not input("Los jij het probleem op? ") == "Y":
        raise ConnectionRefusedError ("Input should be 'Y'")
    aantal_sets_over = 52
    while aantal_sets_over != 0:
        print_bord(spelbord, "0/0")
        veld1 = input("Welk veld wil je bekijken? (verticale pos/horizontale pos) ")
        print_bord(spelbord, veld1)
        veld2 = input("Welk veld is hetzelfde? (verticale pos/horizontale pos) ")
        while veld1 == veld2:
            print("velden mogen niet dezelfde positie hebben")
            veld2 = input("Welk veld is hetzelfde? (verticale pos/horizontale pos) ")
        print_bord(spelbord, veld2)
        veld1 = [int(veld1[2:])-1, int(veld1[0])-1]
        veld2 = [int(veld2[2:])-1, int(veld2[0])-1]
        if goed_geraden(spelbord, veld1, veld2):
            print("Match gevonden!")
            spelbord[veld1[1]][veld1[0]] = ""
            spelbord[veld2[1]][veld2[0]] = ""
            aantal_sets_over -= 1
        else:
            print("Probeer opnieuw")
        sleep(5)
    print("Goed gedaan!")
    sleep(1)
    print("De kaartspellen zijn weer gesorteerd!")
    sleep(1)
    print("Bedankt voor het spelen!")
    sleep(1)


if __name__ == "__main__":
    main()