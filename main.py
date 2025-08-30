from game import User
from board import Board
from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(width=False, height=False)

#Set Winning Combos
winning_combinations = [
    {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
    {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
    {0, 4, 8}, {2, 4, 6}
]

#Checks winner by checking if a winning combo is contained within the user's moves
def check_winner(user):
    user_moves = user.get_moves()

    if len(user_moves) >= 5:
        display_string.set("It's a draw!")
        return True

    for combo in winning_combinations:
        if combo.issubset(user_moves):
            display_string.set(f"{user.name} is the winner!")
            return True

    return False



def get_current_user():
    if user_1.is_turn:
        return user_1
    if user_2.is_turn:
        return user_2
    return None


def switch_current_user():
    user_1.is_turn = not user_1.is_turn
    user_2.is_turn = not user_2.is_turn

def on_move_played(board_index):
    if board.game_on:
        #Retrives the board square by the index
        square = board.squares[board_index]

        current_user = get_current_user()

        if not square.played:
            #Plays move and appropriately changes the variables
            current_user.add_move(square.board_index)
            square.played = True
            square.text.set(current_user.icon)

            if check_winner(current_user):
                board.game_on = False

    switch_current_user()

    if board.game_on:
        display_string.set(f"{get_current_user().name}'s turn!")

board = Board(callback=on_move_played)
user_1 = User(icon="X", name="Aiden")
user_2 = User(icon="O", name="O-long")
display_string = StringVar()

user_1.is_turn = True
display_string.set(f"{get_current_user().name}'s turn!")


Label(textvariable=display_string).grid(row=4, column=0, columnspan=3)


root.mainloop()



