from tictactoe import Board
# from tictactoe import Move
from tictactoe.egtb import Reader
from tictactoe.egtb import Generator
import functools
import operator


dimensions = (4, 3)
total_squares = functools.reduce(operator.mul, dimensions)
for index in reversed(range(total_squares + 1)):
    Generator(dimensions, 3, index)

reader = Reader((3, 3), 3, 2)
board = Board((3, 3), 3)
board.push((0, 0))
board.push((0, 1))
print(reader.index(board))
