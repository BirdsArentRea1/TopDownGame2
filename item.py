import pygame

class item:
    def __init__ (self, x, y, type):
        self.collected = False
        self.x = x
        self.y = y
        self.type = type


    def draw(self,screen):
        if self.collected == False:
            pygame.draw.circle(screen, (250, 0, 0), (self.x, self.y), 10)
            pygame.draw.circle(screen, (250, 250, 0), (self.x, self.y), 5)
            

    def collect(self):
        self.collected = True
