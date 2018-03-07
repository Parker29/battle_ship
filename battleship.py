
from functions import print_board
from functions import random_row
from functions import random_col
board = []

for x in range(0, 5):
  board.append(["O"] * 5)

print_board(board)

ship_row = random_row(board)
ship_col = random_col(board)

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    print_board(board)
  if turn==3:
    print "Game Over"
    answer=raw_input("Would you like to see the location")
    if (answer=="yes" or answer=="Yes"):
        print ship_row
        print ship_col
    else :
        passs
