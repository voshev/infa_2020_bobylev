import pygame
from pygame.draw import *

pygame.init()

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
FPS = 30

screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
"face"
circle(screen, YELLOW, (250, 250), 200)
circle(screen, BLACK, (250, 250), 200, 1)
"eyes"
circle(screen, RED, (150, 200), 40)
circle(screen, BLACK, (150, 200), 40, 1)
circle(screen, BLACK, (150, 200), 15)

circle(screen, RED, (350, 200), 30)
circle(screen, BLACK, (350, 200), 30, 1)
circle(screen, BLACK, (350, 200), 15)
"mouth"
rect(screen, BLACK, (150, 340, 200, 30))
"eyelashes"
polygon(screen, BLACK, [(220, 202.5), (50, 75), (57.5, 65), (227.5, 192.5)])
polygon(screen, BLACK, [(300, 210.9), (430, 65.3), (410, 47.4), (280, 193)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
