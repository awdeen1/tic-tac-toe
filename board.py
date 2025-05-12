from tkinter import *

class GridSquare:
    def __init__(self, callback, grid_id, rc):
        self.grid_id = grid_id

        self.callback = callback
        self.text = StringVar()
        self.played = False
        self.row_column = rc


        new_button = Button(textvariable=self.text, command=self.on_click, font=("Ariel", 30), width=1, height=1)
        new_button.grid(row=self.row_column[0], column=self.row_column[1])

    def on_click(self):
        self.callback(self)
        self.played = True


