# -*- coding: utf-8 -*-
"""
BreakOut Game

Created on Tue Jan 18 18:30:31 2022

@author: ANAT
"""

import turtle as t
from paddle import Paddle
from ball import Ball
from wall import Wall, N_BRICKS
from scoreboard import ScoreBoard
from time import sleep
from screen_pars import *

### Creating the game window ###
screen= t.Screen()
screen.title("BreakOut Game")
screen.setup(width=WIN_WIDTH, height=WIN_HEIGHT)
screen.bgcolor("black")
screen.cv._rootwindow.resizable(False, False)
screen.tracer(0) # tracer turned off, screen will not refresh/update untill it is told to.

### Generating the paddle, ball, wall & ScoreBoard
scoreboard = ScoreBoard()
paddle = Paddle()
ball= Ball()
wall = Wall()

pause = False

### end & restart game functions
def end_game():
    ''' exits game window, triggered on 'n' keypress '''
    if  scoreboard.is_over():
        t.bye()
    
def new_game():
    ''' starts new game, triggered on 'y'/'Space' keypress '''
    if  scoreboard.is_over():
        scoreboard.reset()
        paddle.reset()
        ball.reset(0, 1) 
        wall.reset()
        play_game()
        
def pause_game():
    ''' pause/unpause game window, triggered on 'space' keypress '''
    global pause
    screen.onkeypress(quit_game, "q")
    if not scoreboard.is_over():
        pause = not pause
        paddle.pause(pause)
        scoreboard.pause_quit(pause)

def quit_game():
    ''' quit game, triggered on 'q' keypress '''
    global pause
    screen.onkeypress(t.bye, "q")
    if not scoreboard.is_over():
        pause = True
        paddle.pause(pause)
        scoreboard.pause_quit(pause, True)
         
                             
# Set movement & answer keys
screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(new_game, "Y")
screen.onkeypress(new_game, "y")
screen.onkeypress(end_game, "N")
screen.onkeypress(end_game, "n")
screen.onkeypress(pause_game, "space")
screen.onkeypress(quit_game, "q")

paddle.ondrag(paddle.mouse_drag)

# playing the game
def play_game():
    ''' Starts game loop '''     
    game_is_on=True
    level = 1
    while game_is_on:
        if pause:
            screen.update()       
        else:       
            screen.update() 
            # changing animation sleep time will affect the ball speed
            sleep(ball.get_speed()) 
            ball.move()
    
            #Detect finish level 1 and move to level 2
            if level == 1 and wall.hits == N_BRICKS:
                sleep(0.3)
                level = 2
                scoreboard.game_start(level)
                wall.reset()
                # level 2 paddle & ball
                paddle.resize()
                ball.reset(0, level)
                continue
                
                                        
            #Detect level 2 game won
            elif level == 2 and wall.hits == 2*N_BRICKS:
               game_is_on = False 
               scoreboard.game_won()
               continue
                 
            #Detect collision with paddle
            if ball.ycor() >= PADDLE_Y:
                if ball.distance(paddle) < paddle.max_dis_mid() and ball.ycor() < PADDLE_Y+25:
                    ball.bounce_top_bottom()
                elif ball.distance(paddle) <= paddle.max_dis_cor() and ball.ycor() < PADDLE_Y+25:  
                    ball.bounce_corners()
                    
            #Detect collision with top wall
            if ball.ycor() > TOP_WALL:
                ball.bounce_top_bottom()
                
            #Detect collision with side walls
            if abs(ball.xcor()) > SIDE_BORDER:
                ball.bounce_sides()                   
                                    
            #Detect lost ball/game over
            if ball.ycor() < PADDLE_Y-15:
                scoreboard.decrease_lives()
                ball.reset(paddle.xcor(), level) 
                if scoreboard.get_lives() == 0:
                    game_is_on = False
                    scoreboard.game_lost()
                           
            #Detect collision with bricks
            for brick in wall.bricks:
                if abs(ball.ycor()-brick.ycor()) <= brick.max_y() and \
                    abs(ball.xcor()-brick.xcor()) <=  brick.max_x():
                        ball.bounce_top_bottom()
                        if level == 1 or brick.is_hit:
                            brick.remove()
                            wall.hit()                    
                            scoreboard.increase_score(brick.get_points())
                        elif level == 2:
                           brick.set_color(level, brick.cidx) 
                           wall.hit()  
                           brick.hit()
                           scoreboard.increase_score(brick.get_points())
                                                       
                  
play_game()
t.done()