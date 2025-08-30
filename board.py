from tkinter import *

class GridSquare:
     def __init__(self, row, column, on_play, board_index):
        self.text = StringVar()

        self.played = None
        self.board_index = board_index

        self.on_play = on_play

        self.row, self.column = row, column
        new_button = Button(textvariable=self.text, command=self.on_click, font=("Ariel", 30), width=1, height=1)
        new_button.grid(row=self.row, column=self.column)


     def on_click(self):
        self.on_play(self.board_index)


class Board:
    def __init__(self, callback):
        self.callback = callback
        self.game_on = True

        self.squares = []
        self.square_index = 0

        for row in range(3):
            for column in range(3):
                self.new_gridsquare(row=row, column=column, index=self.square_index)
                self.square_index +=1


    def new_gridsquare(self, row, column, index):
        self.squares.append(GridSquare(on_play=self.callback, row=row, column=column, board_index=index))


