import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Snake and Ladders")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

bg = pygame.image.load(f'Snake and ladders board 1.jpg')
bg = pygame.transform.scale(bg,(1000,800))

storage_of_file_dice_face = [ pygame.image.load(f'Dice Faces {face}.png') for face in range(1,6+1) ] 
storage_of_file_dice_face = [ pygame.transform.scale(image_dice, (150, 150) ) for image_dice in storage_of_file_dice_face ]

# information about click to roll the dice
d_X = 1025
d_Y = 600
d_click = pygame.image.load("Dice Faces 1.png")
d_click = pygame.transform.scale(d_click, (150,150))
d_rect = pygame.Rect(d_X, d_Y, d_click.get_width(), d_click.get_height())

running = True
running1 = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if d_rect.collidepoint(event.pos):
                print("check")
                number = random.randint(1,6)
                print(number)
                for i in range(1,7):
                    screen.blit(storage_of_file_dice_face[i-1] ,(1025, 600))
                    pygame.display.update()
                    pygame.time.delay(300)
                for i in range(1,8):
                    if i == 7:
                        screen.blit(storage_of_file_dice_face[number-1] ,(1025, 600))
                        pygame.display.update()
                        running1 = False
                    else:
                        screen.blit(storage_of_file_dice_face[i-1] ,(1025, 600))
                        pygame.display.update()
                        pygame.time.delay(300)
    
    if running1:
        screen.fill( (192, 192, 192) )
        screen.blit(bg,(0,0))
        screen.blit(d_click,(1025, 600))              
        pygame.display.update()