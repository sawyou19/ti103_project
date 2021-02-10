import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Echecs")

board = pygame.Surface((480, 480))
board.fill((175, 141, 120))

for x in range(0, 8, 2):
    for y in range(0, 8, 2):
        pygame.draw.rect(board, (250, 240, 230), (x * 60, y * 60, 60, 60))
for x in range(1, 9, 2):
    for y in range(1, 9, 2):
        pygame.draw.rect(board, (250, 240, 230), (x * 60, y * 60, 60, 60))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                print(x, y)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                x, y = event.pos
                print(x, y)
    screen.fill((200, 200, 200))
    screen.blit(board, board.get_rect())
    pygame.display.update()
