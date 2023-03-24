import pygame
import time



pygame.init

dis_width = 800
dis_height = 400

Red = (255, 0, 0)
Green = (0, 255, 0)

dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Mygame')
changeColor = 0
gameOver = 0

while(gameOver != 1):


    if changeColor != 255:
         dis.fill((255, changeColor,0))
         changeColor+=1
    else: 
        changeColor=0
    print(changeColor)
    pygame.display.update()


pygame.quit()
quit()


