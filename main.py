import pygame

(width, height) = (900, 900)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

background_colour = (255, 255, 255)
screen.fill(background_colour)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False