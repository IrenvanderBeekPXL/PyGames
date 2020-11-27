# The games programmed in here do not use the GPU and only 1 core

import os
pythongames = ["hartenjagen", "memory", "OXO", "quiz", "schaken", "zeeslag", "hangman"]
javagames = []
games = pythongames + javagames
print("Welcome to TerminalGames")
print("Some games only work on 1920 * 1080 resolution")
print("Copy one of the following games")
for i in games:
    print(i)
game = input("Which game do you want to play?")
while game != "stop":
    print("Opening game...")
    if game in pythongames:
        os.system("python3 " + game + "/main.py")
    print("Copy one of the following games")
    for i in games:
        print(i)
    game = input("Which game do you want to play?")