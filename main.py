from game import User
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

def on_move_played(index):

    if not user_2.won and not user_1.won:
        #Retrives the board square by the index
        square = board[index]

        current_user = get_current_user()

        if len(square.cget('text')) == 0:
            #Plays move and appropriately changes the variables
            current_user.add_move(index)
            square.configure(text=current_user.icon)

            if check_winner(current_user):
                print('yes')
                current_user.won = True

    switch_current_user()

    if not user_2.won and not user_1.won:
        display_string.set(f"{get_current_user().name}'s turn!")

board = []
board_index = 0
for row in range(3):
    for column in range(3):
        def on_click(current_index=board_index):
            on_move_played(current_index)

        new_button = Button(text="", command=on_click,
                            font=("Ariel", 30), width=1, height=1)
        new_button.grid(column=column, row=row)
        board.append(new_button)

        board_index +=1


user_1 = User(icon="X", name="Aiden")
user_2 = User(icon="O", name="O-long")
display_string = StringVar()

user_1.is_turn = True
display_string.set(f"{get_current_user().name}'s turn!")


Label(textvariable=display_string).grid(row=4, column=0, columnspan=3)


root.mainloop()



