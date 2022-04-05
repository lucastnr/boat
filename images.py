import pygame
from constants import size

class Images:
  def __init__(self):
    self.background = pygame.image.load("images/background.png")
    pygame.transform.scale(self.background, size)
    self.farmer = pygame.image.load("images/farmer.png")
    self.farmer = pygame.transform.scale(self.farmer, [180, 200])
    self.cabbage = pygame.image.load("images/cabbage.png")
    self.cabbage = pygame.transform.scale(self.cabbage, [55, 42])

    self.goat = pygame.image.load("images/goat.png")
    self.wolf = pygame.image.load("images/wolf.png")