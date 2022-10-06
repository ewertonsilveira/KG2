import pygame
from states.game_images import GAME_IMAGES

from states.settings import COLS, ENEMY_BASE_HEALTH, ENEMY_INITIAL_BULLETS, ENEMY_INITIAL_GRENADES, ENEMY_RUN_SPEED, GROUND, PLAYERS_SCALE, SOLDIER_BASE_HEALTH, SOLDIER_INITIAL_BULLETS, SOLDIER_INITIAL_GRENADES, TILE_SIZE
from states.shooting.enemy_soldier import EnemySoldier
from states.shooting.health_bar import HealthBar
from states.shooting.item_box import AMMO, GRENADE, HEALTH, ItemBox
from states.shooting.soldier import Soldier

class World(object):
    def __init__(self):        
        self.obstacle_list = []
        self.enemies = []
        self.player = None
        self.health_bar = None
        self.item_box_group = pygame.sprite.Group()

    def process_data(self, data):
        imgs = GAME_IMAGES.get_world_images()
        for y, row in enumerate(data):
            for x, t in enumerate(row):
                tile = int(t)
                if tile >= 0:
                    x_axis = x * TILE_SIZE
                    y_axis = y * TILE_SIZE
                    img = imgs[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x_axis
                    img_rect.y = y_axis
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
                        self.player = self.create_player(x_axis, y_axis)
                        self.health_bar = self.create_health_bar() 
                    elif tile == 16:
                        # enemy
                        self.enemies.append(self.create_enemies(x_axis, y_axis))
                    elif tile == 17:
                        # item ammo
                        self.item_box_group.add(ItemBox(AMMO, x_axis, y_axis))
                    elif tile == 18:
                        # item grenade 
                        self.item_box_group.add(ItemBox(GRENADE, x_axis, y_axis))
                    elif tile == 19:
                        pass # item health ammo
                        self.item_box_group.add(ItemBox(HEALTH, x_axis, y_axis))

        return self.player, self.health_bar, self.enemies

    def draw(self, surface):
        for tile in self.obstacle_list:
            surface.blit(tile[0], tile[1])

    def create_enemies(self, x, y):
        return EnemySoldier("enemy", x, y, ENEMY_BASE_HEALTH, PLAYERS_SCALE, ENEMY_RUN_SPEED, 1, ENEMY_INITIAL_BULLETS, ENEMY_INITIAL_GRENADES)
        

    def create_player(self, x, y):
        return Soldier("player", x, y, SOLDIER_BASE_HEALTH, PLAYERS_SCALE, 5, 1, SOLDIER_INITIAL_BULLETS, SOLDIER_INITIAL_GRENADES)

    def create_health_bar(self):
        return HealthBar(10,10, self.player.health, self.player.max_health)
        