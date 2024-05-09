import pygame
import math
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5

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
        print(ticker - self.startTime)
        if ticker - self.startTime < 15:
            if dir ==RIGHT:
                pygame.draw.rect(screen, (255, 255, 255), (px+30, py+15, 20, 5))
            if dir ==LEFT:
                pygame.draw.rect(screen, (255, 255, 255), (px-25, py+15, 20, 5))
        

    def collide(self, x, y, ex, ey, ticker):
        if ticker - self.startTime < 15:
            if dir ==RIGHT:
                if (x+30<ex and x+30+20>ex+20 and y+15 > ey and y +15+5 < ey + 20):
                    print("hit right")
            if dir ==LEFT:
                if(x > ex and x - 20 < ex - 20 and y+15 > ey and y +15+5 < ey + 20):
                    print("Hit left")
