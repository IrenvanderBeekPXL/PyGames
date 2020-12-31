import os
os.system("pip install stockfish")
from stockfish import Stockfish
import platform
#os.system("python3 schaken/sunfish-master/sunfish.py")
user = "12000780"
if platform.system == "Linux":
    engine = Stockfish("schaken/stockfish-linux/stockfish")
else:
    engine = Stockfish("schaken/stockfish-win/stockfish.exe")
engine.set_depth(20)
engine.set_skill_level(20)
wit = True
moves = []
engine.set_position(moves)
while engine.get_evaluation() != {'type': 'mate', 'value': 0}:
    if wit:
        print(engine.get_board_visual(), end="")
        print("  a   b   c   d   e   f   g   h")
        print()
        move = input("Zet een zet zoals e2e4  ")
        while not engine.is_move_correct(move):
            move = input("Zet een zet zoals e2e4  ")
        moves.append(move)
        engine.set_position(moves)
        wit = False
    else:
        best_move = engine.get_best_move()
        moves.append(best_move)
        print("Mijn zet is", best_move)
        engine.set_position(moves)
        wit = True
    
