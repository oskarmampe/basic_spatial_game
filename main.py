from board import *

# Simulations
end = False
board_dim = int(input("To start, input a board dimension:\n"))

# Default settings
board = [['c' for i in range(board_dim)] for j in range(board_dim)]
board[(board_dim-1)//2][(board_dim-1)//2] = 'd'
b = 1.65
e = 0
time = 64
while not end:
    # Get input
    print("-------------------------CURRENT BOARD-------------------------")
    print('\n'.join([','.join([str(item) for item in row]) for row in board]))
    print("b value: %f, e value: %f, time value: %d" % (b, e, time))
    user_input = input("To modify the board press m, s to simulate, e to change epsilon, b to change b, t to change time to run, w to change world and q to quit.\n")
    if user_input is 's':
        simulate(b, e, board, board_dim=board_dim, time=time)
        end = True
    elif user_input is 'm':
        row = int(input("Input row to change:\n"))
        col = int(input("Input col to change:\n"))
        strat = input("Input strat to change:\n")
        board[row][col] = strat
    elif user_input is 'e':
        e = float(input("Input e to change:\n"))
    elif user_input is 'b':
        b = float(input("Input b to change:\n"))
    elif user_input is 't':
        time = int(input("Input time to change:\n"))
    elif user_input is 'q':
        exit(1)
    elif user_input is 'w':
        world = input("To create a world of cooperators press 'c', otherwise press 'd', to create two walkers press 'w'\n")
        if world is 'c':
            board = [['c' for i in range(board_dim)] for j in range(board_dim)]
            board[(board_dim-1)//2][(board_dim-1)//2] = 'd'
        elif world is 'd':
            board = [['d' for i in range(board_dim)] for j in range(board_dim)]
            board[(board_dim-1)//2][(board_dim-1)//2] = 'c'
        elif world is 'w':
            board = [['d' for i in range(board_dim)] for j in range(board_dim)]

            mid = (board_dim-1)//2
            board[mid][mid] = 'c'
            board[mid-1][mid] = 'c'
            board[mid-1][mid-1] = 'c'
            board[mid-1][mid+1] = 'c'
            board[mid-1][mid+2] = 'c'
            board[mid+1][mid+2] = 'c'
            board[mid+2][mid+2] = 'c'
            board[mid][mid-1] = 'c'
            board[mid][mid+1] = 'c'
            board[mid][mid+2] = 'c'

            board[mid-1][mid+4] = 'c'
            board[mid-1][mid+5] = 'c'
            board[mid-1][mid+6] = 'c'
            board[mid-1][mid+7] = 'c'
            board[mid-2][mid+4] = 'c'
            board[mid-2][mid+5] = 'c'
            board[mid-2][mid+6] = 'c'
            board[mid-2][mid+7] = 'c'
            board[mid-3][mid+7] = 'c'
            board[mid-4][mid+7] = 'c'
        else:
            print("Invalid Input\n")
