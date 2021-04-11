import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))  # Vous définissez la taille de fenêtre de votre jeu
pygame.display.set_caption("Echecs")

board = pygame.Surface((480, 480))
board.fill((175, 141, 120))
image = pygame.image.load("img.png").convert()


def load_piece(image, pos):
    rect = pygame.Rect(pos)
    obj = pygame.Surface(rect.size).convert()
    obj.blit(image, (0, 0), rect)
    return obj

pieces = [
    Piece(load_piece(image, (68, 70, 85, 85)), "King", "Black", 85 * 4, 0, screen),
    Piece(load_piece(image, (234, 70, 85, 85)), "Queen", "Black", 85 * 3, 0, screen),
    Piece(load_piece(image, (400, 70, 85, 85)), "Rook", "Black", 85 * 0, 0, screen),
    Piece(load_piece(image, (400, 70, 85, 85)), "Rook", "Black", 85 * 7, 0, screen),
    Piece(load_piece(image, (566, 70, 85, 85)), "Bishop", "Black", 85 * 2, 0, screen),
    Piece(load_piece(image, (566, 70, 85, 85)), "Bishop", "Black", 85 * 5, 0, screen),
    Piece(load_piece(image, (736, 70, 85, 85)), "Knight", "Black", 85 * 1, 0, screen),
    Piece(load_piece(image, (736, 70, 85, 85)), "Knight", "Black", 85 * 6, 0, screen),
    Piece(load_piece(image, (902, 70, 85, 85)), "Pawn", "Black", 85 * 0, 85, screen),
    Piece(load_piece(image, (902, 70, 85, 85)), "Pawn", "Black", 85 * 1, 85, screen),
    Piece(load_piece(image, (902, 70, 85, 85)), "Pawn", "Black", 85 * 2, 85, screen),
    Piece(load_piece(image, (902, 70, 85, 85)), "Pawn", "Black", 85 * 3, 85, screen),
    Piece(load_piece(image, (902, 70, 85, 85)), "Pawn", "Black", 85 * 4, 85, screen),
    Piece(load_piece(image, (902, 70, 85, 85)), "Pawn", "Black", 85 * 5, 85, screen),
    Piece(load_piece(image, (902, 70, 85, 85)), "Pawn", "Black", 85 * 6, 85, screen),
    Piece(load_piece(image, (902, 70, 85, 85)), "Pawn", "Black", 85 * 7, 85, screen),
    Piece(load_piece(image, (68, 214, 85, 85)), "King", "White", 85 * 4, 85 * 7, screen),
    Piece(load_piece(image, (234, 214, 85, 85)), "Queen", "White", 85 * 3, 85 * 7, screen),
    Piece(load_piece(image, (400, 214, 85, 85)), "Rook", "White", 85 * 0, 85 * 7, screen),
    Piece(load_piece(image, (400, 214, 85, 85)), "Rook", "White", 85 * 7, 85 * 7, screen),
    Piece(load_piece(image, (566, 214, 85, 85)), "Bishop", "White", 85 * 2, 85 * 7, screen),
    Piece(load_piece(image, (566, 214, 85, 85)), "Bishop", "White", 85 * 5, 85 * 7, screen),
    Piece(load_piece(image, (736, 214, 85, 85)), "Knight", "White", 85 * 1, 85 * 7, screen),
    Piece(load_piece(image, (736, 214, 85, 85)), "Knight", "White", 85 * 6, 85 * 7, screen),
    Piece(load_piece(image, (902, 214, 85, 85)), "Pawn", "White", 85 * 0, 85 * 6, screen),
    Piece(load_piece(image, (902, 214, 85, 85)), "Pawn", "White", 85 * 1, 85 * 6, screen),
    Piece(load_piece(image, (902, 214, 85, 85)), "Pawn", "White", 85 * 2, 85 * 6, screen),
    Piece(load_piece(image, (902, 214, 85, 85)), "Pawn", "White", 85 * 3, 85 * 6, screen),
    Piece(load_piece(image, (902, 214, 85, 85)), "Pawn", "White", 85 * 4, 85 * 6, screen),
    Piece(load_piece(image, (902, 214, 85, 85)), "Pawn", "White", 85 * 5, 85 * 6, screen),
    Piece(load_piece(image, (902, 214, 85, 85)), "Pawn", "White", 85 * 6, 85 * 6, screen),
    Piece(load_piece(image, (902, 214, 85, 85)), "Pawn", "White", 85 * 7, 85 * 6, screen)]

for x in range(0, 8, 2):
    for y in range(0, 8, 2):
        pygame.draw.rect(board, (250, 240, 230), (x * 60, y * 60, 60, 60))

for x in range(1, 9, 2):
    for y in range(1, 9, 2):
        pygame.draw.rect(board, (250, 240, 230), (x * 60, y * 60, 60, 60))

while True:  # C'est ce qu'on appelle une boucle de jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # L'utilisateur a cliqué sur le X de la fenêtre
            sys.exit()

        elif event.type == pygame.MOUSEMOTION:
            pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                print(x, y)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                x, y = event.pos
                print(x, y)

    for piece in pieces:
        print(f"{piece.color} {piece.name}: {piece.x} x {piece.y} vs {x // 85 * 85}x{y // 85 * 85}")
        if (x // 85 == piece.x // 85) and (y // 85 == piece.y // 85):
            print(piece.color, piece.name)
        break


    screen.fill((200, 200, 200))
    # pygame.display.flip()
    screen.blit(board, board.get_rect())

    for piece in pieces:
        piece.rect = piece.image.get_rect()
        piece.rect.topleft = piece.x, piece.y
        piece.screen.blit(piece.image, piece.rect)

    pygame.display.update()


