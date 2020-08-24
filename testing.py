import unittest
from board import *

class TestBoard(unittest.TestCase):

    def test_get_neighbour0(self):
        board = ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']

        #edge cases
        neighbours = get_neighbours(board, [1, 1], 4)
        assert neighbours == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]


    def test_get_neighbour1(self):
        board = ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']

        neighbours = get_neighbours(board, [0, 0], 4)
        assert neighbours == [(3, 3), (3, 0), (3, 1), (0, 3), (0, 1), (1, 3), (1, 0), (1, 1)]


    def test_get_neighbour2(self):
        board = ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']

        neighbours = get_neighbours(board, [0, 1], 4)
        assert neighbours == [(3, 0), (3, 1), (3, 2), (0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]
    
    def test_get_neighbour3(self):
        board = ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']

        neighbours = get_neighbours(board, [0, 2], 4)
        assert neighbours == [(3, 1), (3, 2), (3, 3), (0, 1), (0, 3), (1, 1), (1, 2), (1, 3)]
    
    def test_get_neighbour4(self):
        board = ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']

        neighbours = get_neighbours(board, [1, 0], 4)
        assert neighbours == [(0, 3), (0, 0), (0, 1), (1, 3), (1, 1), (2, 3), (2, 0), (2, 1)]
    
    def test_get_neighbour5(self):
        board = ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']

        neighbours = get_neighbours(board, [1, 2], 4)
        assert neighbours == [(0, 1), (0, 2), (0, 3), (1, 1), (1, 3), (2, 1), (2, 2), (2, 3)]

    def test_get_neighbour6(self):
        board = ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']

        neighbours = get_neighbours(board, [2, 0], 4)
        assert neighbours == [(1, 3), (1, 0), (1, 1), (2, 3), (2, 1), (3, 3), (3, 0), (3, 1)]

    def test_get_neighbour7(self):
        board = ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']

        neighbours = get_neighbours(board, [2, 1], 4)
        assert neighbours == [(1, 0), (1, 1), (1, 2), (2, 0), (2, 2), (3, 0), (3, 1), (3, 2)]
    
    def test_get_neighbour8(self):
        board = ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']

        neighbours = get_neighbours(board, [2, 2], 4)
        assert neighbours == [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)]

    def test_get_payoff_values(self):
        board = [['c' for i in range(3)] for j in range(3)]
        board[1][1] = 'd'
        payoff_matrix = [[1, 0], [1.65, 0]]
        payoff_values = get_payoff_values(board, payoff_matrix, 3)
        assert payoff_values == [[('c', 7), ('c', 7), ('c', 7)], [('c', 7), ('d', 13.200000000000001), ('c', 7)], [('c', 7), ('c', 7), ('c', 7)]]

if __name__ == '__main__':
    unittest.main()