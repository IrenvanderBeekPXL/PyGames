# Alles waar geen def voor staat is main
from secrets import randbelow

spelbord = [[False, False, False, False], [False, False, False, False], [False, False, False, False]]


def spawn_check(matrix, row, col):
    # check if already exists
    if (matrix[row][col]):
        return False

    # check sides
    collide_top = False
    collide_bottom = False
    collide_left = False
    collide_right = False
    if (row != 0 and matrix[row - 1][col]):  # check Top
        collide_top = True
    if (row != len(matrix) - 1 and matrix[row + 1][col]):  # check Bottom
        collide_bottom = True
    if (col != 0 and matrix[row][col - 1]):  # check Left
        collide_left = True
    if (col != len(matrix[0]) - 1 and matrix[row][col + 1]):  # check Right
        collide_right = True

    # return true if nothing colided
    if (collide_top == collide_bottom == collide_left == collide_right):
        return True
    else:
        return False


def spawnBooten():
    aantal_booten = 0
    while (aantal_booten != 3):
        pos = randbelow(12)
        col = pos % 4
        row = pos // 4
        if (spawn_check(spelbord, row, col)):
            aantal_booten += 1
            spelbord[row][col] = True


spawnBooten()
# Bedankt Sander voor de code hierboven!


def veld_splitter(veld_str):
    veld_lijst = list(veld_str)
    veld_lijst[0] = ord(veld_lijst[0]) - 65
    veld_lijst[1] = int(veld_lijst[1]) - 1
    return veld_lijst


boten_over = 3
schoten = 0
while boten_over != 0:
    input("Druk op enter om te laden...")
    # print spelbord
    for i in " ABCD":
        print(i, end="\t   ")
    print(end="\n")
    for i in range(1, len(spelbord) + 1):
        print(i, end="\t")
        for j in spelbord[i-1]:
            print("Veld", end="\t")
        print(end="\n")
    # Vraag gamer om input
    veld = input("Op welk veld wil je schieten? (KolomRij) ")
    veld = veld_splitter(veld)
    schoten += 1
    if spelbord[veld[1]][veld[0]]:
        print("Raak!")
        boten_over -= 1
        spelbord[veld[1]][veld[0]] = False
    else:
        print("Mis!")

print("Je hebt alle vijandelijke schepen neergeschoten!")
print("Je hebt", schoten, "keer geschoten")
print("Bedankt voor het spelen!")
