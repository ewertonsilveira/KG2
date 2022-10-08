import pygame
from states.settings import * 

WHOLE_SCREEN_FADE = 1
VERTICAL_SCREEN_FADE_DOWN = 2

class ScreenFade():
    def __init__(self, direction, color, speed):
        self.speed = speed
        self.color = color
        self.direction = direction
        self.fade_counter = 0

    def run_effect(self, surface):
        self.fade_counter += self.speed

        if self.direction == WHOLE_SCREEN_FADE:
            pygame.draw.rect(surface, self.color, (0 - self.fade_counter, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT))
            pygame.draw.rect(surface, self.color, (SCREEN_WIDTH // 2 + self.fade_counter, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.draw.rect(surface, self.color, (0, 0 - self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT // 2))
            pygame.draw.rect(surface, self.color, (0, SCREEN_HEIGHT // 2 +self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT))
        elif self.direction == VERTICAL_SCREEN_FADE_DOWN:
            pygame.draw.rect(surface, self.color, (0, 0, SCREEN_WIDTH, 0 + self.fade_counter))

        return self.fade_counter >= SCREEN_HEIGHT