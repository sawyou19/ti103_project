import pygame
import sys

class Piece:
    def __init__(self):
        self.color = ""
        self.name = ""

        self.x = 0.0
        self.y = 0.0

bk = Piece()
bk.color = "Black"
bk.name = "King"

wk = Piece()
wk.color = "White"
wk.name = "King"

pieces_type = ['King', 'Queen', 'Bishop', 'Bishop', 'Knight', 'Knight', 'Rook', 'Rook', "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"]
pieces_color = ['White', 'Black']
pieces = []



for c in pieces_color:
    for t in pieces_type:
        p = Piece()
        p.color = c
        p.name = t
        pieces.append(p)

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


    def load_piece(image, pos):
        rect = pygame.Rect(pos)
        obj = pygame.Surface(rect.size).convert()
        obj.blit(image, (0, 0), rect)
        return obj

    screen.fill((200, 200, 200))
    screen.blit(board, board.get_rect())
    pygame.display.update()
