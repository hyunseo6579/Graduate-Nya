# for testing basic functions I need in this game
# maybe for cleaner code, I can separate file by each frame

import pygame

cat = [pygame.image.load('nyas/cat1.png'),pygame.image.load('nyas/cat2.png'),pygame.image.load('nyas/cat3.png')]
pygame.init()
scrnx = 750
scrny = 500
screen = pygame.display.set_mode((scrnx,scrny))

run = True
frame = 0
i = 0

btnx = (scrnx - 200) / 2
btny = 400
button_rect = pygame.Rect(btnx, btny, 200, 70)

def mainscreen():
        global i
        i = i%3 # switch image every update
        screen.blit(cat[i], (scrnx/3,scrny/5))
        i += 1

def titlescreen():
        x = (scrnx - 541)/2  # 541 is width of image
        screen.blit(pygame.image.load("nyas/cat_title.png"),(x,0))
        screen.blit(pygame.image.load('nyas/start.png'),(btnx,btny))


while run:
        pygame.time.delay(50)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        if frame == 0 and pygame.mouse.get_pressed()[0]:
                a,b = pygame.mouse.get_pos()  # use this to check if start button is clicked
                if button_rect.collidepoint(a,b):
                        frame += 1


        screen.fill((255, 255, 255))
        if frame == 0:
                titlescreen()
        elif frame == 1:
                mainscreen()

        pygame.display.update()

