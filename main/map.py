import pygame
from player2 import player
from item import item
from fireball2 import fireball
from sword import Sword
from enemy2 import enemy
import math
pygame.init()
pygame.display.set_caption("top down game")
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
gameover = False
#☻

font = pygame.font.Font('freesansbold.ttf', 32)

#die = pygame.mixer.Sound('LegoYodaDeath.mp3')
#boom = pygame.mixer.Sound('VineBoom.mp3')
#warp = pygame.mixer.Sound("smb_pipe.wav")

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
green1 = (39, 154, 27)
green2 = (54, 178, 41)
yellow1 = (250, 228, 39)
yellow2 = (254, 241, 132)
red1 = (213, 6, 6)
red2 = (244, 45, 45)

#1 is menu, 2 is playing, 3 is credits, 4 is quit, 5 is death screen
state = 1 
button1 = False
button2 = False
button3 = False
quitGame = False

#CONSTANTS
LEFT = 0
RIGHT = 1
DOWN = 2
UP = 3
SPACE = 4
W = 5
ticker = 0

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
        

p1 = player()
e1 = enemy()
ball = fireball()
andrew = Sword(p1.xpos, p1.ypos)
items = [item(100, 400, 'potion'), item(200, 400, 'ring')]

keys = [False, False, False,False,False]

mapNum = 1

map = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4],
       [2,2,2,2,3,2,2,2,3,2,2,2,2,2,3,2,2,2,2,4],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4], 
       [2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,4],
       [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
       [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,10],
       [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,10],
       [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
       [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
       [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
       [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
       [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
'''''
map2 = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,2], 
       [2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,1,1,1,2],
       [2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,2],
       [5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2],
       [5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,1,1,1,2,2,2,2,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
'''''
map2 = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,8,8,8,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,8,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,8,8,8,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,8,1,1,1,1,1,1,1,1,1,1,1,2], 
       [2,1,1,1,1,1,1,8,8,8,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,9],
       [5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,9],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

map3 = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,8,8,8,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,8,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,8,8,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,8,1,1,1,1,1,1,1,1,2], 
       [2,1,1,1,1,1,1,8,8,8,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5],
       [9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

brick = pygame.image.load('imgs/stonebrick1.png') #2
brick2 = pygame.image.load('imgs/stonebrickright.png') #4
brick3 = pygame.image.load('imgs/stonebrickleft.png') #6
brick4 = pygame.image.load('imgs/stonebrickdown.png') #7
window = pygame.image.load('imgs/stonebrickwindow.png') #3
floor = pygame.image.load('imgs/woodplank1.png') #1
#door is 5
text1 = font.render('Start',False,(0,0,0))
text2 = font.render('Exit',False,(0,0,0))
text3 = font.render('Credits',False,(0,0,0))
text4 = font.render('Made by Ewan',False,(0,0,0))

while not gameover:#GAMELOOP############################################################################################################
    clock.tick(60)
    ticker += 1
#INPUT----------------------------------------------------------------------------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True
            if event.key == pygame.K_SPACE:
                keys[SPACE] = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            if event.key == pygame.K_SPACE:
                keys[SPACE] = False
                
        #keeps track of mouse position
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
            
        #keeps track of mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
            #print("mouse button down detected!")
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        
        #keyboard input
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q:
                quitGame = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                quitGame = False


    #PHYSICS--------------------------------------------------------------------------------------------------------------------------------
    #print(mousePos)
    if state == 2 and mouseDown == True:
        #print("hello!")
        andrew.slash(ticker)
    if mapNum == 1:
        p1.move(keys, map)
    elif mapNum == 2:
        p1.move(keys, map2)
    elif mapNum == 3:
        p1.move(keys, map3)
    if mapNum == 1 or 2 or 3:
        if e1.isAlive == True:
             #e1.move(map, ticker, p1.xpos, p1.ypos)
            e1.die(ball.xpos, ball.ypos, andrew.collide(p1.xpos, p1.ypos, p1.direction, e1.xpos, e1.ypos, ticker))
            p1.ouch(e1.xpos, e1.ypos)


    #if e1.die == True:
        #pygame.mixer.Sound.play(boom)
    
    if p1.health <= 0:
        state = 5
    #move between maps 1-2
    if mapNum == 1:
        if map[int((p1.ypos)/50)][int((p1.xpos)/50)] == 10:
            print(p1.inventory)
            for i in range(len(p1.inventory)):
                if p1.inventory[i].type=="ring":
                    print("setting door to open")
                    map[8][19] = 5
                    map[9][19] = 5
                print("unlocking door!")
        elif map[int((p1.ypos)/50)][int((p1.xpos)/50)] == 10:
            print("door is locked!")

        if map[int((p1.ypos)/50)][int((p1.xpos)/50)] == 5:
            mapNum = 2
            #pygame.mixer.Sound.play(warp)
            p1.xpos = 50
    if mapNum == 2:
        if map2[int((p1.ypos)/50)][int((p1.xpos)/50)] == 9:
            mapNum = 3
            #pygame.mixer.Sound.play(warp)
            p1.xpos = 930


    #move between 2-3
    if mapNum == 2:
        if map2[int((p1.ypos)/50)][int((p1.xpos)/50)] == 9:
            mapNum = 2
            #pygame.mixer.Sound.play(warp)
            p1.xpos = 50
    if mapNum == 3:
        if map3[int((p1.ypos)/50)][int((p1.xpos)/50)] == 5:
            mapNum = 1
            #pygame.mixer.Sound.play(warp)
            p1.xpos = 930
    if ball.isAlive == True:
        ball.move()
    if keys[SPACE] == True:
            ball.shoot(p1.xpos, p1.ypos, p1.direction)

    #collect items
    for i in items:
        #print(dist(p1.xpos, p1.ypos, i.x, i.y))
        if i.collected == False and dist(p1.xpos, p1.ypos, i.x, i.y)<30:
            p1.collect_item(i)
            for j in range (len(items)):
                if items[j].type == "potion" and items[j].collected == True:
                    print("potion collected")
                if items[j].type == "ring" and items[j].collected == True:
                    print("key collected")

    #state 1: menu state!------------------------------
    if state == 1 and mousePos[0]>100 and mousePos[0]<300 and mousePos[1]>400 and mousePos[1]<550:
        button1 = True
    else:
        button1 = False
        
    if state == 1 and mousePos[0]>400 and mousePos[0]<600 and mousePos[1]>400 and mousePos[1]<600:
        button2 = True
    else:
        button2 = False
        
    if state == 1 and mousePos[0]>700 and mousePos[0]<898 and mousePos[1]>400 and mousePos[1]<600:
        button3 = True
    else:
        button3 = False
            
    if state == 1 and button1 == True and mouseDown == True:
        state = 2
    
    if state == 1 and button2 == True and mouseDown == True:
        state = 3
        
    if state == 1 and button3 == True and mouseDown == True:
        state = 4
    #state 2: playing state!---------------------------
    if state == 2 and quitGame == True: #pressing quit takes you back to menu
        state = 1
    if state == 3 and quitGame == True: #pressing quit takes you back to menu
        state = 1
    if state == 4 and quitGame == True: #pressing quit takes you back to menu
        state = 1

    #RENDER---------------------------------------------------------------------------------------------------------------------------------

    screen.fill((0,0,0))

    if state == 1:
        screen.fill((70,70,255))

    for i in items:
        i.draw(screen)        
        
        if button1 == False:
            pygame.draw.rect(screen, (green1), (100, 400, 200, 150))
            screen.blit(text1, (160,450))
        else:
            pygame.draw.rect(screen, (green2), (100, 400, 200, 150))
            screen.blit(text1, (160,450))
            
        if button2 == False:
            pygame.draw.rect(screen, (yellow1), (400, 400, 200, 150))
            screen.blit(text3, (440,450))
        else:
            pygame.draw.rect(screen, (yellow2), (400, 400, 200, 150))
            screen.blit(text3, (440,450))

        #repeat for third button
        if button3 == False:
            pygame.draw.rect(screen, (red1), (700, 400, 200, 150))
            screen.blit(text2, (765,450))
        else:
            pygame.draw.rect(screen, (red2), (700, 400, 200, 150))
            screen.blit(text2, (765,450))


       
    #game state-------------------------------
    if state == 2:
        if mapNum == 1:
            screen.fill((80,150,100))# Clear the screen green
            for i in range(len(map)):
                for j in range(len(map[i])):
                    if map[i][j] == 1:
                        screen.blit(floor, (j * 50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 2:
                        screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 3:
                        screen.blit(window, (j * 50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 4:
                        screen.blit(brick2, (j * 50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 5: #unlocked door
                        pygame.draw.rect(screen, (0,0,0), (j*50, i*50, 50, 50))
                    if map[i][j] == 6:
                        screen.blit(brick3, (j * 50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 7:
                        screen.blit(brick4, (j * 50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 10: #locked door
                        pygame.draw.rect(screen, (255,255,255), (j*50, i*50, 50, 50))
                    

        elif mapNum == 2:
            screen.fill((80,150,100))
            for i in range(len(map2)):
                for j in range(len(map2[i])): 
                    if map2[i][j] == 1:
                        screen.blit(floor, (j * 50, i * 50), (0, 0, 50, 50))
                    if map2[i][j] == 2:
                        screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
                    if map2[i][j] == 5:
                        pygame.draw.rect(screen, (0,0,0), (j*50, i*50, 50, 50))
                    if map2[i][j] == 6:
                        pygame.draw.rect(screen, (0,0,0), (j*50, i*50, 50, 50))
                    if map[i][j] == 8:
                        pygame.draw.rect(screen, (255,0,0), (j*50, i*50, 50, 50))
                    if map2[i][j] == 9:
                        pygame.draw.rect(screen, (0,0,0), (j*50, i*50, 50, 50))

        elif mapNum == 3:
            screen.fill((80,150,100))
            for i in range(len(map3)):
                for j in range(len(map2[i])):
                    if map3[i][j] == 1:
                        screen.blit(floor, (j * 50, i * 50), (0, 0, 50, 50))
                    if map3[i][j] == 2:
                        screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 3:
                        screen.blit(window, (j * 50, i * 50), (0, 0, 50, 50))
                    if map3[i][j] == 5:
                        pygame.draw.rect(screen, (0,0,0), (j*50, i*50, 50, 50))
                    if map3[i][j] == 6:
                        pygame.draw.rect(screen, (0,0,0), (j*50, i*50, 50, 50))
                    if map[i][j] == 8:
                        pygame.draw.rect(screen, (255,0,0), (j*50, i*50, 50, 50))
                    if map2[i][j] == 9:
                        pygame.draw.rect(screen, (0,0,0), (j*50, i*50, 50, 50))
                
        p1.draw(screen)
        e1.draw(screen)
        if ball.isAlive == True:
            ball.draw(screen)
        andrew.draw(screen, p1.xpos, p1.ypos, p1.direction, ticker)
        
        for i in items:
            i.draw(screen)
        
         #health bar
        pygame.draw.rect(screen, (255, 255, 255), (750, 5, 200, 30))
        pygame.draw.rect(screen, (150, 0, 0), (750, 5, p1.health, 30))
        pygame.draw.rect(screen, (0,0,0), (750, 5, 200, 30), 3)
    
    if state == 3:
        screen.fill((200,200,200))
        screen.blit(text4, (60,100))
        
    if state == 4:
        gameover = True

    if state == 5:
        screen.fill((250,0,0))
        #pygame.mixer.Sound.play(die)

    pygame.display.flip()

#GAME LOOP END##########################################################################################################################
pygame.quit()
