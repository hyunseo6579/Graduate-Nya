import pygame


def main():

    pygame.init()
    window = pygame.display.set_mode((750,500))
    run = True
    frame = 0

    title = titlepage(window)
    mainpg = mainpage(window)

    while run:
        pygame.time.delay(50)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        window.fill((255, 255, 255))

        if frame == 0:
            title.blit()
            if title.clicked():
                frame += 1

        elif frame == 1:
            mainpg.blit()

        pygame.display.update()


class titlepage:

    def __init__(self,window):
        self.titlecat = pygame.image.load('nyas/cat_title.png')
        self.startbutton = pygame.image.load('nyas/start.png')
        self.window = window
        self.windowsz = window.get_size()
        self.catcoord = ((self.windowsz[0]-541)/2,0)
        self.strtcoord = ((self.windowsz[0]-200)/2,(self.windowsz[1]/5)*4)
        self.strtRect = pygame.Rect(self.strtcoord, (200, 70))

    def blit(self):
        self.window.blit(self.titlecat,self.catcoord)
        self.window.blit(self.startbutton,self.strtcoord)

    def clicked(self):
        if pygame.mouse.get_pressed()[0]:
            a,b = pygame.mouse.get_pos()
            if self.strtRect.collidepoint(a,b):
                return True
            else:
                return False


class mainpage:

    def __init__(self,window):
        self.window = window
        self.windowsz = window.get_size()
        self.catframes = []
        for i in range(5):
            self.catframes.append(pygame.image.load('nyas/cat'+str(i+1)+'.png'))
        self.i = 0  # for cat frames

    def blit(self):
        i = self.i % 5  # switch image every update
        self.window.blit(self.catframes[i], (self.windowsz[0]/3,self.windowsz[1]/5))
        self.i = i + 1


main()