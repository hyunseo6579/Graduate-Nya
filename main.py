import pygame
from assignment import assignment
from syllabus import syllabus
from exam import exam


def main():

    pygame.init()
    pygame.display.set_caption("Graduate Nya")
    window = pygame.display.set_mode((750,500))
    run = True
    frame = 0
    assignum = 1
    duedate = [3,6,9]
    progress = [0,0,0]  # how many asisgnments completed; 0 means in progress aka dot
    date = 1  # d-1. puzzle changes from assignment to exam depending on the date

    title = titlepage(window)
    mainpg = mainpage(window)
    assig = assignment(window)
    sylb = syllabus(window)
    exm = exam(window)

    arrow = pygame.image.load('nyas/arrow.png')  # points to syllabus
    flower = [pygame.image.load('nyas/flower.png'),pygame.image.load_extended('nyas/flower2.png')]
    note = pygame.image.load('nyas/note.png')
    notex = pygame.Rect((517,116),(20,17))

    showsylb = False
    showarrow = True
    enter = False # true when enter is clicked
    exampass = None # boolean
    shownote = False

    text = ''
    while run:
        pygame.time.delay(50)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        window.fill((255, 255, 255))

        if frame == 0:
            title.blit()
            if title.clicked():
                frame += 1

        elif frame == 1:
            # check date matching with assignment due date
            for i in range(3):
                if date > duedate[i] and progress[i] == 0:  #over due
                    progress[i] = 2 # assignment fail
                    assignum += 1
                #elif date == duedate[i]+1 and progress[i] == 1:  #if finished on date
                #    assignum += 1
                elif date <= duedate[i] and progress[i] == 1:  #finished before due
                    date = duedate[i] + 1 # jumps to day after due date
                    assignum += 1

            mainpg.draw()
            mainpg.blit(date)
            mainpg.progressblit(progress)
            mainpg.showtext(date)

            a,b = pygame.mouse.get_pos()
            if pygame.Rect((630,355),(60,100)).collidepoint(a,b):
                window.blit(flower[1],pygame.Rect((600, 325), (100, 140)))
                if pygame.mouse.get_pressed()[0]:
                    shownote = True
            else:
                window.blit(flower[0],pygame.Rect((600, 325), (100, 140)))

            if showarrow:
                window.blit(arrow,(135,280))

            if mainpg.clicked(date) == "assignment":
                frame += assignum

            elif mainpg.clicked(date) == "syllabus":
                showsylb = True

            elif mainpg.clicked(date) == "exam":
                frame = 5

            if showsylb == True:
                sylb.blit()
                if sylb.exclicked() == True:
                    showsylb = False
                    showarrow = False

            if shownote == True:
                window.blit(note, (0, 0))
                if pygame.mouse.get_pressed()[0]:
                    if notex.collidepoint(a, b):
                        shownote = False

        elif frame == 2 or frame == 3 or frame == 4:  # frame for assignments
            len = [6,12,6]  #max length of text per assignment
            input = text[:len[assignum-1]]  # only up to 10 char
            assig.start(assignum, input)  # pulls the assignment 1 screen
            if assig.clicked(assignum-1) == "enter":
                enter = True
            if enter == True:
                if assig.correct(assignum, input) == True:
                    progress[assignum - 1] = 1  # (if not, player can try again until it's due date)
                    assig.popup(1)
                else:
                    assig.popup(0)
                if assig.clicked(assignum-1) == "ok":  # ok button should only work after enter button has been pressed
                    frame = 1  # go back to mainpg
                    date += 1
                    enter = False
                    text = ''

        elif frame == 5:
            exm.blit(text[:10])  # take up to 10 char
            if exm.clicked() == "enter":
                enter = True
            if enter == True:
                if exm.correct(text[:10]) == True:
                    exm.popup(1)
                    exampass = True
                else:
                    exm.popup(0)
                    exampass = False
                if exm.clicked() == "ok":
                    enter = False
                    frame += 1

        elif frame == 6:
            if exm.passed(progress, exampass) == True: # if user has passing mark
                exm.blitresult(1)
            else:
                exm.blitresult(0)

        pygame.display.update()


class titlepage:

    def __init__(self,window):
        self.titlecat = pygame.image.load('nyas/cat_title.png')
        self.startbutton = pygame.image.load('nyas/start.png')
        self.window = window
        self.windowsz = window.get_size()
        self.catcoord = (int((self.windowsz[0]-541)/2),0)
        self.strtcoord = (int((self.windowsz[0]-200)/2),int(self.windowsz[1]/5)*4)
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

    def __init__(self,window):
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

        self.puzzleicon = pygame.image.load('nyas/assignment.png')   # load assignment icon
        self.puzzleicon2 = pygame.image.load('nyas/examicon.png')   # load exam icon
        self.syllabusicon = pygame.image.load('nyas/syllabusicon.png')
        self.calender = pygame.image.load('nyas/calender.png')
        self.clipboard = pygame.image.load('nyas/clipboard.png')
        self.dot = pygame.image.load('nyas/dot.png')
        self.check = pygame.image.load('nyas/check.png')
        self.ex = pygame.image.load('nyas/ex.png')

        self.icons = [pygame.Rect((50,250),(80,90)),pygame.Rect((50,350),(80,90)),pygame.Rect((200,30),(100,120))]   # list of buttons(Rects) that can be pressed

    def blit(self,date):
        # blits frames to make it into an animation
        i = self.i % 5  # switch image every update
        j = self.j % 6
        self.window.blit(self.catframes[i], (int(self.windowsz[0]/3),int(self.windowsz[1]/5)))
        self.window.blit(self.windowframes[j],(30,30))
        self.i = i + 1
        self.j = j + 1
        if date <= 9:
            self.window.blit(self.puzzleicon,self.icons[1])
        elif date == 10:
            self.window.blit(self.puzzleicon2,self.icons[1])
        self.window.blit(self.syllabusicon,self.icons[0])
        self.window.blit(self.calender,self.icons[2])
        self.window.blit(self.clipboard, pygame.Rect((525,50),(45,55)))


    def progressblit(self,progress):
        x = 580
        between = 40 # space between the x coords
        y = 65
        rect = (30,30)

        # self note: progress 0 = dot, 1 = check, 2 = ex

        for i in range(3): # total of 3 assignments
            if progress[i] == 0:
                self.window.blit(self.dot, pygame.Rect((x+between*i, y), rect))
            elif progress[i] == 1:
                self.window.blit(self.check, pygame.Rect((x + between * i, y), rect))
            elif progress[i] == 2:
                self.window.blit(self.ex, pygame.Rect((x + between * i, y), rect))


    def draw(self):
        self.walllines()

    def walllines(self):
        # next 3 lines are to draw room lining
        pygame.draw.aaline(self.window,self.black,(0,3*int(self.windowsz[1]/4)),(500,200))
        pygame.draw.aaline(self.window,self.black,(500,200),(self.windowsz[0],3*int(self.windowsz[1]/5)))
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

    def clicked(self,date):
        # 0 is syllabus, 1 is puzzle(assignment or exam)
        if pygame.mouse.get_pressed()[0]:
            a,b = pygame.mouse.get_pos()
            if self.icons[0].collidepoint(a,b):
                return "syllabus"
            elif self.icons[1].collidepoint(a,b) and date < 10:  #before exam date
                return "assignment"
            elif self.icons[1].collidepoint(a,b) and date == 10:  #exam date
                return "exam"


main()
