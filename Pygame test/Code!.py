import pygame
import random
from sys import exit

play = True
while play == True:
    ##pygame code##
    pygame.init()
    screen = pygame.display.set_mode((1920,1020))
    pygame.display.set_caption("Gambling")
    clock = pygame.time.Clock()
    
    test_font = pygame.font.Font("Font/Planet-Joy.ttf",60)
    text = test_font.render("Nothing",True,"Yellow")
    baltext = test_font.render("200",True,"Yellow")

    background = pygame.image.load("Graphics/Casino.jpg").convert_alpha()
    background_2 = pygame.image.load("Graphics/Black.png").convert_alpha()
    blank = pygame.image.load("Graphics/blank.jpg").convert_alpha()
    s1 = blank.get_rect(midbottom = (800,700))
    s2 = blank.get_rect(midbottom = (1000,700))
    s3 = blank.get_rect(midbottom = (1200,700))
    
    s1_s = blank
    s2_s = blank
    s3_s = blank
    
    button_s = pygame.image.load("Graphics/Button.png").convert_alpha()
    button_r = button_s.get_rect(midbottom = (950,400))
    pressonce = 0
    balance = 200
    change = ""
    
    seven = pygame.image.load("Graphics/Seven.png").convert_alpha()
    cherry = pygame.image.load("Graphics/Cherry.png").convert_alpha()
    bell = pygame.image.load("Graphics/Bell.png").convert_alpha()
    grape = pygame.image.load("Graphics/Grape.png").convert_alpha()
    orange = pygame.image.load("Graphics/Orange.png").convert_alpha()
    lemon = pygame.image.load("Graphics/Lemon.png").convert_alpha()
    bar = pygame.image.load("Graphics/Bar.png").convert_alpha()
    banana = pygame.image.load("Graphics/Banana.png").convert_alpha()
    watermelon = pygame.image.load("Graphics/Watermelon.png").convert_alpha()
    
    bank_s = pygame.image.load("Graphics/Bank.jpg").convert_alpha()
    bank_r = bank_s.get_rect(midbottom = (300,500))
    
    loanS_s = pygame.image.load("Graphics/LoanShark.jpg").convert_alpha()
    loanS_r = loanS_s.get_rect(midbottom = (1300,1000))
    
    icon = [seven,cherry,bell,grape,orange,lemon,bar,banana,watermelon]
    ##variables##
    pycoderun = True
    pressed = 0
    stage = 0
    while pycoderun == True:
        while stage == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button_r.collidepoint(event.pos):
                          pressed = 1
                          pressonce = 2
                        else:
                            pressed = 0
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        pressed = 0
            if pressed == 1:
                for x in range(random.randint(0,9)):
                    s1_s = icon[x]
                for x in range(random.randint(0,9)):
                    s2_s = icon[x]
                for x in range(random.randint(0,9)):
                    s3_s = icon[x]
            if pressonce == 2:
                balance -= 5
                pressonce = 1
                change = " - 5"
                text = test_font.render("Nothing",True,"White")
            if s1_s == s2_s == s3_s and pressed == 0 and pressonce == 1:
                print("Jackpot")
                text = test_font.render("Jackpot",True,"White")
                pressonce = 0
                balance += 105
                change = " + 100"
            elif s1_s == s2_s and pressed == 0 and pressonce == 1:
                print("Mini")
                text = test_font.render("Mini Jackpot",True,"White")
                pressonce = 0
                balance += 10
                change = " + 5"
            elif s2_s == s3_s and pressed == 0 and pressonce == 1:
                print("Mini")
                text = test_font.render("Mini Jackpot",True,"White")
                pressonce = 0
                balance += 10
                change = " + 5"
            screen.blit(background,(0,0))
            screen.blit(text,(1000,800))
            balchan = str(balance) + change
            baltext = test_font.render(str(balchan),True,"White")
            screen.blit(baltext,(1400,800))
            screen.blit(s1_s,s1)
            screen.blit(s2_s,s2)
            screen.blit(s3_s,s3)
            screen.blit(button_s,button_r)
            if balance <= 0:
                stage += 1
            pygame.display.update()
            clock.tick(60)
        while stage == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if loanS_r.collidepoint(event.pos):
                          stage = 0
                          balance = 500
                        elif bank_r.collidepoint(event.pos):
                          stage = 0
                          balance = 200
            screen.blit(background_2,(0,0))
            screen.blit(text,(1000,800))
            baltext = test_font.render("Backrupt",True,"White")
            screen.blit(baltext,(200,700))
            screen.blit(bank_s,bank_r)
            screen.blit(loanS_s,loanS_r)
            baltext = test_font.render("Loan Shark (500)",True,"Red")
            baltext = test_font.render("Loan Shark (500)",True,"Red")
            screen.blit(baltext,(800,50))
            baltext = test_font.render("Bank (200)",True,"Red")
            screen.blit(baltext,(70,50))
            pygame.display.update()
            clock.tick(60)