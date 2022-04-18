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

    initial = pygame.image.load("images/initial_state.png")
    initial = pygame.transform.scale(initial, [1280, 280])
    state_2 = pygame.image.load("images/state_2.png")
    state_2 = pygame.transform.scale(state_2, [1280, 280])
    state_3 = pygame.image.load("images/state_3.png")
    state_3 = pygame.transform.scale(state_3, [1280, 280])
    state_4 = pygame.image.load("images/state_4.png")
    state_4 = pygame.transform.scale(state_4, [1280, 280])
    state_5 = pygame.image.load("images/state_5.png")
    state_5 = pygame.transform.scale(state_5, [1280, 280])
    state_6 = pygame.image.load("images/state_6.png")
    state_6 = pygame.transform.scale(state_6, [1280, 280])
    state_7 = pygame.image.load("images/state_7.png")
    state_7 = pygame.transform.scale(state_7, [1280, 280])
    state_8 = pygame.image.load("images/state_8.png")
    state_8 = pygame.transform.scale(state_8, [1280, 280])

    self.states = [initial, state_2, state_3, state_4, state_5, state_6, state_7, state_8]