import pygame

class exam:

    def __init__(self,window):
        self.window = window
        self.examimg = pygame.image.load('nyas/exam.png')
        self.correctimg = pygame.image.load('nyas/correct2.png')
        self.incorrectimg = pygame.image.load('nyas/incorrect2.png')
        self.inputRect = pygame.Rect((249,441),(181,35))
        self.enterRect = pygame.Rect((454,436),(61,43))
        self.okRect = pygame.Rect((289,307),(171,68))
        self.passedimg = pygame.image.load('nyas/pass.png')
        self.failedimg = pygame.image.load('nyas/fail.png')

    def blit(self, text):
        self.window.blit(self.examimg,(0,0))
        font = pygame.font.SysFont('Comic Sans MS', 24)
        input = font.render(text, True, (0,0,0))
        self.window.blit(input,self.inputRect)

    def clicked(self):
        if pygame.mouse.get_pressed()[0]:
            a,b = pygame.mouse.get_pos()
            if self.enterRect.collidepoint(a,b):
                return "enter"
            elif self.okRect.collidepoint(a,b):
                return "ok"

    def correct(self, input):
        if input != '':  # if there is anything written
            return True
        else:
            return False

    def popup(self, correctness):
        # 1 is correct, 0 is wrong
        if correctness == 1:
            self.window.blit(self.correctimg,(0,0))
        elif correctness == 0:
            self.window.blit(self.incorrectimg,(0,0))

    def passed(self, progress, exampass):
        score = 0
        for i in range(3):
            if progress[i] == 1:  # assignment completed
                score += 20
        if exampass == True:
            score += 40

        if score >= 50:
            return True
        else:
            return False

    def blitresult(self, result):
        # 1 is pass, 0 is fail
        if result == 1:
            self.window.blit(self.passedimg, (0,0))
        elif result == 0:
            self.window.blit(self.failedimg,(0,0))