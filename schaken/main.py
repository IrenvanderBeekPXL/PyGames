import os
import multiprocessing
os.system("pip install stockfish")
from stockfish import Stockfish
import platform
treads = multiprocessing.cpu_count()
if platform.system == "Linux":
    engine = Stockfish("schaken/stockfish-linux/stockfish", parameters={"Slow Mover": 120, "Threads": treads})
else:
    engine = Stockfish("schaken/stockfish-win/stockfish.exe", parameters={"Slow Mover": 120, "Threads": treads})
engine.set_depth(2)
engine.set_skill_level(2)
wit = True
moves = []
engine.set_position(moves)
play = input("Do you want to play or load in a game? (play/load) ") == "play"
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
            wit = False
        else:
            engine.set_depth(20)
            engine.set_skill_level(20)
            best_move = engine.get_best_move()
            moves.append(best_move)
            print("Mijn zet is", best_move)
            engine.set_position(moves)
            engine.set_depth(2)
            engine.set_skill_level(2)
            wit = True
else:
    print("Please give me the series of moves.")
    print("Press enter with a move to give me the move and \nwithout a move to load in")
    move = input()
    while len(move) != 0:
        moves.append(move)
        move = input()
    engine.set_position(moves)

if input("Do you want to analyze the last game? (Y/n)") == "Y":
    input("WARNING! Analyzing could take a whole day for a long game. Press enter to continue...")
    print("Analyzing...")
    position = []
    best_moves = []
    types = []
    engine.set_depth(30)
    engine.set_skill_level(20)
    white = True
    for i in moves:
        engine.set_position(position)
        best_move = engine.get_best_move()
        best_moves.append(best_move)
        if i == best_move:
            print(i, "was the best move")
            types.append("Best move")
            moves.append(i)
        else:
            evaluation_before = engine.get_evaluation()
            moves.append(i)
            engine.set_position(moves)
            evaluation_after = engine.get_evaluation()
            if evaluation_after.get("type") == "cp":
                if white:
                    if evaluation_after.get("value") >= evaluation_before.get("value"):
                        print(i, "was a good move")
                        types.append("Good move")
                    else:
                        pass
                else:
                    if evaluation_after.get("value") <= evaluation_before.get("value"):
                        print(i, "was a good move")
                        types.append("Good move")
                    else:
                        pass
            elif evaluation_before.get("type") == "mate":
                pass
            elif evaluation_after.get("type") == "mate":
                if white:
                    if evaluation_before.get("value") > 60:
                        types.append("Not that bad")
                        print(i, "was not so good")
                    elif evaluation_before.get("value") > 25:
                        types.append("Bad move")
                        print(i, "was a bad move")
                    else:
                        types.append("Blunder")
                        print(i, "was a blundery blunder")
                else:
                    if evaluation_before.get("value") < -60:
                        types.append("Not that bad")
                        print(i, "was not so good")
                    elif evaluation_before.get("value") < -25:
                        types.append("Bad move")
                        print(i, "was a bad move")
                    else:
                        types.append("Blunder")
                        print(i, "was a blundery blunder")

            print(best_move, "was the best move")
