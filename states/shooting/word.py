import pygame
from states.colors import COLORS
from states.fonts import FONTS
from states.game_images import GAME_IMAGES

from states.settings import ENEMY_BASE_HEALTH, ENEMY_INITIAL_BULLETS, ENEMY_INITIAL_GRENADES, ENEMY_RUN_SPEED, GROUND, PLAYERS_SCALE, SCREEN_HEIGHT, SOLDIER_BASE_HEALTH, SOLDIER_INITIAL_BULLETS, SOLDIER_INITIAL_GRENADES, TILE_SIZE
from states.shooting.decoration import Decoration
from states.shooting.enemy_soldier import EnemySoldier
from states.shooting.exit import Exit
from states.shooting.health_bar import HealthBar
from states.shooting.item_box import AMMO, GRENADE, HEALTH, ItemBox
from states.shooting.soldier import ENEMY_TYPE, PLAYER_TYPE, Soldier
from states.shooting.water import Water


class World(object):
    def __init__(self):        
        self.obstacle_list = []
        self.enemies = []
        self.player = None
        self.health_bar = None
        self.bg_scroll = 0
        self.screen_scroll = 0
        self.level_length = 0
        self.exit_group = pygame.sprite.Group()
        self.water_group = pygame.sprite.Group()
        self.item_box_group = pygame.sprite.Group()
        self.decoration_group = pygame.sprite.Group()

    def process_data(self, data):
        imgs = GAME_IMAGES.get_world_images()
        self.level_length = len(data[0])
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
                        self.water_group.add(Water(img, x_axis, y_axis))
                    elif tile >= 11 and tile <= 14:
                        # decoration
                        self.decoration_group.add(Decoration(img, x_axis, y_axis))
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
                        # item health ammo
                        self.item_box_group.add(ItemBox(HEALTH, x_axis, y_axis))
                    elif tile == 20:
                        self.exit_group.add(Exit(img, x_axis, y_axis))


        return self.player, self.health_bar, self.enemies

    def draw(self, surface):

        for tile in self.obstacle_list:
            tile[1].x += self.screen_scroll
            surface.blit(tile[0], tile[1])

        # draw enemies
        for _, enemy in enumerate(self.enemies):
            enemy.ai(surface, self.bg_scroll, self.level_length, self.screen_scroll, self.obstacle_list, self.player)
            enemy.draw(surface)
            enemy.update(surface, self.screen_scroll, self.obstacle_list, [self.player])            
        

        # player
        self.player.draw(surface)
        self.player.update(surface, self.screen_scroll, self.obstacle_list, self.enemies)
        self.health_bar.draw(surface, self.player.health)

        # show ammo
        self.draw_text(surface, 'AMMO: ', FONTS.secondary_font, COLORS.WHITE, 10, 35)
        for x in range(self.player.ammo): surface.blit(GAME_IMAGES.get_bullet_image(), (80 + (x * 10), 40))

        # show grenades
        self.draw_text(surface, 'GRENADES:', FONTS.secondary_font, COLORS.WHITE, 10, 60)
        for x in range(self.player.grenade): surface.blit(GAME_IMAGES.get_grenade_image(), (125 + (x * 15), 60))


        self.item_box_group.update(self.screen_scroll, self.player)
        self.item_box_group.draw(surface)

        self.exit_group.update(self.screen_scroll)
        self.exit_group.draw(surface)

        self.water_group.update(self.screen_scroll)
        self.water_group.draw(surface)

        self.decoration_group.update(self.screen_scroll)
        self.decoration_group.draw(surface)

    def draw_bg(self, surface, color):
        surface.fill(color)

        sky_img = GAME_IMAGES.get_sky_image()

        width = sky_img.get_width()
        m_img = GAME_IMAGES.get_mountain_image()
        pine1_img = GAME_IMAGES.get_pine1_image()
        pine2_img = GAME_IMAGES.get_pine2_image()
        
        for idx in range(6):
            w = idx * width
            surface.blit(sky_img,   (w - self.bg_scroll * 0.5, 0))
            surface.blit(m_img,     (w - self.bg_scroll * 0.6, SCREEN_HEIGHT - m_img.get_height() - SCREEN_HEIGHT * 0.40))
            surface.blit(pine1_img, (w - self.bg_scroll * 0.7, SCREEN_HEIGHT - pine1_img.get_height() - SCREEN_HEIGHT * 0.20))
            surface.blit(pine2_img, (w - self.bg_scroll * 0.8, SCREEN_HEIGHT - pine2_img.get_height()))

    def draw_text(self, surface, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        surface.blit(img, (x, y))

    def create_enemies(self, x, y):
        return EnemySoldier(ENEMY_TYPE, x, y, ENEMY_BASE_HEALTH, PLAYERS_SCALE, ENEMY_RUN_SPEED, 1, ENEMY_INITIAL_BULLETS, ENEMY_INITIAL_GRENADES)
        

    def create_player(self, x, y):
        return Soldier(PLAYER_TYPE, x, y, SOLDIER_BASE_HEALTH, PLAYERS_SCALE, 5, 1, SOLDIER_INITIAL_BULLETS, SOLDIER_INITIAL_GRENADES)

    def create_health_bar(self):
        return HealthBar(10,10, self.player.health, self.player.max_health)
        