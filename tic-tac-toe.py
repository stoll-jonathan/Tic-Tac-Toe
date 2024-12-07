# Check that the chosen square is empty
def squareIsFree(square, grid):
  row, column = getIndexOfSquare(square)

  if grid[row][column] == ' ':
    return True
  else:
    return False

# Verify that the chosen square is in the correct format
def squareIsValid(square, grid):
  if len(square) != 2:
    return False
  if not square[0].isalpha():
    return False
  if not square[1].isnumeric():
    return False

  row, column = getIndexOfSquare(square)
  return (row >= 0 and row <= 3 and column >= 0 and column <= 3)

# Check to see if the last move has won the game
def gameWon(grid, playerOneTurn):
  if playerOneTurn:
    piece = 'X'
  else:
    piece = 'O'
  
  #check diagonals
  if (grid[0][0] == piece and grid[1][1] == piece and grid[2][2] == piece and grid[3][3] == piece):
    return True
  if (grid[3][0] == piece and grid[2][1] == piece and grid[1][2] == piece and grid[0][3] == piece):
    return True

  #check horizontals
  if (grid[0][0] == piece and grid[0][1] == piece and grid[0][2] == piece and grid[0][3] == piece):
    return True
  if (grid[1][0] == piece and grid[1][1] == piece and grid[1][2] == piece and grid[1][3] == piece):
    return True
  if (grid[2][0] == piece and grid[2][1] == piece and grid[2][2] == piece and grid[2][3] == piece):
    return True
  if (grid[3][0] == piece and grid[3][1] == piece and grid[3][2] == piece and grid[3][3] == piece):
    return True
  
  #check verticals
  if (grid[0][0] == piece and grid[1][0] == piece and grid[2][0] == piece and grid[3][0] == piece):
    return True
  if (grid[0][1] == piece and grid[1][1] == piece and grid[2][1] == piece and grid[3][1] == piece):
    return True
  if (grid[0][2] == piece and grid[1][2] == piece and grid[2][2] == piece and grid[3][2] == piece):
    return True
  if (grid[0][3] == piece and grid[1][3] == piece and grid[2][3] == piece and grid[3][3] == piece):
    return True

  return False

# Convert the square index to an array index
def getIndexOfSquare(square):
  if (square[0].upper() == 'A'):
    column = 0
  elif (square[0].upper() == 'B'):
    column = 1
  elif (square[0].upper() == 'C'):
    column = 2
  elif (square[0].upper() == 'D'):
    column = 3
  else:
    column = 4
  
  row = int(square[1]) - 1

  return row, column

# Place the current player's piece on the chosen square
def placePiece(square, piece):
  row, column = getIndexOfSquare(square)
  grid[row][column] = piece

# Display the current state of the game
def displayGrid(grid):
  print('  A   B   C   D')
  print('1', grid[0][0], '|', grid[0][1], '|', grid[0][2], '|', grid[0][3])
  print(' ---------------')
  print('2', grid[1][0], '|', grid[1][1], '|', grid[1][2], '|', grid[1][3])
  print(' ---------------')
  print('3', grid[2][0], '|', grid[2][1], '|', grid[2][2], '|', grid[2][3])
  print(' ---------------')
  print('4', grid[3][0], '|', grid[3][1], '|', grid[3][2], '|', grid[3][3])

playerOneTurn = True      # Determines the current player
turns = 0                 # Holds the total amount of turns taken (later used to determine a draw)
grid = [                  # Represents the game board
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ']]


# Main loop
while True:
  turns += 1
  displayGrid(grid)

  # Determine the current player and piece
  if (playerOneTurn):
    piece = 'X'
    print("Player 1's Turn")
  else:
    piece = 'O'
    print("Player 2's Turn")
  
  # Take and validate user input
  while (True):
    square = input("Choose a square (ex - a3): ")
    if (squareIsValid(square, grid) and squareIsFree(square, grid)):
      placePiece(square, piece)
      break
    else:
      print("Invalid input")

  # If the last move won the game, announce a winner
  if gameWon(grid, playerOneTurn):
    print('\n')
    displayGrid(grid)
    if (playerOneTurn):
      print("Game Over, Player 1 wins!")
    else:
      print("Game Over, Player 2 wins!")
    break
  
  # If the last move took up the last (16th) square, announce a draw
  elif turns == 16:
    print('\n')
    displayGrid(grid)
    print("Game Over, tie!")
    break

  # Flip current turn and format the output
  playerOneTurn = not playerOneTurn
  print('\n')