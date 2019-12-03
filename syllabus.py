import pygame

class syllabus:

    def __init__(self, window):
        self.window = window
        self.syllabus = pygame.image.load('nyas/syllabus.png')
        self.coord = (0,0)
        self.exrect = pygame.Rect((165,28),(33,30))

    def blit(self):
        self.window.blit(self.syllabus,self.coord)

    def exclicked(self):
        if pygame.mouse.get_pressed()[0]:
            a,b = pygame.mouse.get_pos()
            if self.exrect.collidepoint(a,b):
                return True
            else:
                return False