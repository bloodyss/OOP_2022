import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

balls = []
ball_lifetime = 5 * FPS
max_balls = 5


def new_ball():
    if len(balls) < max_balls:
        x = randint(100, 1100)
        y = randint(100, 800)
        r = randint(30, 50)
        color = COLORS[randint(0, 5)]
        dx = randint(-5, 5)
        dy = randint(-5, 5)
        balls.append({'x': x, 'y': y, 'r': r, 'color': color, 'dx': dx, 'dy': dy, 'lifetime': ball_lifetime})


def click(event):
    for ball in balls:
        if (ball['x'] - event.pos[0]) ** 2 + (ball['y'] - event.pos[1]) ** 2 < ball['r'] ** 2:
            balls.remove(ball)


def draw_ball(ball):
    circle(screen, ball['color'], (ball['x'], ball['y']), ball['r'])
def count_hits(balls):
    """Подсчитывает количество попаданий по мячикам."""
    hits = 0
    for ball in balls:
        if ball['lifetime'] < ball_lifetime:  # Если время жизни уменьшилось, значит, было попадание
            hits += 1
    return hits

def move_ball(ball):
    ball['x'] += ball['dx']
    ball['y'] += ball['dy']
    if ball['x'] - ball['r'] < 0 or ball['x'] + ball['r'] > 1200:
        ball['dx'] = -ball['dx']
    if ball['y'] - ball['r'] < 0 or ball['y'] + ball['r'] > 900:
        ball['dy'] = -ball['dy']

    ball['lifetime'] -= 1
    if ball['lifetime'] <= 0:
        balls.remove(ball)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    new_ball()
    screen.fill(BLACK)

    for ball in balls.copy():
        draw_ball(ball)
        move_ball(ball)

    total_hits = count_hits(balls)

    

    pygame.display.update()

    for ball in balls.copy():
        draw_ball(ball)
        move_ball(ball)

    pygame.display.update()

pygame.quit()
print("Кол. попаданий:", total_hits)