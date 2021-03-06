# You can also do this as a "Wie is de mol" test program. It will not time, but you can run a stopwatch

from secrets import randbelow

def hide():
    input("Press enter to hide")
    for i in range(2000):
        print("\n")
    input("Press enter to continue")

def max(list):
    maximum = 0
    for i in range(len(list)):
        if list[maximum] < list[i]:
            maximum = i
    return maximum

def min(list):  # Almost a copy of max
    maximum = 0
    for i in range(len(list)):
        if list[maximum] > list[i]:
            maximum = i
    return maximum

def main():
    # alle variabelen maken...
    hide()
    namen = []
    vragenlijst = []
    antwoordenlijst = []
    goede_antwoorden = []
    punten = []
    teller = 0
    if input("Wil je de standaardquiz gebruiken? (Y/n)") == "n":
        # vragen en antwoorden vragen aan de quizmaster
        vraag = input("Typ een vraag in (xxx om te stoppen) ")
        while vraag != "xxx" and vraag != "XXX":
            vragenlijst.append(vraag)
            antwoorden = []
            goede_antwoord = input("Wat is het goede antwoord? ")
            goede_antwoorden.append(goede_antwoord)
            antwoord = input("Wat is een van de verkeerde antwoorden? ")
            while antwoord != "xxx" and antwoord != "XXX":
                antwoorden.append(antwoord)
                antwoord = input("Wat is een van de verkeerde antwoorden? (xxx om te stoppen) ")
            antwoorden.insert(randbelow(len(antwoorden)+1), goede_antwoord)
            antwoordenlijst.append(antwoorden)
            vraag = input("Typ een vraag in (xxx om te stoppen) ")
    else:
        vragenlijst.append("Wat is de hoofdstad van Nederland?")
        goede_antwoord = "Amsterdam"
        antwoorden = ["Brussel", "Utrecht", "Eindhoven"]
        antwoorden.insert(randbelow(len(antwoorden)+1), goede_antwoord)
        antwoordenlijst.append(antwoorden)

        vragenlijst.append("In welke taal is dit quizprogramma geschreven?")
        goede_antwoord = "Python"
        antwoorden = ["Nederlands", "Engels", "Zuid-afrikaans", "Java"]
        antwoorden.insert(randbelow(len(antwoorden)+1), goede_antwoord)
        antwoordenlijst.append(antwoorden)

        vragenlijst.append("Welke taal spreken ze in Nederland het meest?")
        goede_antwoord = "Nederlands"
        antwoorden = ["Fries", "Engels", "Nederlands en Fries"]
        antwoorden.insert(randbelow(len(antwoorden)+1), goede_antwoord)
        antwoordenlijst.append(antwoorden)

        vragenlijst.append("Welke programeertaal werd toegevoegd aan TerminalGames voor meerdere games aan het begin van 2021?")
        goede_antwoord = "Java"
        antwoorden = ["C++", "Python", "Engels"]
        antwoorden.insert(randbelow(len(antwoorden)+1), goede_antwoord)
        antwoordenlijst.append(antwoorden)
        
        vragenlijst.append("Welke terminalgames zijn geschreven in Java?")
        goede_antwoord = "UNO en hoogsteKaart"
        antwoorden = ["UNO en schaken", "schaken en hoogsteKaart", "MensErgerJeNiet(AI) en UNO"]
        antwoorden.insert(randbelow(len(antwoorden)+1), goede_antwoord)
        antwoordenlijst.append(antwoorden)
        
        vragenlijst.append("Hoe heet de TerminalGames project map op de PC van de eigenaar?")
        goede_antwoord = "PyGames"
        antwoorden = ["TerminalGames", "iets anders", "Hij werkt alleen in de cloud"]
        antwoorden.insert(randbelow(len(antwoorden)+1), goede_antwoord)
        antwoordenlijst.append(antwoorden)

    hide()
    # antwoorden vragen aan de deelnemers
    naam = input("Hoe heet je? ")
    while naam != "xxx" and naam != "XXX":
        namen.append(naam)
        punten.append(0)
        for i in range(len(vragenlijst)):
            print("Copy-paste een antwoord onderaan de antwoordenlijst aub")
            print(vragenlijst[i])
            for j in range(len(antwoordenlijst[i])):
                print(antwoordenlijst[i][j])
            if input() == goede_antwoorden[i]:
                punten[teller] += 1
        teller += 1
        hide()
        naam = input("Hoe heet je? (xxx om te stoppen) ")
    # antwoorden analyseren
    hide()
    print(namen)
    print(punten)

main()