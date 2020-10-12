import pygame
from pygame.draw import *
from random import randint
import os

pygame.init()

FPS = 8
size = screen_width, screen_height = 1200, 900
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:
    def __init__(self):
        self.x = randint(100, 700)
        self.y = randint(100, 500)
        self.r = randint(30, 50)
        self.v_x = randint(50, 100)
        self.v_y = randint(50, 100)
        self.color = COLORS[randint(0, 5)]

    def initialization(self):
        circle(screen, self.color, (self.x, self.y), self.r)

    def smash_x(self):
        """what happens if ball smashes on the x-axe"""
        self.v_x = - self.v_x

    def smash_y(self):
        """what happens if ball smashes on the y-axe"""
        self.v_y = - self.v_y

    def balling(self):
        """function which moves ball"""
        self.x += self.v_x
        self.y += self.v_y
        self.initialization()
        if self.x < self.r or self.x > screen_width - self.r:
            self.smash_x()
        if self.y < self.r or self.y > screen_height - self.r:
            self.smash_y()

    def click(self):
        return self.x, self.y, self.r


class Rect:
    """
    this class is a X, which randomly moving
    """
    def __init__(self):
        self.x = randint(100, 700)
        self.y = randint(100, 500)
        self.r = randint(30, 50)
        self.v_x = randint(50, 100)
        self.v_y = randint(50, 100)
        self.color = COLORS[randint(0, 5)]

    def initialization(self):
        rect(screen, self.color, (self.x, self.y, self.r, self.r), self.r)

    def smash_x(self):
        self.v_x = - self.v_x

    def smash_y(self):
        self.v_y = - self.v_y

    def balling(self):
        """function which moves rect"""
        a = 100
        self.x = randint(self.x - a, self.x + a)
        self.y = randint(self.y - a, self.y + a)
        self.initialization()

        if self.x >= screen_width - self.r:
            self.x = randint(self.x - a, self.x)
        if self.x <= self.r:
            self.x = randint(self.x, self.x + a)
        if self.y <= self.r:
            self.y = randint(self.y, self.y + 15)
        if self.y >= screen_height - self.r:
            self.y = randint(self.y - a, self.y)

    def click(self):
        return self.x, self.y, self.r


pygame.display.update()
clock = pygame.time.Clock()
finished = False

n_1 = 0  # the first score (catching balls)
n_2 = 0  # the second score (catching rect)

new_ball_1 = Ball()
new_ball_2 = Ball()

new_rect_1 = Rect()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cords_1 = new_ball_1.click()
            cords_1_1 = new_ball_2.click()
            cords_2 = new_rect_1.click()
            if ((event.pos[0] - cords_1[0]) ** 2 + (event.pos[1] - cords_1[1]) ** 2) < cords_1[2] ** 2:
                n_1 += 1
            if ((event.pos[0] - cords_1_1[0]) ** 2 + (event.pos[1] - cords_1_1[1]) ** 2) < cords_1_1[2] ** 2:
                n_1 += 1
            if ((event.pos[0] - cords_2[0]) ** 2 + (event.pos[1] - cords_2[1]) ** 2) < cords_2[2] ** 2:
                n_2 += 1
            print(n_1, n_2)
    new_ball_2.balling()
    new_ball_1.balling()
    new_rect_1.balling()
    pygame.display.update()
    screen.fill(BLACK)

results = []


def load():
    global results
    """this function allows us to bring the previous results"""
    with open('results.txt', 'r') as file:
        for i in file.read():
            results.append(i)


def text():
    global n_1, n_2, results
    """this function adds the scores to the file"""
    load()
    with open('results.txt', 'w') as file:
        for i in results:
            file.write(i)
        file.write(str(n_1)+','+str(n_2)+'\n')


text()

pygame.quit()
