import pygame
import sys

pygame.init()

(width, height) = (900, 900)

screen = pygame.display.set_mode((width, height))
pygame.display.flip()

background_colour = (255, 255, 255)
screen.fill(background_colour)

base_font = pygame.font.Font(None, 32)
user_text = ''

input_rect = pygame.Rect(450, 450, 140, 32)

rect_colour = pygame.Color('lightskyblue3')
rect_passive = pygame.Color('chartreuse4')

colour_active = False

while True:
  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    
    if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                colour_active = True
            else:
                colour_active = False
    
    if event.type == pygame.KEYDOWN:
  
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
  
            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode

    if colour_active:
        rect_passive = colour_active
    else:
        rect_passive = colour_active
        
    pygame.draw.rect(screen, rect_passive, input_rect)
    
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(100, text_surface.get_width()+10)
    
    pygame.display.flip()