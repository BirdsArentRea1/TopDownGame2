import pygame
import math
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3


class Sword:
    def __init__(self, px, py):
        self.xpos = px #set initial position to be the player's position
        self.ypos = py
        self.vx = 0
        self.vy = 0
        self.startTime = 1000
    
        

    def slash(self, ticker):
        self.startTime = ticker
     

    
    def draw(self, screen, px, py, dir, ticker):
        #print(ticker - self.startTime) #print for testing
        if ticker - self.startTime < 15:
            if dir ==RIGHT:
                pygame.draw.rect(screen, (255, 255, 255), (px+30, py+15, 20, 5))
            if dir ==LEFT:
                pygame.draw.rect(screen, (255, 255, 255), (px-25, py+15, 20, 5))
        

    def collide(self, x, y, dir, ex, ey, ticker):
       # print("inside collision")

        if ticker - self.startTime < 15:
          
            #print("dir is", dir)
            if dir ==RIGHT:
                #print("checking sword position", x+30+20, y)
                if x+30+20 > ex: #check if tip of sword to the right of enemy's left edge
                    if x+30+20 <ex+30: #check if top of sword is to the left of enemy's right edge
                        if y+15 > ey: #check if tip of sword is below top of enemy
                            if y+15 < ey+30:
                                print("right hit!", end = " ")
                                return True
            if dir ==LEFT:
                if(x > ex and x - 20 < ex - 20 and y+15 > ey and y +15+5 < ey + 20):
                    print("Hit left")


            #other directions
