# -*- coding: utf-8 -*-
"""
Paddle Class

Created on Tue Jan 18 19:05:50 2022

@author: ANAT
"""

from turtle import Turtle
from screen_pars import *

STEP = 20
W = 1 #  width factor, 20px
L = [8, 5] # length factor, 160px , 120px


PADDLE_W = W*20
POSITION = (PADDLE_X, PADDLE_Y) #(0,-250)

RIGHT_BORDER = WIN_WIDTH/2-10
LEFT_BORDER = -1*RIGHT_BORDER

class Paddle(Turtle):
    def __init__(self):
        ''' initializing Paddle object '''
        super().__init__()
        self.penup()       
        self.speed("fastest")
        self.shape('square')
        self.color('indigo')
        self.reset()

    def reset(self):
        ''' reset paddle shape and position '''
        self.goto(POSITION)
        self.shapesize(stretch_wid=W, stretch_len=L[0]) 
        self.paddle_l = L[0]*20   
        self.is_pause = False

    def pause(self, is_paused):
        ''' set paddle state '''
        self.is_pause = is_paused
                    
    def go_left(self):
        ''' move paddle left with key press '''
        if not self.is_pause:
            edge = self.xcor()-self.paddle_l/2
            if edge > LEFT_BORDER:
                self.bk(STEP)
        
    def go_right(self):
        ''' move paddle right with key press '''
        if not self.is_pause:
            edge = self.xcor()+self.paddle_l/2
            if edge < RIGHT_BORDER:
                self.fd(STEP) 
            
    def mouse_drag(self, x, y):
        ''' move paddle with mouse click & drag. y cor is constant'''
        y=PADDLE_Y
        if not self.is_pause:
            # self.ondrag(None) 
            edge_l = LEFT_BORDER+self.paddle_l/2
            edge_r = RIGHT_BORDER-self.paddle_l/2
            if x < edge_l: 
                self.goto(edge_l, y) 
            elif x > edge_r:   
                self.goto(edge_r, y) 
            else: 
                self.goto(x, y)
            # self.ondrag(self.mouse_drag)           
            
    def max_dis_mid(self):
        ''' maximal distance hit on the paddle middle '''
        return  int( ( (self.paddle_l//2 - 20)**2 +  (PADDLE_W//2 + 10)**2 )**0.5) 

    def max_dis_cor(self):
        ''' maximal distance hit on the paddle corner '''
        return  int( ( (self.paddle_l//2 + 10)**2 +  (PADDLE_W//2 + 10)**2 )**0.5) 

    def resize(self):
        ''' resize paddle for level 2 '''
        self.shapesize(stretch_wid=W, stretch_len=L[1])
        self.paddle_l = L[1]*20
        self.goto(POSITION)
        