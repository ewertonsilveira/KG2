import pygame
from .base import BaseState

class Menu(BaseState):
    def __init__(self):
        super(Menu, self).__init__()
        self.active_index = 0
        self.options = [("SHOOTER Game","SHOOTER"), ("JUMPER Game", "GAMEPLAY"), ("Quit Game","EXIT")]
        self.next_state = "" #self.options[self.active_index][1]
        self.bgColor = (52, 78, 91)

    def render_text(self, index):
        color = pygame.Color("red") if index == self.active_index else pygame.Color("white")
        return self.font.render(self.options[index][0], True, color)

    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)

    def handle_action(self):
        selection = self.options[self.active_index][1]
        if selection == "EXIT":
            self.quit = True
        else:
            self.done = True
            self.next_state = selection

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if self.active_index > 0 and self.active_index < len(self.options): self.active_index -= 1 
            elif event.key == pygame.K_DOWN:
                if self.active_index >= 0 and self.active_index < len(self.options) - 1: self.active_index += 1 
            elif event.key == pygame.K_RETURN:
                self.handle_action()
            elif event.key == pygame.K_SPACE:
                self.handle_action()

    def draw(self, surface):
        surface.fill(self.bgColor)
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            surface.blit(text_render, self.get_text_position(text_render, index))
