import pygame
import os
from automato import Automato

size = width, height = 1280, 1060
x = 1280 # - 960
y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

screen = pygame.display.set_mode(size)
pygame.init()

mainLoop = True
paused = False
automato = Automato()

while mainLoop:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        mainLoop = False
      if event.type == pygame.MOUSEBUTTONUP:
        automato.loop()
  screen.fill((0, 0, 0))
  pygame.display.update()

pygame.quit()