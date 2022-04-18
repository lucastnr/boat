import pygame
from automaton import Automaton
from constants import size, positions
from images import Images
from fonts.fonts import opensans

x = 1400
y = 200

screen = pygame.display.set_mode(size)
pygame.init()
imgs = Images()

mainLoop = True
automaton = Automaton()

button = pygame.Rect(500, 600, 250, 65)
buttonText = opensans.render("Próximo", True, (255, 255, 255))
state = 0

while mainLoop:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        mainLoop = False
      if event.type == pygame.MOUSEBUTTONUP:
        if button.collidepoint(pygame.mouse.get_pos()):
          automaton.loop()
          state += 1
  screen.blit(imgs.background, [0,0])
  if state <= 7:
    screen.blit(imgs.states[state], [0,720])
  # Desenha botão
  pygame.draw.rect(screen, (200,0,0), button)
  screen.blit(buttonText, (545, 598))
  # Desenha personagens
  characters = [imgs.goat, imgs.wolf, imgs.farmer, imgs.cabbage]
  states = automaton.getStates()
  for i in range(4):
    pos = positions[i][states[i]]
    screen.blit(characters[i], pos)

  pygame.display.update()

pygame.quit()