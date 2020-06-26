import matplotlib.pyplot as plt

def get_neighbours(board, idx, board_dim):
    #CHECK IF IDX IS 0 THEN 99 IF >99 THEN 0
    neighbours = []
    neighbours_idx = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i in neighbours_idx:
        first = idx[0] + i[0]
        second = idx[1] + i[1]

        # Wrap Around to a torus-like structure
        if first < 0:
            first = board_dim-1
        elif first > board_dim-1:
            first = 0

        if second < 0:
            second = board_dim-1
        elif second > board_dim-1:
            second = 0

        neighbours.append((first, second))
    
    return neighbours

def play_with_neighbours(player, neighbours, payoff_matrix):
    player_strat = 0 if player == 'c' else 1
    sums = 0
    for neighbour in neighbours:
        enemy_strat = 0 if neighbour == 'c' else 1
        sums += payoff_matrix[player_strat][enemy_strat]
    return sums


def create_plot(board, board_dim):
    image = [[(-1,-1,-1) for _ in range(board_dim)] for _ in range(board_dim)]
    for i,row in enumerate(board):
        for j,col in enumerate(row):
            image[i][j] = [255,0,0] if col == 'd' else [0,0,255]
    plt.imshow(image)
    plt.show()



def get_payoff_values(board, payoff_matrix, board_dim):
    payoff_board = [[('-',-9999) for _ in range(board_dim)] for _ in range(board_dim)]
    for i,row in enumerate(board):
        for j,item in enumerate(row):
            player_idx = (i,j)
            player = item
            neighbours = get_neighbours(board, player_idx, board_dim)
            players = [board[idx[0]][idx[1]] for idx in neighbours]
            cell_sum = play_with_neighbours(player, players, payoff_matrix)
            payoff_board[i][j] = (board[i][j], cell_sum)
    return payoff_board
        
def update_board(board, board_dim):
    new_board = [['-' for _ in range(board_dim)] for _ in range(board_dim)]
    for i,row in enumerate(board):
        for j,col in enumerate(row):
            player = (i,j)
            strat, payoff = col
            neighbours = get_neighbours(board, player, board_dim)
            best_payoff = -9999
            best_neighbour = None
            for neighbour in neighbours:
                neigh_strat, neigh_payoff = board[neighbour[0]][neighbour[1]]
                if neigh_payoff > best_payoff:
                    best_neighbour = neigh_strat
                    best_payoff = neigh_payoff
            new_board[i][j] = strat if payoff > best_payoff else best_neighbour


    return new_board


def simulate(b, epsilon, board_dim=100, epochs=1):
    #board = [[(j*5)+i for i in range(5)] for j in range(5)]
    board = [['c' for i in range(board_dim)] for j in range(board_dim)]
    board[(board_dim-1)//2][(board_dim-1)//2] = 'd'
    #print('\n'.join([','.join([str(item) for item in row]) for row in board]))
    #all_neighbours = get_neighbours(board, (0, 0), board_dim=board_dim)
    payoff_matrix = [[1, 0], [b, epsilon]]
    for epoch in range(epochs):
        print('-------------------------START OF EPOCH %d-------------------------' % (epoch+1))
        payoff_board = get_payoff_values(board, payoff_matrix, board_dim)
        # print('\n'.join([','.join([str(item) for item in row]) for row in payoff_board]))
        board = update_board(payoff_board, board_dim)
        # print('--------------------------------- EPOCH %d ---------------------------------' % (epoch+1))
        # print('\n'.join([','.join([str(item) for item in row]) for row in board]))
        # print('--------------------------------- END OF EPOCH %d ---------------------------------' % (epoch+1))
        print('-------------------------END OF EPOCH %d-------------------------' % (epoch+1))
    create_plot(board, board_dim)

    #print('\n'.join([','.join([str(item) for item in row]) for row in board]))
    # print("----------------------IDX----------------------")
    # print('\n'.join([','.join([str(item) for item in row]) for row in board]))
    # print("----------------------END IDX----------------------")
    
    # print("----------------------IDX----------------------")
    # print(board[0][0])
    # print("----------------------END IDX----------------------")

    # print("----------------------NEIGHBOURS----------------------")
    # print(all_neighbours)
    # print("----------------------NEIGHBOURS----------------------")

    # for i in all_neighbours:
    #     print(board[i[0]][i[1]])


