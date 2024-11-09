import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Snake and Ladders")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)
                    

font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 1000
text_y = 600


class Map():
    def __init__(self, file) :
        self.players = []
        self.file = file


    def add_player(self, player) :
        self.players.append( player )

    def show_map(self):
        screen.blit(self.file, (0, 0) )


    def player_walk(self, current_player_index, count, number) :
        human_Upturn_R = [ (910,730), (910,580), (910,420), (910,260), (910,100)]
        move_up = { 730 : 660, 660 : 580, 580 : 500, 500 : 420, 420 : 340, 340 : 260, 260 : 180, 180 : 100, 100 : 30 }
        human_Upturn_L = [ (10,660), (10,500), (10,340), (10,180) ]
        bot_Upturn_R = [ (945,730), (945,580), (945,420), (945,260), (945,100)]
        bot_Upturn_L = [ (45,660), (45,500), (45,340), (45,180) ]
        walk_right_to_left = [ 660, 500, 340, 180, 30 ]


        if current_player_index == 0 :
            if self.players[current_player_index].player_x == 10 and self.players[current_player_index].player_y == 30 and (number - count) != 0:
                self.players[current_player_index].walk_backwards = True

            if self.players[current_player_index].walk_backwards :
                self.players[current_player_index].player_x += 100
                if count == number :
                    self.players[current_player_index].walk_backwards = False
            else :
                if (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in human_Upturn_R :
                    self.players[current_player_index].player_y = move_up[ self.players[current_player_index].player_y ] 
                elif (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in human_Upturn_L :
                    self.players[current_player_index].player_y = move_up[ self.players[current_player_index].player_y ]
                elif self.players[current_player_index].player_y in [ y[1] for y in human_Upturn_R ]:
                    self.players[current_player_index].player_x += 100
                elif self.players[current_player_index].player_y in walk_right_to_left :
                    self.players[current_player_index].player_x -= 100
        elif current_player_index == 1 :
            if self.players[current_player_index].player_x == 45 and self.players[current_player_index].player_y == 30 and (number - count) != 0:
                self.players[current_player_index].walk_backwards = True

            if self.players[current_player_index].walk_backwards :
                self.players[current_player_index].player_x += 100
                if count == number :
                    self.players[current_player_index].walk_backwards = False
            else :
                if (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in bot_Upturn_R :
                    self.players[current_player_index].player_y = move_up[ self.players[current_player_index].player_y ]
                elif (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in bot_Upturn_L :
                    self.players[current_player_index].player_y = move_up[ self.players[current_player_index].player_y ]
                elif self.players[current_player_index].player_y in [ y[1] for y in bot_Upturn_R ]:
                    self.players[current_player_index].player_x += 100
                elif self.players[current_player_index].player_y in walk_right_to_left :
                    self.players[current_player_index].player_x -= 100

        screen.fill( (192, 192, 192) )
        all_bg[0].show_map()
        all_bg[0].players[0].add_image_to_screen()
        all_bg[0].players[1].add_image_to_screen()
        screen.blit( storage_of_file_dice_face[0], (1025, 600) )
        pygame.display.flip()
        pygame.time.delay(100)
        
        human_ladder = [ [(210,730),(410,420)], [(710,730),(810,660)], [(610,660),(510,580)],[(10,580),(110,500)],[(910,500),(710,180)],[(110,340),(10,180)],[(210,100),(310,30)],[(910,100),(810,30)]]
        human_d_ladder = { (l[0]) : l[1] for l in human_ladder }
        bot_ladder = [ [ (l[0][0] + 35 , l[0][1] ), (l[1][0] + 35, l[1][1]) ] for l in human_ladder ]
        bot_d_ladder = { (l[0]) : l[1] for l in bot_ladder }
        
        snake = [ [(11,910,660),(6,510,730)] , [(54,610,340),(27,610,580)] , [(57,310,340),(2,110,730)] , [(78,210,180),(15,510,660)] , [(89,810,100),(85,410,100)] , [(95,510,30),(67,610,260)] , [(99,110,30),(41,10,420)] ]
        human_snake = [ [(910,660),(510,730)] , [(610,340),(610,580)] , [(310,340),(110,730)] , [(210,180),(510,660)] , [(810,100),(410,100)] , [(510,30),(610,260)] , [(110,30),(10,420)] ]
        human_d_snake = { (z[0]) : z[1] for z in human_snake }
        bot_snake = [ [ (z[0][0] + 35, z[0][1]), (z[1][0] + 35, z[1][1]) ]  for z in human_snake]
        bot_d_snake = { (z[0]) : z[1] for z in bot_snake }

        # Movement Ladder Snake
        if count == number :
            print('check1')
            if current_player_index == 0 :
                if (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in [ (l[0][0], l[0][1]) for l in human_ladder ] :
                    (self.players[current_player_index].player_x, self.players[current_player_index].player_y) = human_d_ladder[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)]
                elif (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in [ (l[0][0], l[0][1]) for l in human_snake ] :
                    (self.players[current_player_index].player_x, self.players[current_player_index].player_y) = human_d_snake[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)]
            elif current_player_index == 1 :
                if (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in [ (l[0][0], l[0][1]) for l in bot_ladder ] :
                    (self.players[current_player_index].player_x, self.players[current_player_index].player_y) = bot_d_ladder[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)]
                elif (self.players[current_player_index].player_x, self.players[current_player_index].player_y) in [ (l[0][0], l[0][1]) for l in bot_snake ] :
                    (self.players[current_player_index].player_x, self.players[current_player_index].player_y) = bot_d_snake[(self.players[current_player_index].player_x, self.players[current_player_index].player_y)]

        # Result 
        if current_player_index == 0 :
            if self.players[current_player_index].player_x == 10 and self.players[current_player_index].player_y == 30 and (number - count) == 0:
                print("You Win")
        if current_player_index == 1 :
            if self.players[current_player_index].player_x == 45 and self.players[current_player_index].player_y == 30 and (number - count) == 0:
                print("You lose")


        screen.fill( (192, 192, 192) )
        all_bg[0].show_map()
        all_bg[0].players[0].add_image_to_screen()
        all_bg[0].players[1].add_image_to_screen()
        screen.blit( storage_of_file_dice_face[0], (1025, 600) )
        pygame.display.flip()
        pygame.time.delay(100)
#        screen.fill( (192, 192, 192) )
#        all_bg[0].show_map()
#        all_bg[0].players[0].add_image_to_screen()
#        all_bg[0].players[1].add_image_to_screen()
#        screen.blit( storage_of_file_dice_face[0], (1025, 600) )
#        pygame.display.update()
    #        ladder = [ [(3,210,730),(45,410,420)], [(8,710,730),(12,810,660)], [(14,610,660),(26,510,580)],[(21,10,580),(39,110,500)],[(31,910,500),(73,710,180)],[(59,110,340),(80,10,180)],[(83,210,100),(97,310,30)],[(90,910,100),(92,810,30)]]

Upturn_L = [(20,10,660),(21,10,580),[(40,10,500),(41,10,420)],[(60,10,340),(61,10,260)],[(80,10,180),(81,10,100)]]
Upturn_R = [[(10,910,730),(11,910,660)],[(30,910,580),(31,910,500)],[(50,910,420),(51,910,340)],[(70,910,260),(71,910,180)],[(90,910,100),(91,910,30)]]


class Player():
    def __init__(self, name, player_file, player_x, player_y):
        self.name = name
        self.player_file = player_file
        self.player_x = player_x
        self.player_y = player_y
        self.walk_backwards = False

    def add_image_to_screen(self):
        screen.blit( self.player_file, (self.player_x, self.player_y) )


bg = [ pygame.image.load(f'Snake and ladders board.jpg') for number in range(1) ]
bg = [ pygame.transform.scale( file_bg, (1000, 800) ) for file_bg in bg ]
all_bg = [ Map(file_bg) for file_bg in bg ]


storage_of_file_player = [ pygame.image.load(f'rook {count}.png') for count in range(1,2+1) ]
storage_of_file_dice_face = [ pygame.image.load(f'Dice Faces {face}.jpg') for face in range(1,6+1) ] 

storage_of_file_player = [ pygame.transform.scale(image_player ,(40, 50) ) for image_player in storage_of_file_player ]
storage_of_file_dice_face = [ pygame.transform.scale(image_dice, (150, 150) ) for image_dice in storage_of_file_dice_face ]


for index in range(len(storage_of_file_player)) :
    if index == 0 :
        all_bg[0].add_player(Player("Human", storage_of_file_player[0], 10 , 730)) #y730 -> 660 -> 580 -> 500 -> 420 -> 340 -> 260 -> 180 -> 100 -> 30 
    if index == 1 :
        all_bg[0].add_player( Player("Bot", storage_of_file_player[1], 45, 730))  #45, 730


running = True
current_player_index = 0

while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and ( 1025 <= event.pos[0] <= 1175 ) and ( 600 <= event.pos[1] <= 750 ) :
                number = random.randint(1,6)
                print(number)
                if number >= 1 :
                    count = all_bg[0].player_walk(current_player_index, 1, number)  
                pygame.time.delay(100)         
                if number >= 2 :
                    count = all_bg[0].player_walk(current_player_index, 2, number)    
                pygame.time.delay(100) 
                if number >= 3 :
                    count = all_bg[0].player_walk(current_player_index, 3, number)
                pygame.time.delay(100)       
                if number >= 4 :
                    count = all_bg[0].player_walk(current_player_index, 4, number)
                pygame.time.delay(100)     
                if number >= 5 :
                    count = all_bg[0].player_walk(current_player_index, 5, number)
                pygame.time.delay(100)     
                if number == 6 :
                    count = all_bg[0].player_walk(current_player_index, 6, number)                                     
                
                current_player_index = (current_player_index + 1) % 2


    if running :
        screen.fill( (192, 192, 192) )
        all_bg[0].show_map()
        all_bg[0].players[0].add_image_to_screen()
        all_bg[0].players[1].add_image_to_screen()
        screen.blit( storage_of_file_dice_face[0], (1025, 600) )
        pygame.display.flip()
