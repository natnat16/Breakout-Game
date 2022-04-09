# -*- coding: utf-8 -*-
"""
Wall # Brick Class

Created on Tue Jan 18 19:40:38 2022

@author: ANAT
"""

from turtle import Turtle
from screen_pars import *

W = 2 #  width factor, 40px
L = 4 # length factor, 80px
BRICK_L = L*20
BRICK_W = W*20
N_ROW = WIN_WIDTH//(BRICK_L+10) #11
N_BRICKS = 5*N_ROW #55


# brick second color is used in level 2
BRICKS =  [
            {'color': ['red', 'tomato'], 'points': 1 },
            {'color': ['yellow', 'khaki'], 'points': 2 }, 
            {'color': ['blue', 'royalblue'], 'points': 3 },
            {'color': ['orangered', 'chocolate'], 'points': 5 }, 
            {'color': ['green', 'limegreen'], 'points': 7 }
          ]
                 
INIT_X = -540
INIT_Y = 0
INC_X = 90
INC_Y = 50

class Wall():
    def __init__(self):
        ''' initializing Wall object '''
        self.bricks=[]
        self.create_wall()
        self.reset()
      
    def reset(self): 
        ''' reset wall bricks color and location'''
        self.hits = 0
        for brick in self.bricks:
            loc = brick.get_location()
            brick.goto(loc)
            brick.set_color(1, brick.cidx)
                
    def create_wall(self):
        ''' creating brick wall '''
        c=-1
        y = INIT_Y
        for b in range(N_BRICKS):
            brick = Brick()
            if b%N_ROW==0:
                c+=1
                y += INC_Y
                x = INIT_X                
            x += INC_X
            brick.set_color(1, c)
            brick.set_location(x, y)
            brick.goto(x, y) 
            self.bricks.append(brick)
            
            
    def hit(self):
        ''' counting wall hits by ball '''
        self.hits += 1
                 

class Brick(Turtle):
    def __init__(self):
        ''' initializing Brick object '''
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=W, stretch_len=L) 
        self.is_hit = False
        
        
    def set_color(self, level, c_idx):
        ''' set brick color '''
        l = level-1
        self.cidx = c_idx
        self.color(BRICKS[c_idx]['color'][l])
        
    def set_location(self,x,y):
        ''' set brick coordinates '''
        self.location = (x,y)
        
    def get_location(self):
        ''' get brick coordinates '''
        return self.location
        
    def get_points(self):
        ''' return brick point value '''
        return  BRICKS[self.cidx]['points']
            
    def max_x(self):
        ''' maximal distance hit on the x direction '''
        return BRICK_L//2 + 10

    def max_y(self):
        ''' maximal distance hit on the y direction '''
        return  BRICK_W//2 + 10  

    def remove(self):
        ''' remove brick from screen '''
        self.goto(WIN_WIDTH*2, WIN_HEIGHT*2)
                
    def hit(self):
        ''' tags brick as hit by ball '''
        self.is_hit = True
        
        
    
