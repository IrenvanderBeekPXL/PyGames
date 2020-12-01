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

def move(player, pawn, needs_to_start, board):
    moves_to_move = dice()
    # Make a system to get the correct pawn, and move it moves_to_move places towards index -inf
    # Also store the last number in the variable last_number. You can use print_board for debugging
    # If moves_to_move is 6, you should get a new pawn on the board


    if last_number != 0:
        needs_to_start[last_number-1] += 1

def main():
    needs_to_start = [4] * 4
    board = [0] * 40
    print_board(board, needs_to_start)

if __name__ == "__main__":
    main()