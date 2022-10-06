import pygame
from states.game_images import GAME_IMAGES

from states.settings import COLS, ENEMY_BASE_HEALTH, ENEMY_INITIAL_BULLETS, ENEMY_INITIAL_GRENADES, ENEMY_RUN_SPEED, GROUND, PLAYERS_SCALE, SOLDIER_BASE_HEALTH, SOLDIER_INITIAL_BULLETS, SOLDIER_INITIAL_GRENADES, TILE_SIZE
from states.shooting.enemy_soldier import EnemySoldier
from states.shooting.health_bar import HealthBar
from states.shooting.soldier import Soldier

class World(object):
    def __init__(self):        
        self.obstacle_list = []
        self.enemies = []
        self.player = None
        self.health_bar = None

    def process_data(self, data):
        imgs = GAME_IMAGES.get_world_images()
        for x, row in enumerate(data):
            for y, t in enumerate(row):
                tile = int(t)
                if tile >= 0:
                    img = imgs[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)

                    if tile <= 8: # dirt
                        self.obstacle_list.append(tile_data)
                    elif tile >= 9 and tile <= 10:
                        # water
                        pass
                    elif tile >= 11 and tile <= 14:
                        # decoration
                        pass 
                    elif tile == 15:
                        # player
                        self.player = self.create_player()
                        self.health_bar = self.create_health_bar() 
                    elif tile == 16:
                        # enemy
                        self.create_enemies()
                    elif tile == 17:
                        pass # item box ammo
                    elif tile == 18:
                        pass # item grenade ammo
                    elif tile == 19:
                        pass # item health ammo

        return self.player, self.health_bar, self.enemies


    def create_enemies(self):
        return EnemySoldier("enemy", self.screen_rect.right * 0.6, GROUND, ENEMY_BASE_HEALTH, PLAYERS_SCALE, ENEMY_RUN_SPEED, 1, ENEMY_INITIAL_BULLETS, ENEMY_INITIAL_GRENADES)
        

    def create_player(self):
        return Soldier("player", 200, GROUND, SOLDIER_BASE_HEALTH, PLAYERS_SCALE, 5, 1, SOLDIER_INITIAL_BULLETS, SOLDIER_INITIAL_GRENADES)

    def create_health_bar(self):
        return HealthBar(10,10, self.player.health, self.player.max_health)
        