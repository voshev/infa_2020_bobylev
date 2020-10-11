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


def car(x=350, y=800, stretch_factor=1):
    width = 50
    height = 10
    """It's drawing exhaust"""
    new_ellipse(x - 35 * stretch_factor, y + 2 * stretch_factor, 30 * stretch_factor, 3 * stretch_factor, black)
    """It's drawing the base of car"""
    rect(screen, blue, (x, y, width * stretch_factor, height * stretch_factor))
    rect(screen, blue, (x + 6 * stretch_factor, y - 7 * stretch_factor,
                        width * 0.6 * stretch_factor, height * 0.7 * stretch_factor))
    """Its drawing windows of car"""
    rect(screen, white, (x + 10 * stretch_factor, y - 5 * stretch_factor,
                         width * 0.2 * stretch_factor, height * 0.4 * stretch_factor))
    rect(screen, white, (x + 22 * stretch_factor, y - 5 * stretch_factor,
                         width * 0.2 * stretch_factor, height * 0.4 * stretch_factor))
    """It's drawing wheels"""
    circle(screen, black, (x + 10 * stretch_factor, y + 10 * stretch_factor),
           5 * stretch_factor, 5 * stretch_factor)
    circle(screen, black, (x + 40 * stretch_factor, y + 10 * stretch_factor),
           5 * stretch_factor, 5 * stretch_factor)


def new_ellipse(x, y, width, height, color):
    surface = pygame.Surface((width * 2, height * 2), pygame.SRCALPHA)
    size_of_ellipse = (width, height, width, height)
    ellipse(surface, color, size_of_ellipse)
    screen.blit(surface, (x, y))


def street(x, y, stretch_factor):
    rect(screen, (255, 255, 255), (x-50, y-90, 704 * stretch_factor, 504 * stretch_factor))
    rect(screen, (183, 196, 200, 255), (x-50, y-90, 700 * stretch_factor, 500 * stretch_factor))

    rect(screen, (147, 167, 172), (x, y, 115 * stretch_factor, 460 * stretch_factor))
    rect(screen, (147, 172, 167), (x + 140 * stretch_factor, y + 30 * stretch_factor,
                                   110 * stretch_factor, 450 * stretch_factor))
    rect(screen, (183, 200, 196), (x + 60 * stretch_factor, y + 75 * stretch_factor,
                                   125 * stretch_factor, 440 * stretch_factor))
    rect(screen, (219, 227, 226), (x + 380 * stretch_factor, y - 10 * stretch_factor,
                                   120 * stretch_factor, 480 * stretch_factor))
    rect(screen, (111, 145, 138), (x + 320 * stretch_factor, y + 100 * stretch_factor,
                                   110 * stretch_factor, 420 * stretch_factor))


"""It's drawing bottom background"""
rect(screen, (91, 111, 108, 255), (0, 600, 700, 333))
ellipse(screen, (221, 227, 221, 255), (-50, 780, 900, 300))
""""""
street(50, 80, 1.2)
"""It's drawing clouds"""
new_ellipse(-100, 670, 200, 50, (191, 201, 195, 100))
new_ellipse(-100, 730, 200, 50, (191, 201, 195, 100))
new_ellipse(-300, 630, 200, 50, (191, 201, 195, 100))
new_ellipse(-600, -200, 800, 200, (83, 108, 103, 30))
new_ellipse(-650, 100, 800, 150, (83, 108, 103, 30))
new_ellipse(-600, -50, 500, 150, (83, 108, 103, 30))
new_ellipse(-800, 300, 600, 150, (83, 108, 103, 30))

car(stretch_factor=4)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
