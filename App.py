import sys
import pygame
from  CHECKER.const import WHITE
from CHECKER.const import SCREEN_HEIGTH, SCREEN_WIDTH
from CHECKER.const import SQUARE_SIZE, BOARD_SIZE
from CHECKER.game import Game
from AI.Algorithm import findTheWay

pygame.init()

WIN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
pygame.display.set_caption('OUR FUCKING GAME')

FPS = 60

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    myGame = Game(WIN)
    while run:
        clock.tick(FPS)

        if myGame.winner() :
            run = False

        if myGame.turn == WHITE:
            # 4 là độ sâu vừa đủ để tìm không quá lâu
            # mà cũng vừa đủ thông minh :)))
            value, new_board = findTheWay(myGame.get_board(), 4, WHITE, myGame)
            myGame.ai_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[0] < BOARD_SIZE and pos[1] < BOARD_SIZE:
                        row, col = get_row_col_from_mouse(pos)
                        myGame.select(row, col)
        myGame.update()

    pygame.quit()
    sys.exit()
    
main()