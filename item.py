import pygame

potion = pygame.image.load('imgs/potion.png')

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
                pygame.draw.circle(screen, (250, 0, 0), (self.x, self.y), 10)
                pygame.draw.circle(screen, (0, 250, 0), (self.x, self.y), 5)
                
        if self.collected == True:
            if self.type == "potion":
                screen.blit(potion, (200, 755 ), (0, 0, 50, 50))
            elif self.type == "ring":
                pygame.draw.circle(screen, (250, 0, 0), (275,775), 10)
                pygame.draw.circle(screen, (0, 250, 0), (275,775), 5)
            

    def collect(self):
        self.collected = True
