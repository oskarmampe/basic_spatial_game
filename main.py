import numpy as np

from board import *



#print('\n'.join([','.join([str(item) for item in row]) for row in board]))

#print(np.matrix(board).shape)

all_neighbours = simulate(1.65, 0, board_dim=300, epochs=64)
