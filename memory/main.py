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


def main():
    spelbord = schud_kaarten()
    print("Het spelbord bevat 52 kaarten...")
    sleep(1)
    print("Maar ze zijn helemaal door elkaar geschud...")
    sleep(1)
    input("Los jij het probleem op? ")

if __name__ == "__main__":
    main()