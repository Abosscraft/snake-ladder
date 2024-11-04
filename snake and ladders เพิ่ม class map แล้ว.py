import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Snake and Ladders")
icon = pygame.image.load('anaconda.png')
pygame.display.set_icon(icon)
                    

font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 1000
text_y = 600


class Player():
    def __init__(self, name, player_file, player_x, player_y):
        self.name = name
        self.player_file = player_file
        self.player_x = player_x
        self.player_y = player_y
        

    def add_image_to_screen(self):
        screen.blit( self.player_file, (self.player_x, self.player_y) )

    def walk(self, change_x, change_y) :
        screen.blit( self.player_file, (self.player_x + 1, self.player_y ))

        
class Map():
    def __init__(self, file) :
        self.players = []
        self.file = file


    def add_player(self, player) :
        self.players.append( player )

    def show_map(self):
        screen.blit(self.file, (0, 0) )

    def good_stage(self) :
        all_good_stage = { 3 : 45, 8 : 12, 14 : 26, 21 : 39, 31 : 73, 59 : 80, 83 : 97, 90 : 92 }

    def bad_stage(self) :
        all_bad_stage = { 11 : 6, 54 : 27, 57 : 2, 78 : 15, 89 : 85, 95 : 67 }


bg = [ pygame.image.load(f'Snake and ladders board.jpg') for number in range(1) ]
bg = [ pygame.transform.scale( file_bg, (1000, 800) ) for file_bg in bg ]
all_bg = [ Map(file_bg) for file_bg in bg ]


storage_of_file_player = [ pygame.image.load(f'rook {count}.png') for count in range(1,2+1) ]
storage_of_file_dice_face = [ pygame.image.load(f'Dice Faces {face}.jpg') for face in range(1,6+1) ] 

storage_of_file_player = [ pygame.transform.scale(image_player ,(40, 50) ) for image_player in storage_of_file_player ]
storage_of_file_dice_face = [ pygame.transform.scale(image_dice, (150, 150) ) for image_dice in storage_of_file_dice_face ]


players = [] 
for index in range(len(storage_of_file_player)) :
    if index == 0 :
        players.append( Player("Human", storage_of_file_player[0], 10 , 30) ) #y730 -> 660 -> 580 -> 500 -> 420 -> 340 -> 260 -> 180 -> 100 -> 30 
    if index == 1 :
        players.append( Player("Bot", storage_of_file_player[1], 40, 730))  #45, 730


move_up = { 730 : 660, 660 :580, 580 : 500, 500 : 420, 420 : 340, 340 :260, 260 : 180, 180 :100, 100 : 30 }

running = True

while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        else :
            screen.fill( (192, 192, 192) )
            all_bg[0].show_map() 
            players[0].add_image_to_screen()
            players[1].add_image_to_screen()
            screen.blit( storage_of_file_dice_face[0], (1025, 600) )
            pygame.display.update()

exit()