import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Snake and Ladders")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)
                       
bg = pygame.image.load('Snake and ladders board.jpg')
bg = pygame.transform.scale( bg, (1000, 800) )
                        
#Player
storage_of_file_player = [ pygame.image.load(f'rook {count}.png') for count in range(1,2+1) ]
storage_of_file_dice_face = [ pygame.image.load(f'Dice Faces {face}.jpg') for face in range(1,6+1) ] 


font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 1000
text_y = 600


class Player():
    def __init__(self, name, player_file, player_x, player_y):
        self.name = name
        self.player_file = player_file
        self.player_x = player_x
        self.player_y = player_y
        self.position = 1

    def add_image_to_screen(self):
        screen.blit( self.player_file, (self.player_x, self.player_y) )

    def move(self,dice_roll):
        self.position += dice_roll
        if self.position in good_stage:
            self.position = good_stage[self.position]
        elif self.position in bad_stage:
            self.position = bad_stage[self.position]

        #Update x and y position
        self.update_screen_position()
        
    def update_screen_position(self):
        row = (self.position - 1) // 10
        
        if row % 2 == 0:
            column = (self.position - 1) % 10 
        else:
            column = (9 - self.position) % 10
        
        self.player_x = 10 + column * 100
        self.player_y = 730 - row * 80

    def turn(self) :
        return f'{self.name} Turn'
        
#Transform size image
storage_of_file_player = [ pygame.transform.scale(image_player ,(40, 50) ) for image_player in storage_of_file_player ]
storage_of_file_dice_face = [ pygame.transform.scale(image_dice, (150, 150) ) for image_dice in storage_of_file_dice_face ]

players = [] 
for index in range(len(storage_of_file_player)) :
    if index == 0 :
        players.append( Player("Human", storage_of_file_player[0], 10 , 730) ) #y730 -> 660 -> 580 -> 500 -> 420 -> 340 -> 260 -> 180 -> 100 -> 30 
    if index == 1 :
        players.append( Player("Bot", storage_of_file_player[1], 45, 730))  #45, 730

def roll_the_dice():
    return random.randint(1, 6)

def show_turn():
    pass
    

good_stage = { 3 : 45, 8 : 12, 14 : 26, 21 : 39, 31 : 73, 59 : 80, 83 : 97, 90 : 92 }
bad_stage = { 11 : 6, 54 : 27, 57 : 2, 78 : 15, 89 : 85, 95 : 67 }
move_up = { 730 : 660, 660 :580, 580 : 500, 500 : 420, 420 : 340, 340 :260, 260 : 180, 180 :100, 100 : 30 }

running = True

#Main Game Loop
current_player_index = 0
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            dice_roll = roll_the_dice()   
            print(dice_roll)
            players[current_player_index].move(dice_roll)
            current_player_index = (current_player_index + 1) % len(players) #Switch turn
            
    screen.fill( (192, 192, 192) )
    screen.blit(bg, (0, 0))
    players[0].add_image_to_screen()
    players[1].add_image_to_screen()
    screen.blit( storage_of_file_dice_face[1], (1025, 600) )
    pygame.display.update()