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
