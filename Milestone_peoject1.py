#All kinds of functions are bein displayed here..............
    #To print a tic tak toe board
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']   
def display_board(board):
  print('  |    |')
  print(' ' + board[7] + '| ' + board[8] + '  | ' + board[9])
  print('  |    |')
  print('-----------')
  print('  |    |')
  print(' ' + board[4] + '| ' + board[5] + '  | ' + board[6])
  print('  |    |')
  print('-----------')
  print('  |    |')
  print(' ' + board[1] + '| ' + board[2] + '  | ' + board[3])
  print('  |    |')


def player_choice():
   # To assign the markers to the players
  marker=""
  while not (marker =="X" or marker =="O"):
    marker=input("Player1 Do you want to be X or 0:").upper()
    if marker=='X':
      return("X","O")
    else:
      return("O","x")

def place_marker(board,position,marker):
  #To mark the marker on the bard based on the users input
  board[position]=marker

def win_check(board,mark):
  # To define the winning conditions in the game
  return((board[7] == mark and board[8] == mark and board[9] == mark)
  (board[4] == mark and board[5] == mark and board[6] == mark)
  (board[1] == mark and board[2] == mark and board[3] == mark)
  (board[7] == mark and board[5] == mark and board[3] == mark)
  (board[1] == mark and board[5] == mark and board[9] == mark)
  (board[7] == mark and board[4] == mark and board[1] == mark)
  (board[8] == mark and board[5] == mark and board[2] == mark)
  (board[3] == mark and board[6] == mark and board[9] == mark))

import random

def choose_first():
  # To find which player has the first chance
  flip=random.randint(0,1)
  if flip==0:
    return 'player1'
  else:
    return 'player2'

def space_check(board,position):
  #To check whether there is space available in the board
  return board[position]==""    

def full_board_check(board):
 # To check whether the board is full or not
 for i in range(0,10):
    if space_check(board,i):
      return False
      # Since the board is full it returns true
    return True

def player_position(board):
  # For asking the player to choose his next spot in the board
  position=0
  while position not in[1,2,3,4,5,6,7,8,9] or not space_check(board,position):
    position= int(input("Choose your next position:"))
  return position

def replay():
  # To ask whether the players need to play again
  choice= input("Do you want to play again?Enter Yes or No...").upper()
  return choice=="YES" 

#---------------------------------------------------------------------------------------------------------------------

# Main block of code.....

print("Welcome to the Tic Tac Toe")  
while True:
  # Reset the board
  the_Board = [' '] * 10
  player1_marker, player2_marker = player_choice()
  turn = choose_first()
  print(turn + ' will go first.')
    
  play_game = input('Are you ready to play? Enter Yes or No.')
    
  if play_game.lower()[0] == 'y':
    game_on = True
  else:
    game_on = False

  while game_on:
   if turn == 'Player 1':
     # Player1's turn.
            
     display_board(the_Board)
     position = player_choice()
     place_marker(the_Board, player1_marker, position)

     if win_check(the_Board, player1_marker):
       display_board(the_Board)
       print('Congratulations! You have won the game!')
       game_on = False
     else:
       if full_board_check(the_Board):
         display_board(the_Board)
         print('The game is a draw!')
         break
       else:
          turn = 'Player 2'
   else:
     # Player2's turn.
            
     display_board(the_Board)
     position = player_choice()
     place_marker(the_Board, player2_marker, position)

     if win_check(the_Board, player2_marker):
       display_board(the_Board)
       print('Player 2 has won!')
       game_on = False
     else:
       if full_board_check(the_Board):
         display_board(the_Board)
         print('The game is a draw!')
         break
       else:
         turn = 'Player 1'

  if not replay():
    break
  
#breaks out of the while loop since the players have decided not to play the game  



           

