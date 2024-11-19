import pygame
pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Snake and Ladders")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

bg = [ pygame.image.load(f'Snake and ladders board {number}.jpg') for number in range(1,3)  ]
bg = [ pygame.transform.scale(image,(1000,800)) for image in bg ]
# information about choose map 
bg1_X = 100
bg1_Y = 250 
bg2_X = 650
bg2_Y = 250
bg_for_select = [ pygame.image.load(f'Snake and ladders board {number}.jpg') for number in range(1,2+1) ] 
bg_for_select = [ pygame.transform.scale(map, (450, 450)) for map in bg_for_select ]
bg1_rect = pygame.Rect(bg1_X, bg1_Y, bg_for_select[0].get_width(), bg_for_select[0].get_height() )
bg2_rect = pygame.Rect(bg2_X, bg2_Y, bg_for_select[1].get_width(), bg_for_select[1].get_height() )

text_font = pygame.font.SysFont('Arial', 100)
text_font_win = pygame.font.SysFont('Arial', 200)
def draw_text(text, font, text_color, X, Y):
    text_image = font.render(text, True, text_color)
    screen.blit(text_image, (X, Y))

def draw_rect():
    pygame.draw.rect(screen, (245, 245, 245), pygame.Rect(300, 300, 750, 200, border_radius=10))

running = True
running1 = True
running2 = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if bg1_rect.collidepoint(event.pos):
                selected_map = 0
                running1 = False
                running2 = True
            elif bg2_rect.collidepoint(event.pos):
                selected_map = 1
                running1 = False
                running2 = True

    if running1:
        screen.fill( (192, 192, 192) )
        draw_text('Choose map',text_font,(0,0,0),370,60)
        screen.blit(bg_for_select[0], (100, bg1_Y))
        screen.blit(bg_for_select[1], (650, bg2_Y))
        pygame.display.update()
    elif running2:
        screen.fill( (192, 192, 192) )
        screen.blit(bg[selected_map],(0,0))
        pygame.display.update()