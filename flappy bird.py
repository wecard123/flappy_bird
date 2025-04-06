import pygame
import random
from flappybirdhigh import *
pygame.init()
screen = pygame.display.set_mode((1300, 650))
player = pygame.image.load("bird.png")
pygame.display.set_icon(player)
pygame.display.set_caption("flappy bird")
player_surface = pygame.Surface((64, 64))
player_rect = player_surface.get_rect()
player_rect.x = 625
player_rect.y = 300
pipe_x = 1300
background = pygame.image.load("flappy bird background.jpg")
velocity = 0
pipeVEL = 0
font = pygame.font.SysFont("comsicans", 60)
font2 = pygame.font.SysFont("comsicans", 120)
text = font2.render("play", 1, "black")
text3 = font2.render("play again", 1, "black")
text4 = font2.render("level 1", 1, "red")
text5 = font2.render("level 2", 1, "red")
text6 = font2.render("level 3", 1, "red")
text7 = font2.render("level 4", 1, "red")
text8 = font2.render("level 5", 1, "red")
text10 = font2.render("flappy bird", 1, "yellow")
text11 = font2.render("level 6", 1, "red")
text12 = font2.render("level 7", 1, "red")
text13 = font2.render("level 8", 1, "red")
text14 = font2.render("level 9", 1, "red")
text15 = font2.render("level 10(max)", 1, "red")
button = pygame.Rect(518, 300, 270, 100)
button2 = pygame.Rect(428, 300, 470, 100)
gravity = False
score = 0
score_now = "0"
high_score2 = 0
start = True
restart = False
hi = True
run = True
while run:
    pygame.time.delay(50)
    f = open("flappybirdhigh.py", "w")
    f.write("high_score1 = " + str(high_score1))
    f.close()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(background, (0, 0))
    screen.blit(player, (player_rect.x, player_rect.y, player_rect.width, player_rect.height))
    if start:
        screen.blit(text10, (450, 10))
        pygame.draw.rect(screen, "green", button)
        screen.blit(text, (560, 300))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                velocity = 20
                pipeVEL = 6
                start = False
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and player_rect.y > velocity:
        player_rect.y -= velocity
        gravity = True
    else:
        gravity = False
    if gravity == False:
        player_rect.y += velocity
    if hi:
        pipe_y = random.randint(0, 650 - 300)
        hi = False
    if pipe_x + 100 < pipeVEL:
        pipe_y = random.randint(0, 650 - 300)
        score = score + 1
        score_now = str(score)
        pipe_x = 1300
    pipe = pygame.Rect(pipe_x, pipe_y, 100, 300)
    pygame.draw.rect(screen, "yellow", pipe)   
    if player_rect.y > 650:
        velocity = 0
        pipeVEL = 0
        restart = True
    if pipe.x >= player_rect.x and pipe.colliderect(player_rect):
        velocity = 0
        pipeVEL = 0
        restart = True
    if pipe.y >= player_rect.y and pipe.colliderect(player_rect):
        velocity = 0
        pipeVEL = 0
        restart = True
    if restart:
        pygame.draw.rect(screen, "green", button2)
        screen.blit(text3, (450, 300))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button2.collidepoint(event.pos):
                velocity = 20
                pipeVEL = 8
                pipe_x = 1300
                player_rect.y = 300
                score = 0
                score_now = str(score)
                restart = False
    high_score2 = score
    if high_score2 > high_score1:
        high_score1 = high_score2
        high_score_now = str(high_score1)
        high_score2 = 0
    else:
        high_score1 = high_score1
        high_score_now = str(high_score1)
        high_score2 = 0
    text9 = font.render("high score:" + high_score_now, 1, "black")
    screen.blit(text9, (10, 60))
    text2 = font.render("score:" + score_now, 1, "black")
    screen.blit(text2, (10, 10))
    if score == 0 and start == False and restart == False:
        screen.blit(text4, (450, 500))
    if score == 5 and restart == False:
        screen.blit(text5, (450, 500))
        pipeVEL = 13
    if score == 10 and restart == False:
        screen.blit(text6, (450, 500))
        pipeVEL = 18
    if score == 15 and restart == False:
        screen.blit(text7, (450, 500))
        pipeVEL = 23
    if score == 20 and restart == False:
        screen.blit(text8, (450, 500))
        pipeVEL = 28
    if score == 25 and restart == False:
        screen.blit(text11, (450, 500))
        pipeVEL = 30
    if score == 30 and restart == False:
        screen.blit(text12, (450, 500))
        pipeVEL = 32
    if score == 35 and restart == False:
        screen.blit(text13, (450, 500))
        pipeVEL = 34
    if score == 40 and restart == False:
        screen.blit(text14, (450, 500))
        pipeVEL = 36
    if score == 45 and restart == False:
        screen.blit(text15, (450, 500))
        pipeVEL = 38
    pipe_x -= pipeVEL
    pygame.display.update()
pygame.quit()