from secrets import randbelow
def dice():
    return randbelow(6) + 1

def print_board(board, need_to_start):
    print("   ", end=" ")
    for i in need_to_start:
        print(i, end="  ")
        for j in range(int(len(board) / len(need_to_start)-1)):
            print("  ", end=" ")
    print("", end="\n ")
    for i in board:
        print(i, end="  ")
    print()

def move(player, pawn, needs_to_start, board, moves_to_move):
    # Make a system to get the correct pawn, and move it moves_to_move places towards index -inf
    # Also store the last number in the variable last_number. You can use print_board for debugging
    # If moves_to_move is 6, you should get a new pawn on the board
    # the place to let it start is player * 10 - 8
    def moving(moves_to_move, player, pawn, board):
        for i in range(pawn + 1):
            try:
                pawn_index = board.index(player, pawn_index)
            except:
                if player in board:
                    pawn_index = 0
                else:
                    break
        try:
            last_number = board[pawn_index - moves_to_move]
            board[pawn_index - moves_to_move] = player
            board[pawn_index] = "."
        except:
            last_number = "."
        return last_number

    if moves_to_move == 6 and needs_to_start[player] != 0:
        needs_to_start[player] -= 1
        last_number = board[player * 10 + 2]
        board[player * 10 + 2] = player
    else:
        last_number = moving(moves_to_move, player, pawn, board)    

    if last_number != ".":
        needs_to_start[last_number] += 1

def main():
    needs_to_start = [4] * 4
    board = ["."] * 40
    while not "." in board or not 0 in needs_to_start:
        for i in range(4):
            moves_to_move = dice()
            print_board(board, needs_to_start)
            print("jij hebt", moves_to_move, "gegooid met de dobbelsteen")
            pawn = int(input("Welke pion wil je zetten? (jij bent speler " + str(i) + ") "))
            move(i, pawn, needs_to_start, board, moves_to_move)

    print("Spel afgelopen. Alle pionnen zijn verdwenen")

if __name__ == "__main__":
    main()