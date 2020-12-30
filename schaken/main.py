import os
from stockfish import Stockfish
import platform
#os.system("python3 schaken/sunfish-master/sunfish.py")
user = "12000780"
engine = Stockfish("C:/Users/" + user + "/PycharmProjects/PyGames/schaken/stockfish-win/stockfish.exe")
engine.set_depth(20)
engine.set_skill_level(20)
moves = []
while True:
    print(engine.get_board_visual(), end="")
    print("  a   b   c   d   e   f   g   h")
    print()
    move = input("Zet een zet zoals e2e4  ")
    while not engine.is_move_correct(move):
        move = input("Zet een zet zoals e2e4  ")
    moves.append(move)
    engine.set_position(moves)
    moves.append(engine.get_best_move())
    engine.set_position(moves)
