from game import TicTacToe
from os import system
from time import sleep

tic_tac_toe = TicTacToe()

while tic_tac_toe.winner is False:
      sleep(2)
      system('clear')

      tic_tac_toe.print_board()
      user_input = input(f"{tic_tac_toe.current_user.name}, type any number between 1 and 9 to play that square! ")
      #Tests if the user input is a member of the tic-tac-toe dictionary, retries input otherwise.
      while user_input not in tic_tac_toe.board:
            user_input = input("Try that again! ")

      #Function takes the user move and current user
      tic_tac_toe.play_move(move=user_input, user=tic_tac_toe.current_user)





