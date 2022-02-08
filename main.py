import pygame
import sys

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
(width, height) = (900, 900)

screen = pygame.display.set_mode((width, height))
pygame.display.flip()

background_colour = (255, 255, 255)
screen.fill(background_colour)


def PrintText(text, screen):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(text, True, BLACK)
 
    textRect = text.get_rect()
 
    textRect.center = (width // 2, height // 2)

    screen.blit(text, textRect)

def InputText(pygame):
  colour_active = False
  base_font = pygame.font.Font(None, 32)
  user_text = ''

  input_rect = pygame.Rect(450, 450, 140, 32)
  rect_passive = pygame.Color('chartreuse4')

  if event.type == pygame.MOUSEBUTTONDOWN:
        
    if input_rect.collidepoint(event.pos):
      colour_active = True
    else:
      colour_active = False
    
    if event.type == pygame.KEYDOWN:
  
            # Check for backspace
      if event.key == pygame.K_BACKSPACE:
        user_text = user_text[:-1]
      else:
        user_text += event.unicode

    if colour_active:
        rect_passive = colour_active
    else:
        rect_passive = colour_active
        
    pygame.draw.rect(screen, rect_passive, input_rect)
    
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    input_rect.center = (width // 2, height // 2)
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(100, text_surface.get_width()+10)
    
  return user_text

while True:
    PrintText(text = )

    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    pygame.display.flip()