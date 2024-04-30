import pygame
pygame.init()
pygame.display.set_caption("1")
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
gameover = False
#☻

xpos= 500 
ypos = 200 
vx = 0 
keys = [False, False, False, False] 

xpos = 0
ypos = 0
mousePos = (xpos, ypos)
mouseDown = False

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

#1 is menu, 2 is playing, 3 is credits, 4 is quit, 5 is death screen
state = 1 
button1 = False
button2 = False
button3 = False
quitGame = False

LEFT = 0
RIGHT = 1
DOWN = 2
UP = 3
SPACE = 4
W = 5
ticker = 0

#p1 = player()
#e1 = enemy()
#ball = fireball()

keys = [False, False, False,False,False]

mapNum = 1

