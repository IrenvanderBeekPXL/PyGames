from secrets import randbelow
import math
number = 10000
while True:
    item = chr(randbelow(92) + 34)
    randpos = randbelow(number)
    teller = 0
    for i in range(int(math.sqrt(number))):
        for j in range(int(math.sqrt(number))):
            teller += 1
            if teller == randpos:
                print(chr(ord(item) - 1), end=" ")
            else:
                print(item, end=" ")

        print()

    print("The math for the position is (vertical * 100) + horisontal")

    if randpos == int(input("On which position is the one that is not as the rest?")):
        print("Nice")
        if input("Do you want to stop now? (Y/n) ") == "Y":
            print("Thanks for playing")
            break
    else:
        print("Try again")
