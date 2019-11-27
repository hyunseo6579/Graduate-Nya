import pygame


def main():

    pygame.init()
    window = pygame.display.set_mode((750,500))
    run = True
    frame = 0
    date = 1  # d-1. puzzle changes from assignment to exam depending on the date

    title = titlepage(window)
    mainpg = mainpage(window,date)

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
            mainpg.draw()
            mainpg.blit()
            mainpg.showtext(date)

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

        self.test = pygame.image.load('nyas/calender.png')

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

    def __init__(self,window,date):
        self.black = (0,0,0)
        self.window = window
        self.windowsz = window.get_size()
        self.catframes = []
        self.windowframes = []
        for i in range(5):
            self.catframes.append(pygame.image.load('nyas/cat'+str(i+1)+'.png'))
        for j in range(6):
            self.windowframes.append(pygame.image.load('nyas/window'+str(j+1)+'.png'))
        self.i = 0  # for cat frames
        self.j = 0  # for window frames
        if date < 2:
            self.puzzleicon = pygame.image.load('nyas/assignment.png')   # load assignment icon
        else:
            self.puzzleicon = pygame.image.load('nyas/exam.png')   # load exam icon
        self.syllabusicon = pygame.image.load('nyas/syllabus.png')
        self.calender = pygame.image.load('nyas/calender.png')
        self.flower = pygame.image.load('nyas/flower.png')
        self.icons = [pygame.Rect((50,250),(80,90)),pygame.Rect((50,350),(80,90)),pygame.Rect((200,30),(100,120))]   # list of buttons(Rects) that can be pressed

    def blit(self):
        # blits frames to make it into an animation
        i = self.i % 5  # switch image every update
        j = self.j % 6
        self.window.blit(self.catframes[i], (self.windowsz[0]/3,self.windowsz[1]/5))
        self.window.blit(self.windowframes[j],(30,30))
        self.i = i + 1
        self.j = j + 1
        self.window.blit(self.puzzleicon,self.icons[1])
        self.window.blit(self.syllabusicon,self.icons[0])
        self.window.blit(self.calender,self.icons[2])
        self.window.blit(self.flower,pygame.Rect((600,325),(100,140)))

    def draw(self):
        self.walllines()

    def walllines(self):
        # next 3 lines are to draw room lining
        pygame.draw.aaline(self.window,self.black,(0,3*self.windowsz[1]/4),(500,200))
        pygame.draw.aaline(self.window,self.black,(500,200),(self.windowsz[0],3*self.windowsz[1]/5))
        pygame.draw.aaline(self.window,self.black,(500,200),(500,0))

    def showtext(self,date):
        font = pygame.font.SysFont('Comic Sans MS', 32)
        ddate = font.render(str(date), True, self.black)
        dateRect = ddate.get_rect()
        dateRect.center = (255,100)

        font = pygame.font.SysFont('Comic Sans MS', 20, True,True)
        exam = font.render(("Exam in "+str(10-date)+" Days"), True, self.black)
        examRect = exam.get_rect()
        examRect.center = (600,30)

        self.window.blit(exam,examRect)
        self.window.blit(ddate,dateRect)

    def clicked(self):
        # 0 is syllabus, 1 is puzzle(assignment or exam)
        if pygame.mouse.get_pressed()[0]:
            a,b = pygame.mouse.get_pos()
            for i in range(2):  # only 0 and 1 are buttons
                if self.icons[i].collidepoint(a,b):
                    return i

main()