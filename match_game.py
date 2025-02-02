import pygame
import pgzero

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill('black')

pygame.display.update()
ludo = pygame.image.load('match/ludo.png')
candy = pygame.image.load('match/candy_crush.jpg')
surfers = pygame.image.load('match/subway_surfers.png')
temple = pygame.image.load('match/temple_run.png')

screen.blit(ludo, (50,50))
screen.blit(candy, (50, 170))
screen.blit(surfers, (50, 290))
screen.blit(temple, (50, 410))

font = pygame.font.SysFont('Times New Roman', 40)
text1 = font.render('Subway Surfers', True, 'white')
screen.blit(text1, (300, 70))
text2 = font.render('Temple Run', True, 'white')
screen.blit(text2, (300,190))
text3 = font.render('Candy Crush', True, 'white')
screen.blit(text3, (300, 315))
text4 = font.render('Ludo', True, 'white')
screen.blit(text4, (300, 420))

run = True 
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    pygame.display.update()

    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, 'light pink', pos, 10, 0)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen, 'light blue', pos, pos2, 5)
        pygame.draw.circle(screen, ' purple', pos2, 10,0)
        pygame.display.update()



