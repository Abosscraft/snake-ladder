import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Snake and Ladders")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

bg = pygame.image.load(f'Snake and ladders board 2.jpg')
bg = pygame.transform.scale( bg, (1000, 800) )

storage_of_file_player = pygame.image.load(f'rook 1.png')
storage_of_file_player = pygame.transform.scale( storage_of_file_player, (40, 50) )

storage_of_file_dice_face = [ pygame.image.load(f'Dice Faces {face}.png') for face in range(1,6+1) ]
storage_of_file_dice_face = [ pygame.transform.scale(image_dice, (150, 150) ) for image_dice in storage_of_file_dice_face ]

class Player():
    def __init__(self, name, player_file, player_x, player_y):
        self.name = name
        self.player_file = player_file
        self.player_x = player_x
        self.player_y = player_y
        self.walk_backwards = False

    def add_image_to_screen(self):
        screen.blit( self.player_file, (self.player_x, self.player_y) )
    
    def walk_backward_from_stage_100(self, count, number):
        even_number_floor = [ 660, 500, 340, 180, 30 ]
        # check state player 
        if self.walk_backwards :
            self.player_x += 100
            if number - count == 0 :
                # back to normal state
                self.walk_backwards = False
        elif self.player_y in even_number_floor and self.player_x != 10:
            self.player_x -= 100
        
        screen.fill( (192, 192, 192) )
        screen.blit(bg, (0,0))
        player1.add_image_to_screen()
        screen.blit( storage_of_file_dice_face[5], (1025, 600) )
        pygame.display.update()
        pygame.time.delay(300)     
        
        # check position player when player arrive stage 100 
        if (self.player_x,self.player_y) == (10, 30) and (number - count) != 0 :
            self.walk_backwards = True

player1 = Player( "Player1", storage_of_file_player, 310 , 30 )

# information about click to roll the dice
d_X = 1025
d_Y = 600
d_click = pygame.image.load("Dice Faces 1.png")
d_click = pygame.transform.scale(d_click, (150,150))
d_rect = pygame.Rect(d_X, d_Y, d_click.get_width(), d_click.get_height())

text_font = pygame.font.SysFont('Arial', 100)
text_font_win = pygame.font.SysFont('Arial', 200)
def draw_text(text, font, text_color, X, Y):
    text_image = font.render(text, True, text_color)
    screen.blit(text_image, (X, Y))

def draw_rect():
    pygame.draw.rect(screen, (245, 245, 245), pygame.Rect(300, 300, 620, 200, border_radius=10))

running = True
running1 = True
current_player_index = 0
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if d_rect.collidepoint(event.pos):
                number = 6
                if number >= 1 :
                    player1.walk_backward_from_stage_100(1, number)
                    pygame.time.delay(100)         
                if number >= 2 :
                    player1.walk_backward_from_stage_100(2, number)    
                    pygame.time.delay(100) 
                if number >= 3 :
                    player1.walk_backward_from_stage_100(3, number)
                    pygame.time.delay(100)       
                if number >= 4 :
                    player1.walk_backward_from_stage_100(4, number)
                    pygame.time.delay(100)     
                if number >= 5 :
                    player1.walk_backward_from_stage_100(5, number)
                    pygame.time.delay(100)     
                if number == 6 :
                    player1.walk_backward_from_stage_100(6, number)
    

    if running1 :
        screen.fill( (192, 192, 192) )
        screen.blit(bg, (0,0))
        player1.add_image_to_screen()
        screen.blit( d_click, (1025, 600) )
        pygame.display.update()     