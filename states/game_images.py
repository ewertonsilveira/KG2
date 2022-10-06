import pygame

from states.settings import GRENADE_EXPLOSION_SCALE, TILE_SIZE, TILE_TYPES

class GameImageLoader(object):
    def __init__(self):
        self.world_images = []
        self.bullet_image = None
        self.grenade_image = None
        self.ammo_box_image = None
        self.health_box_image = None
        self.grenade_box_image = None
        self.grenade_explosion_images = None
    
    def get_bullet_image(self):
        if self.bullet_image == None:        
            self.bullet_image = pygame.image.load("public/graphics/icons/bullet.png").convert_alpha();
            print('bullet img')
        return self.bullet_image

    def get_grenade_explosion_images(self):
        if self.grenade_explosion_images == None:
            self.grenade_explosion_images = []
            print('grenade explosion img')
            for num in range(1, 6):
                img = pygame.image.load(f'public/graphics/explosion/exp{num}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * GRENADE_EXPLOSION_SCALE), int(img.get_height() * GRENADE_EXPLOSION_SCALE)))
                self.grenade_explosion_images.append(img)
        return self.grenade_explosion_images;

    def get_grenade_image(self):
        if self.grenade_image == None:
            self.grenade_image = pygame.image.load("public/graphics/icons/grenade.png").convert_alpha();
            print('grenade img')
        return self.grenade_image
    
    def get_grenade_box_image(self):
        if self.grenade_box_image == None:
            self.grenade_box_image = pygame.image.load("public/graphics/icons/grenade_box.png").convert_alpha();
            print('grenade box img')
        return self.grenade_box_image

    def get_health_box_image(self):
        if self.health_box_image == None:
            self.health_box_image = pygame.image.load("public/graphics/icons/health_box.png").convert_alpha();
            print('health_box img')
        return self.health_box_image
    
    def get_ammo_box_image(self):
        if self.ammo_box_image == None:
            self.ammo_box_image = pygame.image.load("public/graphics/icons/ammo_box.png").convert_alpha();
            print('ammo_box img')
        return self.ammo_box_image

    def get_world_images(self):
        if len(self.world_images) == 0:
            for img_id in range(TILE_TYPES):
                img = pygame.image.load(f"public/graphics/tile/{img_id}.png").convert_alpha()
                img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
                self.world_images.append(img)
            print('game world imgs')
        return self.world_images

GAME_IMAGES = GameImageLoader()