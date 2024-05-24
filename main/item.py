import pygame

potion = pygame.image.load('imgs/potion.png')
key = pygame.image.load("imgs/key.png")

class item:
    def __init__ (self, x, y, type):
        self.collected = False
        self.x = x
        self.y = y
        self.type = type

    def draw(self,screen):
        if self.collected == False:
            if self.type == "potion":
                screen.blit(potion, (self.x , self.y ), (0, 0, 50, 50))
            elif self.type == "ring":
                screen.blit(key, (self.x, self.y), (0, 0, 50, 50))
        if self.collected == True:
            if self.type == "potion":
                screen.blit(potion, (200, 755 ), (0, 0, 50, 50))
            elif self.type == "ring":
                screen.blit(key, (245, 750 ), (0, 0, 50, 50))
            

    def collect(self):
        self.collected = True
