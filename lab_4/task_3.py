import pygame
from pygame.draw import *

pygame.init()

FPS = 30
size = display_width, display_height = 700, 900
screen = pygame.display.set_mode(size)

screen.fill((255, 255, 255))

blue = (0, 204, 255)
white = (213, 246, 255)
black = (0, 34, 43)
green = (111, 145, 138)


def car(x=350, y=800, stretch_factor=1, i=1):
    width = 50
    height = 10
    if i == 1:
        """It's drawing exhaust"""
        new_ellipse(x - 35 * stretch_factor * i, y + 2 * stretch_factor,
                    30 * stretch_factor, 3 * stretch_factor, black)
        """It's drawing the base of car"""
        rect(screen, blue, (x, y, width * stretch_factor, height * stretch_factor))
        rect(screen, blue, (x + 6 * stretch_factor * i, y - 7 * stretch_factor,
                            width * 0.6 * stretch_factor, height * 0.7 * stretch_factor))
        """Its drawing windows of car"""
        rect(screen, white, (x + 10 * stretch_factor * i, y - 5 * stretch_factor,
                             width * 0.2 * stretch_factor, height * 0.4 * stretch_factor))
        rect(screen, white, (x + 22 * stretch_factor * i, y - 5 * stretch_factor,
                             width * 0.2 * stretch_factor, height * 0.4 * stretch_factor))
        """It's drawing wheels"""
        circle(screen, black, (x + 10 * stretch_factor * i, y + 10 * stretch_factor),
               5 * stretch_factor, 5 * stretch_factor)
        circle(screen, black, (x + 40 * stretch_factor * i, y + 10 * stretch_factor),
               5 * stretch_factor, 5 * stretch_factor)
    if i == -1:
        """It's drawing exhaust"""
        new_ellipse(x + 5 * stretch_factor * i, y + 2 * stretch_factor,
                    30 * stretch_factor, 3 * stretch_factor, black)
        """It's drawing the base of car"""
        rect(screen, blue, (x, y, width * stretch_factor, height * stretch_factor))
        rect(screen, blue, (x - 11 * stretch_factor * i, y - 7 * stretch_factor,
                            width * 0.6 * stretch_factor, height * 0.7 * stretch_factor))
        """Its drawing windows of car"""
        rect(screen, white, (x - 27 * stretch_factor * i, y - 5 * stretch_factor,
                             width * 0.2 * stretch_factor, height * 0.4 * stretch_factor))
        rect(screen, white, (x - 15 * stretch_factor * i, y - 5 * stretch_factor,
                             width * 0.2 * stretch_factor, height * 0.4 * stretch_factor))
        """It's drawing wheels"""
        circle(screen, black, (x - 10 * stretch_factor * i, y + 10 * stretch_factor),
               5 * stretch_factor, 5 * stretch_factor)
        circle(screen, black, (x - 40 * stretch_factor * i, y + 10 * stretch_factor),
               5 * stretch_factor, 5 * stretch_factor)


def new_ellipse(x, y, width, height, color):
    surface = pygame.Surface((width * 2, height * 2), pygame.SRCALPHA)
    size_of_ellipse = (width, height, width, height)
    ellipse(surface, color, size_of_ellipse)
    screen.blit(surface, (x, y))


def new_rect(x, y, width, height, color):
    surface = pygame.Surface((width * 2, height * 2), pygame.SRCALPHA)
    size_of_rect = (x, y, width, height)
    rect(surface, color, size_of_rect)
    screen.blit(surface, (x, y))


def street(x, y, stretch_factor, i=1):
    if i == 1:
        rect(screen, (255, 255, 255),
             (x - 70 * stretch_factor * i, y - 76 * stretch_factor, 710 * stretch_factor, 610 * stretch_factor))
        rect(screen, (183, 196, 200, 255),
             (x - 70 * stretch_factor * i, y - 72 * stretch_factor, 700 * stretch_factor, 600 * stretch_factor))

        rect(screen, (147, 167, 172), (x, y, 115 * stretch_factor, 460 * stretch_factor))
        rect(screen, (147, 172, 167),
             (x + 140 * stretch_factor * i, y + 30 * stretch_factor, 110 * stretch_factor, 550 * stretch_factor))
        rect(screen, (183, 200, 196),
             (x + 60 * stretch_factor * i, y + 75 * stretch_factor, 125 * stretch_factor, 540 * stretch_factor))
        rect(screen, (219, 227, 226),
             (x + 380 * stretch_factor * i, y - 10 * stretch_factor, 120 * stretch_factor, 580 * stretch_factor))
        rect(screen, (111, 145, 138),
             (x + 320 * stretch_factor * i, y + 100 * stretch_factor, 110 * stretch_factor, 520 * stretch_factor))
    if i == -1:
        rect(screen, (255, 255, 255),
             (x + 52 * stretch_factor * i, y - 76 * stretch_factor, 710 * stretch_factor, 610 * stretch_factor))
        rect(screen, (183, 196, 200, 255),
             (x + 50 * stretch_factor * i, y - 72 * stretch_factor, 700 * stretch_factor, 600 * stretch_factor))

        rect(screen, (147, 167, 172), (x + 420 * stretch_factor, y, 115 * stretch_factor, 560 * stretch_factor))
        rect(screen, (147, 172, 167),
             (x - 280 * stretch_factor * i, y + 30 * stretch_factor, 110 * stretch_factor, 550 * stretch_factor))
        rect(screen, (183, 200, 196),
             (x - 350 * stretch_factor * i, y + 75 * stretch_factor, 125 * stretch_factor, 540 * stretch_factor))
        rect(screen, (219, 227, 226),
             (x - 10 * stretch_factor * i, y - 10 * stretch_factor, 120 * stretch_factor, 580 * stretch_factor))
        rect(screen, (111, 145, 138),
             (x - 150 * stretch_factor * i, y + 100 * stretch_factor, 110 * stretch_factor, 520 * stretch_factor))


for i in range(1, 500, 5):
    ellipse_i = pygame.Surface((800, 800), pygame.SRCALPHA)
    ellipse(ellipse_i, (0, 0, 0, i / 100), (200 - (i - 1) / 2, 200 - (i - 1) / 2, 2 * i, i))
    screen.blit(ellipse_i, (-50, 0))

for i in range(1, 400, 5):
    ellipse_i = pygame.Surface((800, 800), pygame.SRCALPHA)
    ellipse(ellipse_i, (0, 0, 0, i / 100), (200 - (i - 1) / 2, 200 - (i - 1) / 2, 2 * i, i))
    screen.blit(ellipse_i, (500, -100))

new_rect(0, 70, 150, 500, (0, 0, 0, 100))
new_rect(0, 0, 100, 800, (0, 0, 0, 10))
new_rect(150, 70, 150, 500, (0, 0, 0, 100))
new_rect(130, 10, 150, 500, (0, 0, 0, 100))
new_rect(185, 0, 150, 500, (0, 0, 0, 100))
new_rect(205, 0, 150, 500, (0, 0, 0, 100))
new_rect(215, 0, 150, 500, (0, 0, 0, 100))
new_rect(225, 0, 150, 500, (0, 0, 0, 100))
new_rect(255, 0, 150, 500, (0, 0, 0, 100))


new_ellipse(120, 50, 500, 100, (0, 0, 0, 50))
new_ellipse(-600, 100, 500, 100, (0, 0, 0, 50))
new_ellipse(-600, -120, 500, 100, (0, 0, 0, 50))
new_ellipse(-390, -90, 500, 120, (0, 0, 0, 50))
new_ellipse(-310, -150, 600, 120, (0, 0, 0, 50))

rect(screen, (255, 255, 255), (500, 0, 1, 500), 5)

rect(screen, (91, 111, 108, 255), (0, 600, 700, 333))

street(300, 300, 0.7, -1)
street(0, 330, 0.7, 1)

new_ellipse(-250, 200, 700, 100, (83, 108, 103, 30))

car(400, 820, 4, -1)
car(100, 800, 4, 1)
car(580, 750, 2, -1)
car(400, 740, 2, -1)
car(220, 745, 2, -1)
car(20, 750, 2, -1)


for i in range(1, 400, 10):
    ellipse_i = pygame.Surface((800, 800), pygame.SRCALPHA)
    ellipse(ellipse_i, (250, 250, 250, 10 - i / 100), (200 - (i - 1) / 2, 200 - (i - 1) / 2, 2 * i, i))
    screen.blit(ellipse_i, (-50, 630))

new_ellipse(0, 0, 800, 100, (250, 250, 250, 100))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
