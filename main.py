import pygame
import os
from automaton import Automaton
from constants import size
from images import Images


x = 1400
y = 200
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

screen = pygame.display.set_mode(size)
pygame.init()

imgs = Images()

mainLoop = True
paused = False
automaton = Automaton()

while mainLoop:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        mainLoop = False
      if event.type == pygame.MOUSEBUTTONUP:
        automaton.loop()
  screen.fill((0, 0, 0))
  screen.blit(imgs.background, [0,0])
  pygame.display.update()

pygame.quit()