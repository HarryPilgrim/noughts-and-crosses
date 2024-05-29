from UI import GameBoard
from UIAI import GameBoardAI
from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"


#game_board = GameBoard()

#game_board_ai = GameBoardAI()

def play_2_player():
    master.destroy()
    root1= Tk()
    game_board = GameBoard(root1)


def play_ai():
    master.destroy()
    root2= Tk()
    game_board = GameBoard(root2)

master = Tk()
master.title("Noughts and Crosses Homepage")

title = Label(master, text="welcome to ugly Noughts and Crosses", font=(FONT_NAME, 20, "bold"), bg=BACKGROUND_COLOR)
title.grid(column=1, row=0)
master.config(padx=20, pady=20, bg= BACKGROUND_COLOR)

two_player_button = Button(master, width=10)
two_player_button.config(text="2 player", highlightthickness=0, pady=5, command=play_2_player)

two_player_button.grid(column=1, row=1)



ai_button = Button(master, width=10)
ai_button.config(text="play the AI", highlightthickness=0, pady=5, command=play_ai)


ai_button.grid(column=1, row=2)

master.mainloop()