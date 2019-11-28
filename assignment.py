import pygame

class assignment:

    def __init__(self, window):
        self.window = window
        self.assigframe = []
        for i in range(3):
            self.assigframe.append(pygame.image.load("nyas/assig"+str(i+1)+".png"))
        self.enterRect = None #pygame rect for enter button
        self.okRect = None #pygame rect for ok button
        self.answers = ["these","are","answers"]
        self.correct = pygame.image.load()  # load correct popup
        self.inocrrect = pygame.image.load()

    def start(self, assignum,text):  # display the assignment page according to the number
        pass
        #self.window.blit(self.assigframe[assignum-1],(0,0))
        #font = pygame.font.SysFont('Comic Sans MS', 24)
        #input = font.render(text), True, self.black)
        #inputRect = pygame.Rect((coords),(size))
        #self.window.blit(input,inputRect)

    def clicked(self):
        if pygame.mouse.get_pressed()[0]:
            a,b = pygame.mouse.get_pos()
            if self.enterRect.collidepoint(a,b):
                return "enter"
            elif self.okRect.collidepoint(a,b):
                return "ok"

    def correct(self, assignum, input):  # check if input is correct
        if input == self.answers[assignum - 1]:
            return True
        else:
            return False

    def popup(self, correctness):    # popup according to the input; shows correct or incorrect
        # 1 is correct, 0 is incorrect
        pass
        #where = pygame.Rect((coords),(size))
        #if correctness == 1:
            #self.window.blit(self.correct, where)
        #elif correctness == 0:
            #self.window.blit(self.incorrect, where)
