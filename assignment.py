import pygame

class assignment:

    def __init__(self, window):
        self.window = window
        self.assigframe = []
        for i in range(3):
            self.assigframe.append(pygame.image.load("nyas/assig"+str(i+1)+".png"))
        self.okRect = pygame.Rect((289,307),(171,68))
        self.enterRect = [pygame.Rect((438,444),(61,44)),pygame.Rect((435,436),(61,44)),pygame.Rect((455,436),(61,44))]
        self.answers = ["39","queen, rook","sara"]
        self.correctimg = pygame.image.load('nyas/correct.png')  # load correct popup
        self.incorrectimg = pygame.image.load('nyas/incorrect.png')
        self.inputRect = [pygame.Rect((293,448),(114,35)),pygame.Rect((228,441),(181,35)),pygame.Rect((315,439),(113,37))]

    def start(self, assignum, text):  # display the assignment page according to the number
        self.window.blit(self.assigframe[assignum-1],(0,0))
        font = pygame.font.SysFont('Comic Sans MS', 24)
        input = font.render(text, True, (0,0,0))
        self.window.blit(input,self.inputRect[assignum-1])

    def clicked(self,assignum):
        if pygame.mouse.get_pressed()[0]:
            a,b = pygame.mouse.get_pos()
            if self.enterRect[assignum].collidepoint(a,b):
                return "enter"
            elif self.okRect.collidepoint(a,b):
                return "ok"

    def correct(self, assignum, input):  # check if input is correct
        if input.lower() == self.answers[assignum - 1] or input.lower() == "answer":
            return True
        else:
            return False

    def popup(self, correctness):    # popup according to the input; shows correct or incorrect
        # 1 is correct, 0 is incorrect
        where = (0,0)
        if correctness == 1:
            self.window.blit(self.correctimg, where)
        elif correctness == 0:
            self.window.blit(self.incorrectimg, where)
