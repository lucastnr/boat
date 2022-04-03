
import pygame
from constants import size

class Images:
  def __init__(self):
    self.background = pygame.image.load("images/background.png")
    pygame.transform.scale(self.background, size)