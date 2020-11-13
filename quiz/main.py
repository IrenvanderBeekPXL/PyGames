# You can also do this as a "Wie is de mol" test program. It will not time, but you can run a stopwatch

def hide():
    input("Press enter to hide")
    for i in range(2000):
        print("\n")
    input("Press enter to continue")

def main():
    hide()
    vragenlijst = []
    antwoordenlijst = []
    goede_antwoorden = []
    vraag = input("Typ een vraag in (xxx om te stoppen) ")
    while vraag != "xxx" and vraag != "XXX":
        vragenlijst.append(vraag)
        antwoorden = []
        antwoord = input("Wat is het goede antwoord? ")
        goede_antwoorden.append(antwoord)
        antwoord = input("Wat is een van de verkeerde antwoorden? ")
        while antwoord != "xxx" and antwoord != "XXX":
            antwoorden.append(antwoord)
            antwoord = input("Wat is een van de verkeerde antwoorden? (xxx om te stoppen) ")
        antwoordenlijst.append(antwoorden)
        vraag = input("Typ een vraag in (xxx om te stoppen) ")
    hide()

