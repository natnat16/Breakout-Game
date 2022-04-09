# -*- coding: utf-8 -*-
"""
ScoreBoard Class
Created on Wed Jan 19 18:57:09 2022

@author: ANAT
"""
from turtle import Turtle
from time import sleep
from screen_pars import *

LEFT = -1*WIN_WIDTH//2 + 20
RIGHT = WIN_WIDTH//2 - 240
TOP = WIN_HEIGHT//2 -50
BOTTOM = -1*WIN_HEIGHT//2 +10
BANNER_POS = (0, -100)

FONT = ('Courier', 30, 'normal')
TITLE = ('Courier', 60, 'bold')
SUBTITLE = ('Courier', 40, 'bold')
MSG = ('Courier', 30, 'bold')

class ScoreBoard(Turtle):
    ''' initializing ScoreBoard object '''
    def __init__(self):
        super().__init__() 
        self.hideturtle()
        self.color("white")
        self.reset()

    def reset(self):
        ''' reseting game '''
        self.score = 0
        self.lives = 3
        self.game_over=False
        self.msg_text = 'pause'
        self.clear()
        self.game_start(1)
            

    def game_start(self, level):
        ''' game start Banner'''
        self.penup()
        self.goto(BANNER_POS)
        self.pendown()
        self.write(f"BREAKOUT\nLevel {level}\n", False, 'center', TITLE)
        self.write("\n\nmove: ← →/click+drag", False, 'center', FONT)
        sleep(0.5)
        self.update_board()
              
             
    def update_board(self):
        ''' update score & lives on scoreboard '''
        self.clear()
        self.penup()
        self.goto(LEFT, TOP)
        self.pendown()
        self.write(f"Score: {self.score}", False, 'left', FONT)  
        self.penup()
        self.goto(RIGHT, TOP)
        self.pendown()
        self.write(f"Lives: {self.lives}", False, 'left', FONT)       
        self.penup()
        self.goto(RIGHT+120, BOTTOM)
        self.pendown()
        self.write(f"press space to {self.msg_text}", False, 'center', ('Courier', 13, 'normal'))
        
    def increase_score(self, points):
        ''' increase score '''
        self.score += points
        self.update_board()
    
    def decrease_lives(self):
        ''' decrease lives by 1 '''
        self.lives -= 1
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write("life lost", False, 'center', MSG)
        sleep(0.5)
        self.update_board()
    
    def get_lives(self):
        ''' returns lives left '''
        return self.lives

    def pause_quit(self, is_paused, is_quit=False):
        ''' game paused/quit banner '''
        if is_paused:
            self.msg_text = 'resume'
            self.update_board()
            self.penup()
            self.goto(BANNER_POS)
            self.pendown()
            if is_quit:
                self.write("Quit Game?\n", False, 'center', SUBTITLE)
                self.write("\n\n  quit- 'q',   resume- 'space'", False, 'center', ('Courier', 20, 'normal'))     
            else:    
                self.write("Paused\n", False, 'center', SUBTITLE)
        else:
            self.msg_text = 'pause'
            self.update_board()  
  
    
    def game_lost(self):
        ''' game lost banner '''
        self.game_over=True
        self.penup()
        self.goto(BANNER_POS)
        self.pendown()
        self.write("GAME OVER\n", False, 'center', TITLE)
        self.write("\n\n  \n  play again Y/N?", False, 'center', SUBTITLE)
         
    def game_won(self):
        ''' game won banner '''
        self.game_over=True
        self.penup()
        self.goto(BANNER_POS)
        self.pendown()
        self.write("YEY YOU WON!\n", False, 'center', TITLE)
        self.write("\n\n  \n  play again Y/N?", False, 'center', SUBTITLE)
        
    def is_over(self):
        ''' returns whether the game is over '''
        return self.game_over
    

  