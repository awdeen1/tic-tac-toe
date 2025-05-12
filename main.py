from game import Game, User
from board import GridSquare
from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(width=False, height=False)

user_1 = User(icon="X", name="Aiden")
user_2 = User(icon="O", name="O-long")
display_string = StringVar()

game = Game(on_win_callback=display_string.set)

def get_current_user():
    if user_1.is_turn:
        return user_1
    if user_2.is_turn:
        return user_2

def switch_current_user():
    user_1.is_turn = not user_1.is_turn
    user_2.is_turn = not user_2.is_turn

def on_move_played(square):
    game.play_move(selected_square=square, user=get_current_user())
    switch_current_user()
    if game.game_on:
        display_string.set(f"{get_current_user().name}'s turn!")

user_1.is_turn = True
display_string.set(f"{get_current_user().name}'s turn!")

GridSquare(rc=(1, 1), grid_id=1, callback=on_move_played)
GridSquare(rc=(1, 2), grid_id=2, callback=on_move_played)
GridSquare(rc=(1, 3), grid_id=3, callback=on_move_played)

GridSquare(rc=(2, 1), grid_id=4, callback=on_move_played)
GridSquare(rc=(2, 2), grid_id=5, callback=on_move_played)
GridSquare(rc=(2, 3), grid_id=6, callback=on_move_played)

GridSquare(rc=(3, 1), grid_id=7, callback=on_move_played)
GridSquare(rc=(3, 2), grid_id=8, callback=on_move_played)
GridSquare(rc=(3, 3),  grid_id=9, callback=on_move_played)

Label(textvariable=display_string).grid(row=4, column=0, columnspan=3)

root.mainloop()



