from tkinter import StringVar

class User:
    def __init__(self, icon, name):
        self._moves = []
        self.icon = icon
        self.name = name
        self.is_turn = False


    def add_move(self, user):
        self._moves.append(user)

    def get_moves(self):
        return set(self._moves)

