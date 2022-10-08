import pygame
from states.colors import COLORS
from states.fonts import FONTS
from states.game_images import GAME_IMAGES
from states.shooting.button import Button
from states.shooting.enemy_soldier import EnemySoldier
from states.shooting.health_bar import HealthBar

from states.shooting.level_loader import LEVEL_LOADER
from states.shooting.word import World


from ..base import BaseState

from states.settings import *

class Shooter(BaseState):
    def __init__(self):
        super(Shooter, self).__init__()
        self.next_state = "MENU"
        self.start_game = False

        # group of enemies
        self.enemies = []

        # player action variables
        self.moving_left = False
        self.moving_right = False
        self.shoot = False
        self.grenade = False

        # create World
        self.create_world(1)

        # buttons
        start_img = GAME_IMAGES.get_start_btn_image()
        self.start_button = Button(int(SCREEN_WIDTH // 2) - int(start_img.get_width() // 2), int(SCREEN_HEIGHT // 2 - 100), start_img, 1)
        exit_img = GAME_IMAGES.get_exit_btn_image()
        self.exit_button = Button(int(SCREEN_WIDTH // 2) - int(exit_img.get_width() // 2), int(SCREEN_HEIGHT // 2 + 50), exit_img, 1)
        restart_img = GAME_IMAGES.get_restart_btn_image()
        self.restart_button = Button(int(SCREEN_WIDTH // 2) - int(restart_img.get_width() // 2), int(SCREEN_HEIGHT // 2 - 100), restart_img, 1)


    def create_world(self, level):
        self.world = World()

        # Game levels
        self.level = level

        wd = LEVEL_LOADER.get_level(self.level)
        self.world.process_data(wd.world_data)


    def draw(self, surface):

        if self.start_game == False:
            # menu selection
            surface.fill(COLORS.bgColor)
            if self.start_button.draw(surface):
                self.create_world(self.level)
                self.start_game =  True

            if self.exit_button.draw(surface):
                self.done = True
        else:
            self.run_game(surface)


        if not self.world.player.alive:
            self.world.bg_scroll = 0
            self.world.screen_scroll = 0
            # reset selection
            if self.restart_button.draw(surface):
                self.create_world(self.level)    
            
        
    def run_game(self, surface):

        # draw background
        self.world.draw_bg(surface, COLORS.bgColor)

        # draw world map
        self.world.draw(surface)

        # update player actions
        self.world.update_player_action(surface, self.moving_left, self.moving_right, self.shoot, self.grenade)


    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.shoot = True
            if event.key == pygame.K_q:
                self.grenade = True
            if (event.key == pygame.K_w or event.key == pygame.K_UP) and self.world.player.alive and not self.world.player.in_air:
                self.world.player.jump = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.moving_left = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.shoot = False
            if event.key == pygame.K_q:
                self.grenade = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.moving_left = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.moving_right = False
            if event.key == pygame.K_ESCAPE:
                if self.start_game == False:
                    self.done = True
                else:
                    self.start_game = False
            
