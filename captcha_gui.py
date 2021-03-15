import pygame
import random
import os

pygame.init()

#variables for the GUI Screen. Screen will be (640*550) and will appear at (50, 50)
WIDTH = 501
HEIGHT = 726
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('reCaptcha')

hydrantDir = os.listdir("database/hydrants/")  
otherDir = os.listdir("database/other/")    


restartButton = pygame.Rect(15, 670, 40, 40)
verifyButton = pygame.Rect(365, 660, 165, 55)
imgRects = []
hydrantRects = []


def setUp():
    screen.fill((255, 255, 255))

    imgRects.clear()
    hydrantRects.clear()

    captchaOutline = pygame.image.load('captcha_outline.png')
    screen.blit(captchaOutline, (0,0))

       
    hydrantImgs = [pygame.image.load("database/hydrants/" + hydrantDir[x]) for x in random.sample(range(0, len(hydrantDir)), 3)]
    otherImgs = [pygame.image.load("database/other/" + otherDir[y]) for y in random.sample(range(0, len(otherDir)), 6)]

    
    imgs = hydrantImgs + otherImgs
    random.shuffle(imgs)

    x_axis = [10, 173, 336]
    y_axis = [159, 321, 483]
    x = 0
    y = 0

    for img in imgs: 
        screen.blit(img, (x_axis[x], y_axis[y]))
        
        rect = pygame.Rect(x_axis[x], y_axis[y], img.get_height(), img.get_width())

        if img in hydrantImgs:
            hydrantRects.append(rect)

        if len(imgRects) < 9:
            imgRects.append(rect)

        x += 1
        if x == 3:
            x = 0
            y += 1


    pygame.display.flip()

def unlocked():
    screen.fill((0, 255, 0))
    pygame.display.flip()


setUp()

rectSelected = [False for i in range(9)]
finish = False

while finish != True:
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
            finish = True

        # Reset captcha when r is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                rectSelected = [False for i in range(9)]
                setUp()
                
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if restartButton.collidepoint(mousePos):
                rectSelected = [False for i in range(9)]
                setUp()
                 
            if verifyButton.collidepoint(mousePos):
                access = True
                for i in imgRects:
                    if i in hydrantRects:
                        if rectSelected[imgRects.index(i)] == False :
                            access = False
                    else:
                        if rectSelected[imgRects.index(i)] == True:
                            access = False

                if access:
                    print("You have unlocked the website!")
                    unlocked()
                else:
                    print("Please try again")


            for rect in imgRects:
                if rect.collidepoint(mousePos):
                    rectSelected[imgRects.index(rect)] = not rectSelected[imgRects.index(rect)]
                          