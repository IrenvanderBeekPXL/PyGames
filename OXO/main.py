# Deze oefening wil ik later gaan vertalen naar Java, en dus ga ik het anders doen dan dat ik normaal doe

# PyChram vind dat er veel dubbele code is, maar ik zie het niet

def toon_bord(spelbord):
    print(end="\t")
    for i in range(len(spelbord[0])):
        print(i + 1, end="\t")
    print("\n")
    for i in range(len(spelbord)):
        print(i + 1, end="\t")
        for j in spelbord[i]:
            print(j, end="\t")
        print("\n")


def vraag_doe_zet(spelbord, speler):
    toon_bord(spelbord)
    veld = input("Op welk veld wil je iets zetten? ")
    veld = [int(veld[0]) - 1, int(veld[1]) - 1]
    while not rij_kolom_controle(int(veld[0]), int(veld[1]), spelbord):
        veld = input("Error, veld bestaat niet, probeer opnieuw")
        veld = [int(veld[0])-1, int(veld[1])-1]
    while not spelbord[veld[1]][veld[0]] == " ":
        print("Error, veld is al bezet")
        veld = input("Op welk veld wil je iets zetten? ")
        veld = [int(veld[0]) - 1, int(veld[1]) - 1]
        while not rij_kolom_controle(int(veld[0]), int(veld[1]), spelbord):
            veld = input("Error, veld bestaat niet, probeer opnieuw")
            veld = [int(veld[0]) - 1, int(veld[1]) - 1]
    spelbord[veld[1]][veld[0]] = speler


def rij_kolom_controle(rij, kolom, spelbord):
    return len(spelbord[0])-1 >= kolom >= 0 and len(spelbord)-1 >= rij >= 0


def check_winaar(spelbord):
    def drie_op_een_rij(bord, teken):
        return bord[0][0] == bord[1][0] == bord[2][0] == teken or \
               bord[0][1] == bord[1][1] == bord[2][1] == teken or \
               bord[0][2] == bord[1][2] == bord[2][2] == teken or \
               bord[0][0] == bord[1][1] == bord[2][2] == teken or \
               bord[0][2] == bord[1][1] == bord[2][0] == teken or \
               bord[0][0] == bord[0][1] == bord[0][2] == teken or \
               bord[1][0] == bord[1][1] == bord[1][2] == teken or \
               bord[2][0] == bord[2][1] == bord[2][2] == teken

    if drie_op_een_rij(spelbord, "X"):
        return "X"
    elif drie_op_een_rij(spelbord, "O"):
        return "O"
    else:
        return ""


def main():
    bord = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    vraag_doe_zet(bord, "O")
    vraag_doe_zet(bord, "X")
    vraag_doe_zet(bord, "O")
    vraag_doe_zet(bord, "X")
    vraag_doe_zet(bord, "O")
    if check_winaar(bord) == "O":
        print("O heeft gewonnen!")
        toon_bord(bord)
        return "O"
    vraag_doe_zet(bord, "X")
    if check_winaar(bord) == "X":
        print("X heeft gewonnen!")
        toon_bord(bord)
        return "X"
    vraag_doe_zet(bord, "O")
    if check_winaar(bord) == "O":
        print("O heeft gewonnen!")
        toon_bord(bord)
        return "O"
    vraag_doe_zet(bord, "X")
    if check_winaar(bord) == "X":
        print("X heeft gewonnen!")
        toon_bord(bord)
        return "X"
    vraag_doe_zet(bord, "O")
    if check_winaar(bord) == "O":
        print("O heeft gewonnen!")
        toon_bord(bord)
        return "O"
    toon_bord(bord)


if __name__ == '__main__':
    main()
