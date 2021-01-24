import os
import multiprocessing
print("Installing and updating engine wrapper...")
os.system("pip install stockfish")
os.system("pip install --upgrade stockfish")
from stockfish import Stockfish
import platform
treads = multiprocessing.cpu_count()
if platform.system == "Linux":
    engine = Stockfish("schaken/stockfish-linux/stockfish", parameters={"Slow Mover": 120, "Threads": treads})
else:
    engine = Stockfish("schaken/stockfish-win/stockfish.exe", parameters={"Slow Mover": 120, "Threads": treads})
engine.set_depth(30)
engine.set_skill_level(20)
wit = True
moves = []
engine.set_position(moves)
play = True
if play:
    input("WARNING. This chess program is about as strong as it gets. Press enter to continue...")
    while engine.get_best_move_time(3000) is not None:
        if wit:
            print(engine.get_board_visual(), end="")
            print("  a   b   c   d   e   f   g   h")
            print()
            move = input("Zet een zet zoals e2e4  ")
            while not engine.is_move_correct(move):
                move = input("Zet een zet zoals e2e4  ")
            moves.append(move)
            engine.set_position(moves)
            print("Evaluation in centipawns:", engine.get_evaluation())
            wit = False
        else:
            best_move = engine.get_best_move()
            moves.append(best_move)
            print("Mijn zet is", best_move)
            engine.set_position(moves)
            print("Evaluation:", engine.get_evaluation())
            wit = True
