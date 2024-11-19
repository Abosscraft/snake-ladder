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

class Player:
    def __init__(self, name, player_file, player_x, player_y):
        self.name = name
        self.player_file = player_file
        self.player_x = player_x
        self.player_y = player_y

    def add_image_to_screen(self):
        screen.blit( self.player_file, (self.player_x, self.player_y) )


    def walk(self,count,number):
        self.player_x += 100
        screen.fill( (192, 192, 192) )
        screen.blit(bg,(0,0))
        screen.blit(storage_of_file_dice_face[number-1] ,(1025, 600))
        player1.add_image_to_screen()          
        pygame.display.update()
        pygame.time.delay(200)

        human_ladder =  {(210,730):(410,420)}
        player1_animation_ladder = {(210, 730) : [15, -21]}
        if count == number:
            if (player1.player_x, player1.player_y) in human_ladder:
                ani_x = player1_animation_ladder[(player1.player_x, player1.player_y)][0]
                ani_y = player1_animation_ladder[(player1.player_x, player1.player_y)][1]
                limit_x = human_ladder[(player1.player_x, player1.player_y)][0]
                limit_y = human_ladder[(player1.player_x, player1.player_y)][1]
                if limit_x > player1.player_x:
                    while player1.player_x <= limit_x and player1.player_y >= limit_y:
                        if player1.player_x >= limit_x and player1.player_y <= limit_y:
                            player1.player_x, player1.player_y = limit_x, limit_y
                            break
                        
                        player1.player_x += ani_x
                        player1.player_y += ani_y

                        screen.fill((192, 192, 192))
                        screen.blit(bg, (0, 0))
                        screen.blit(storage_of_file_dice_face[number-1], (1025, 600))
                        player1.add_image_to_screen()
                        pygame.display.update()
                        pygame.time.delay(200)
                    player1.player_x, player1.player_y = 410, 420    

p_file = pygame.image.load('rook 1.png')
p_file = pygame.transform.scale(p_file,(40,50))
player1 = Player('player1',p_file,10,730)

running = True
running1 = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if d_rect.collidepoint(event.pos):
                print('Climb')
                number = 2
            for i in range(1,7):
                screen.blit(storage_of_file_dice_face[i-1],(1025,600))
                pygame.display.update()
                pygame.time.delay(100)
            for i in range(1,8):
                if i == 7:
                    screen.blit(storage_of_file_dice_face[number-1],(1025,600))
                    pygame.display.update()
                    pygame.time.delay(100)
                else:
                    screen.blit(storage_of_file_dice_face[i-1],(1025,600))
                    pygame.display.update()
                    pygame.time.delay(100)
            if number >= 1 :
                player1.walk( 1, number)  
                pygame.time.delay(100)         
            if number >= 2 :
                player1.walk( 2, number)    
                pygame.time.delay(100) 

    if running1:
        screen.fill( (192, 192, 192) )
        screen.blit(bg,(0,0))
        screen.blit(d_click,(1025, 600))  
        player1.add_image_to_screen()          
        pygame.display.update()