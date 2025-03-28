import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Circle")

size = 25
speed = 20
x, y = width // 2, height // 2

while True:
    screen.fill((0, 0, 0))  
    pygame.draw.circle(screen, (255, 0, 0), (x, y), size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - size - speed >= 0:
                y -= speed
            if event.key == pygame.K_DOWN and y + size + speed <= height:
                y += speed
            if event.key == pygame.K_LEFT and x - size - speed >= 0:
                x -= speed
            if event.key == pygame.K_RIGHT and x + size + speed <= width:
                x += speed
    pygame.display.flip()

    