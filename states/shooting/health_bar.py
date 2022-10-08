import pygame
from states.colors import COLORS
from states.settings import * 

class HealthBar():
    def __init__(self, x, y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health

    def draw(self, surface, health):
        #update with new health
        self.health = health
        #calculate health ratio
        ratio = self.health / self.max_health
        pygame.draw.rect(surface, COLORS.BLACK, (self.x - 2, self.y - 2, 154, 24))
        pygame.draw.rect(surface, COLORS.RED, (self.x, self.y, 150, 20))
        pygame.draw.rect(surface, COLORS.GREEN, (self.x, self.y, 150 * ratio, 20))
