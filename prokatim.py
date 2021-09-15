import pygame
from math import *

EDRO = (185, 0, 0)
NAVAL = (0, 200, 0)

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Prokatim Edro!")
text = "Прокатим ЯдРо!"
text_surf = pygame.font.Font("freesansbold.ttf", 30).render(text, True, NAVAL)
text_rect = text_surf.get_rect()
text_rect.center = (320, 50)
clock = pygame.time.Clock()
x = 20
y = 75
angle = 0
while x < 640:
    clock.tick(50)
    x = x + 2
    y = y + 1
    angle -= 0.03
    screen.fill((10, 10, 10))
    screen.blit(text_surf, text_rect)
    pygame.draw.polygon(screen, NAVAL, [(0, 479), (0, 130), (639, 450), (639, 479)])
    pygame.draw.ellipse(screen, EDRO, [x+2, y+2, 80-4, 80-4])
    pygame.draw.arc(screen, (200, 200, 100), [x, y, 80, 80], angle, angle + 6.1, 3)
    pygame.display.update()
pygame.quit()
