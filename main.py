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


#3 user test
user_1 = {"name": "Aiden", "icon": "X", "moves": [], "is_turn": True, "won": False}
user_2 = {"name": "O-Ring", "icon": "O", "moves": [], "is_turn": False, "won": False}
user_3 = {"name": "Test", "icon": "P", "moves": [], "is_turn": False, "won": False}

all_users = [user_1, user_2, user_3]

def get_current_user(users):
    for user in users:
        if user['is_turn']:
            return user
    return None

def switch_current_user(users):
    current_user = get_current_user(users)
    next_user_index = users.index(current_user) + 1 % len(users)
    next_user = users[next_user_index]

    current_user['is_turn'] = False
    next_user['is_turn'] = True

#Checks winner by checking if a winning combo is contained within the user's moves
def check_winner(user):
    if all(square.cget('text') != "" for square in board):
        #Draw
        for user in all_users:
            user['won'] = True

    for combo in winning_combinations:
        if combo.issubset(set(user["moves"])):
            user['won'] = True



def on_move_played(index, users):
    #Retrives the board square by the index
    square = board[index]
    current_user = get_current_user(users=all_users)

    if not any(user['won'] for user in users):
        #Plays move and appropriately changes the variables
        if len(square.cget('text')) == 0:
            current_user['moves'].append(index)
            square.configure(text=current_user['icon'])
            check_winner(current_user)

            if all(user['won'] for user in users):
                display_string.set("It's a draw!")
            elif any(user['won'] for user in users):
                display_string.set(f"{current_user['name']} is the winner!")
            else:
                switch_current_user(users=all_users)
                display_string.set(f"{get_current_user(users=all_users)['name']}'s turn!")




board = []
board_index = 0

for row in range(3):
    for column in range(3):
        def on_click(current_index=board_index):
            on_move_played(current_index, users=all_users)

        new_button = Button(text="", command=on_click,
                            font=("Ariel", 30), width=1, height=1)
        new_button.grid(column=column, row=row)
        board.append(new_button)

        board_index +=1


display_string = StringVar()
display_string.set(f"{get_current_user(users=all_users)['name']}'s turn!")


Label(textvariable=display_string).grid(row=4, column=0, columnspan=3)

root.mainloop()



