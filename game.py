import pygame
import sys
from pygame import font
from pygame import draw


def check_win(empty_square,sign):
    zero = 0
    for row in empty_square:
        zero += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if empty_square[0][col] == sign and empty_square [1][col] == sign and empty_square[2][col] == sign:
            return sign
    if empty_square[0][0] == sign and empty_square[1][1] == sign and empty_square[2][2] == sign:
        return sign
    if empty_square[0][2] == sign and empty_square[1][1] == sign and empty_square[2][0] == sign:
        return sign
    if zero == 0:
        return "Ничья"
    return False
pygame.init()

size_block = 300
margin = 15
width = height = size_block*3 + margin*4
size_window = (width,height)
screen = pygame.display.set_mode((size_window))
pygame.display.set_caption("Крестики-Нолики")
black = (0,0,0)
red = (255,99,71)
blue = (0,191,255)
white = (255,255,255)
empty_square = [[0] * 3 for i in range(3)]
counter = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block+margin)
            row = y_mouse // (size_block + margin)
            if empty_square [row][col] == 0:
              if counter % 2 == 0:
                  empty_square [row][col]= 'x'
              else:
                  empty_square [row][col]= 'o'
              counter +=1
    for row in range(3):
        for col in range(3):
           if empty_square[row][col] == 'x':
            color = red
           elif empty_square[row][col] == 'o':
            color = blue
           else:
            color = white
           x = col*size_block + (col+1)*margin
           y = row*size_block + (row+1)*margin
           pygame.draw.rect(screen,color, (x,y,size_block,size_block))
           if color == red:
               pygame.draw.line(screen,white,(x,y),(x + size_block,y + size_block),10)
               pygame.draw.line(screen, white, (x + size_block, y), (x, y + size_block), 10)
           elif color == blue:
               pygame.draw.circle(screen,white,(x + size_block // 2, y + size_block // 2),size_block // 2,10)
    if (counter - 1) % 2 == 0:
     end = check_win(empty_square,"x")
    else:
     end = check_win(empty_square, "o")
    if end:
        screen.fill(black)
        font = pygame.font.SysFont('lucidaconsole',250)
        text1 = font.render(end,True,white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1,[text_x,text_y])
    pygame.display.update()