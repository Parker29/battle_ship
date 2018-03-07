from random import randint
def print_board(board):
  for row in board:
    print " ".join(row)
def random_row(board):
  return randint(0, len(board) - 1)
def random_col(board):
  return randint(0, len(board[0]) - 1)
