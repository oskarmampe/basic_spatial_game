import matplotlib.pyplot as plt
import os
from time import gmtime, strftime


'''
    Takes in a board of any square dimension, and gets all the neighbours of a cell.
    Cells around the edge are wrapped around to create a toroid like shape.
'''
def get_neighbours(board, idx, board_dim):
    neighbours = []

    # Create an array of the positions of neighbours relative to the current cell.
    # For example, (-1, -1) represents the neighbour that is 1 to the left and 1 down from the current cell.
    neighbours_idx = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i in neighbours_idx:
        # Put the row and col indices into a variable to check if they're on the boundary.
        row = idx[0] + i[0]
        col = idx[1] + i[1]

        # Wrap around to a torus-like structure by creating circular connections
        # For example, for a row, if there's no neighbour to the left, go to the last cell in that row.
        # Similar logic applies to columns.
        if row < 0:
            row = board_dim-1
        elif row > board_dim-1:
            row = 0

        if col < 0:
            col = board_dim-1
        elif col > board_dim-1:
            col = 0

        neighbours.append((row, col))
    
    return neighbours

'''
    Play the spatial game with the cell's neighbours. Currently, only cooperator/defector strategy is used.
'''
def play_with_neighbours(player, neighbours, payoff_matrix):
    player_strat = 0 if player == 'c' else 1
    sums = 0
    for neighbour in neighbours:
        enemy_strat = 0 if neighbour == 'c' else 1
        sums += payoff_matrix[player_strat][enemy_strat]
    return sums

'''
    For simplicity, a matplotlib is created to represent the cells' state.
'''
def create_plot(board, old_board, board_dim, file_name, t):
    image = [[[-1,-1,-1] for _ in range(board_dim)] for _ in range(board_dim)]
    for i,row in enumerate(board):
        for j,col in enumerate(row):
            last_cell = old_board[i][j]
            if last_cell is 'd' and col is 'd':
                image[i][j] = [255,0,0]
            elif last_cell is 'd' and col is 'c':
                image[i][j] = [0,255,0]
            elif last_cell is 'c' and col is 'c':
                image[i][j] = [0,0,255]
            elif last_cell is 'c' and col is 'd':
                image[i][j] = [255,255,0]
    plt.figure(num=None, figsize=(20, 18), dpi=100, facecolor='w', edgecolor='k')
    plt.axis("off")
    plt.imshow(image)
    plt.savefig("%s/%d" % (file_name, t+1))
    plt.close()

'''
    Create a new board, but along with the cell's strategy, it's payoff value is also recorded.
'''
def get_payoff_values(board, payoff_matrix, board_dim):
    # Preload an array with tuples representing the strategy and it's payoff. 
    payoff_board = [[('-',-9999) for _ in range(board_dim)] for _ in range(board_dim)]
    for i,row in enumerate(board):
        for j,item in enumerate(row):
            # Get the player index and strategy
            player_idx = (i,j)
            player = item
            # Get all the neighbours indices
            neighbours = get_neighbours(board, player_idx, board_dim)
            # Get all neighbour strategies
            players = [board[idx[0]][idx[1]] for idx in neighbours]
            # Get the payoff of the cell
            cell_sum = play_with_neighbours(player, players, payoff_matrix)
            payoff_board[i][j] = (board[i][j], cell_sum)
    return payoff_board

'''
    Update the board, which requires a board with the strategies and payoffs.
'''
def update_board(board, board_dim):
    new_board = [['-' for _ in range(board_dim)] for _ in range(board_dim)]
    for i,row in enumerate(board):
        for j,col in enumerate(row):
            # Get the cell index and strategy & payoff
            player = (i,j)
            strat, payoff = col
            # Get all of the neighbours
            neighbours = get_neighbours(board, player, board_dim)
            
            # Loop around all the neighbours and find the maximum of the neighbours
            best_payoff = -9999
            best_neighbour = None
            for neighbour in neighbours:
                neigh_strat, neigh_payoff = board[neighbour[0]][neighbour[1]]
                if neigh_payoff > best_payoff:
                    best_neighbour = neigh_strat
                    best_payoff = neigh_payoff
            new_board[i][j] = strat if payoff > best_payoff else best_neighbour

    return new_board

'''
    Simulate the spatial game according to Nowak's example.
'''
def simulate(b, epsilon, board, board_dim=100, time=1, verbose=False):
    if verbose:
        print('\n'.join([','.join([str(item) for item in row]) for row in board]))
    payoff_matrix = [[1, 0], [b, epsilon]]
    file_name = strftime("%Y_%m_%d_%H_%M_%S", gmtime())
    if not os.path.isdir(file_name):
        os.makedirs(file_name)
    for t in range(time):
        old_board = [[item for item in row] for row in board]
        print('-------------------------START OF t %d-------------------------' % (t+1))
        payoff_board = get_payoff_values(board, payoff_matrix, board_dim)
        if verbose:
            print('\n'.join([','.join([str(item) for item in row]) for row in payoff_board]))
        board = update_board(payoff_board, board_dim)
        if verbose:
            print('--------------------------------- t %d ---------------------------------' % (t+1))
            print('\n'.join([','.join([str(item) for item in row]) for row in board]))
            print('--------------------------------- END OF t %d ---------------------------------' % (t+1))
        print('-------------------------END OF t %d-------------------------' % (t+1))
        create_plot(board, old_board, board_dim, file_name, t)
        print('-------------------------SAVED IN %s/%d-------------------------' % (file_name,t+1))

    if time is 0:
        old_board = [[item for item in row] for row in board]
        create_plot(board, old_board, board_dim, file_name, time)

    if verbose:
        print("----------------------IDX----------------------")
        print('\n'.join([','.join([str(item) for item in row]) for row in board]))
        print("----------------------END IDX----------------------")
        
        print("----------------------IDX----------------------")
        print(board[0][0])
        print("----------------------END IDX----------------------")
