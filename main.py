# The games programmed in here do not use the GPU and only 1 core

import os
print("Welcome to PyGames")
print("Some games only work on 1920 * 1080 resolution")
game = input("Which game do you want to play?")
while input != "stop":
    print("Opening game...")
    os.system("python3 " + game + "/main.py")
    game = input("Which game do you want to play?")