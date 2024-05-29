from tkinter import *
from functools import partial
import random

FONT = 80
WIDTH = 10
HEIGHT = 5
PADX = 10
PADY = 10
class GameBoardAI:

    def __init__(self, window):
        self.GAME_COUNTER = 0
        self.X_points = 0
        self.O_points = 0


        self.window = Tk()
        self.window.title("Noughts and Crosses")

        self.TL = Button()  ### TL stands for top left. top, middle, bottom, and left, middle and right.
        self.TL.config(text="-", font=FONT, highlightthickness=0, width=WIDTH, height=HEIGHT, command= lambda: self.change_image_on_button(self.TL))
        self.TL.grid(column=0, row=0, padx=PADX, pady=PADY)

        self.TM = Button()  ### TL stands for top left. top, middle, bottom, and left, middle and right.
        self.TM.config(text="-", font=FONT, highlightthickness=0, width=WIDTH, height=HEIGHT, command= lambda: self.change_image_on_button(self.TM))
        self.TM.grid(column=1, row=0, padx=PADX, pady=PADY)

        self.TR = Button()  ### TL stands for top left. top, middle, bottom, and left, middle and right.
        self.TR.config(text="-", font=FONT, highlightthickness=0, width=WIDTH, height=HEIGHT, command= lambda: self.change_image_on_button(self.TR))
        self.TR.grid(column=2, row=0, padx=PADX, pady=PADY)



        self.ML = Button()  ### TL stands for top left. top, middle, bottom, and left, middle and right.
        self.ML.config(text="-", font=FONT, highlightthickness=0, width=WIDTH, height=HEIGHT, command= lambda: self.change_image_on_button(self.ML))
        self.ML.grid(column=0, row=1, padx=PADX, pady=PADY)

        self.MM = Button()  ### TL stands for top left. top, middle, bottom, and left, middle and right.
        self.MM.config(text="-", font=FONT, highlightthickness=0, width=WIDTH, height=HEIGHT, command= lambda: self.change_image_on_button(self.MM))
        self.MM.grid(column=1, row=1, padx=PADX, pady=PADY)

        self.MR = Button()  ### TL stands for top left. top, middle, bottom, and left, middle and right.
        self.MR.config(text="-", font=FONT, highlightthickness=0, width=WIDTH, height=HEIGHT, command= lambda: self.change_image_on_button(self.MR))
        self.MR.grid(column=2, row=1, padx=PADX, pady=PADY)



        self.BL = Button()  ### TL stands for top left. top, middle, bottom, and left, middle and right.
        self.BL.config(text="-", font=FONT, highlightthickness=0, width=WIDTH, height=HEIGHT, command= lambda: self.change_image_on_button(self.BL))
        self.BL.grid(column=0, row=2, padx=PADX, pady=PADY)

        self.BM = Button()  ### TL stands for top left. top, middle, bottom, and left, middle and right.
        self.BM.config(text="-", font=FONT, highlightthickness=0, width=WIDTH, height=HEIGHT, command= lambda: self.change_image_on_button(self.BM))
        self.BM.grid(column=1, row=2, padx=PADX, pady=PADY)

        self.BR = Button()  ### TL stands for top left. top, middle, bottom, and left, middle and right.
        self.BR.config(text="-", font=FONT, highlightthickness=0, width=WIDTH, height=HEIGHT, command= lambda: self.change_image_on_button(self.BR))
        self.BR.grid(column=2, row=2, padx=PADX, pady=PADY)

        self.player_1_score = Label(text=f"player 1, O: {self.O_points}")
        self.player_1_score.grid(column=3, row=0)

        self.player_2_score = Label(text=f"player 2, X: {self.X_points}")
        self.player_2_score.grid(column=3, row=1)

        self.framey = Frame()
        self.restart = Button(self.framey)
        self.restart.config(text="restart", highlightthickness=0, width=WIDTH, height=int(HEIGHT/3), command=self.want_restart)

        self.play_computer = Button(self.framey)
        self.play_computer.config(text="play against computer", highlightthickness=0, width=WIDTH, height=int(HEIGHT/3))  # , command=pass)

        self.framey.grid(column=3, row=2, sticky="nsew")
        self.restart.pack(side="top")
        self.play_computer.pack(side="top")



        self.window.mainloop()

    def ai_turn(self):
        buttons = [self.TL, self.TM, self.TR, self.ML, self.MM,
                        self.MR, self.BL, self.BM, self.BR]
        acceptable_choices = [button for button in buttons if button['text'] == "-"] ##find buttons that AI can press
        ##### need to have something that happens if they draw (AI will have 0 choices)
        random_button = random.choice(acceptable_choices)

        random_button.config(text="X")  ####for now AI always goes last


        self.GAME_COUNTER += 1


    def change_image_on_button(self, button):
        # button.config(text="poop")
        # print("poop")

        if button["text"] != "-":  # can't press a button that has already been pressed
            pass
        else:
            self.GAME_COUNTER += 1
            if self.GAME_COUNTER % 2 != 0:
                button.config(text="O")
                self.ai_turn()   #### AI for now always goes after

            # else:
            #     button.config(text="X")

        self.who_wins()

    def who_wins(self):
        buttons_text = [self.TL["text"], self.TM["text"], self.TR["text"], self.ML["text"], self.MM["text"],
                        self.MR["text"], self.BL["text"], self.BM["text"], self.BR["text"]]

        ##check rows for win conditions
        for i in range(3):
            if buttons_text[(3 * i) + 0] == buttons_text[(3 * i) + 1] == buttons_text[(3 * i) + 2] == "X":
                print("X winner")
                self.if_X_wins()
            elif buttons_text[(3 * i) + 0] == buttons_text[(3 * i) + 1] == buttons_text[(3 * i) + 2] == "O":
                print("O winner")
                self.if_O_wins()

        ##check columns for win conditions

        for i in range(3):
            if buttons_text[i + 3 * 0] == buttons_text[(i) + 3 * 1] == buttons_text[(i) + 3 * 2] == "X":
                print("X winner")
                self.if_X_wins()
            elif buttons_text[(i) + 3 * 0] == buttons_text[(i) + 3 * 1] == buttons_text[(i) + 3 * 2] == "O":
                print("O winner")
                self.if_O_wins()

        ## check diagonals for win conditions

        if buttons_text[0] == buttons_text[4] == buttons_text[8] == "X" or buttons_text[2] == buttons_text[4] == \
                buttons_text[6] == "X":
            print("X winner")
            self.if_X_wins()
        elif buttons_text[0] == buttons_text[4] == buttons_text[8] == "O" or buttons_text[2] == buttons_text[4] == \
                buttons_text[6] == "O":
            print("O winner")
            self.if_O_wins()

    def if_X_wins(self):
        ##this is X winning, so need to add score to X_points, and clean the board
        self.X_points += 1
        self.player_2_score["text"] = f"player 2, X: {self.X_points}"
        self.GAME_COUNTER = 0

        buttons = [self.TL, self.TM, self.TR, self.ML, self.MM, self.MR, self.BL, self.BM, self.BR]
        for button in buttons:
            button["text"] = "-"

    def if_O_wins(self):
        ##this is O winning, so need to add score to O_points, and clean the board
        self.O_points += 1
        self.player_1_score["text"] = f"player 1, O: {self.O_points}"
        self.GAME_COUNTER = 0

        buttons = [self.TL, self.TM, self.TR, self.ML, self.MM, self.MR, self.BL, self.BM, self.BR]
        for button in buttons:
            button["text"] = "-"

    def if_draw(self):      #######haven't checked this
        buttons = [self.TL, self.TM, self.TR, self.ML, self.MM, self.MR, self.BL, self.BM, self.BR]
        button_is_empty = [True if button=="-" else False for button in buttons]
        if all(button_is_empty):   ###means there is a draw state
            for button in buttons:
                button["text"] = "-"
            self.GAME_COUNTER = 0

    def want_restart(self):
        buttons = [self.TL, self.TM, self.TR, self.ML, self.MM, self.MR, self.BL, self.BM, self.BR]
        for button in buttons:
            button["text"] = "-"
        self.O_points = 0
        self.X_points = 0
        self.GAME_COUNTER = 0
        self.player_1_score["text"] = f"player 1, O: {self.O_points}"
        self.player_2_score["text"] = f"player 2, X: {self.X_points}"
