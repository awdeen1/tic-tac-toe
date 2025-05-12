from tkinter import StringVar

class User:
    def __init__(self, icon, name):
        self._moves = []
        self.icon = icon
        self.name = name
        self.is_turn = False


    def add_move(self, move):
        self._moves.append(move)

    def get_moves(self):
        return set(self._moves)

class Game:
    def __init__(self, on_win_callback):
        self.game_on = True

        self.on_win_callback = on_win_callback

    def play_move(self, selected_square, user):
        if self.game_on:
            if not selected_square.played:
                user.add_move(selected_square.grid_id)
                selected_square.text.set(user.icon)
                self.check_winner(user)

    def check_winner(self, user):
        winning_combinations = [
            {1, 2, 3}, {4, 5, 6}, {7, 8, 9},
            {1, 4, 7}, {2, 5, 8}, {3, 6, 9},
            {1, 5, 9}, {3, 5, 7}
        ]
        user_moves = user.get_moves()

        for combo in winning_combinations:
            if combo.issubset(user_moves):
                self.on_win_callback(f"{user.name} is the winner!")
                self.game_on = False
                return

        if len(user_moves) == 5:
            self.on_win_callback("It's a draw!")
            self.game_on = False
            return