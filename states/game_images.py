import pygame

from states.settings import GRENADE_EXPLOSION_SCALE, TILE_SIZE, TILE_TYPES

class GameImageLoader(object):
    def __init__(self):
        self.world_images = []
        self.sky_image = None
        self.pine1_image = None
        self.pine2_image = None
        self.bullet_image = None
        self.grenade_image = None
        self.ammo_box_image = None
        self.mountain_image = None
        self.exit_btn_image = None
        self.start_btn_image = None
        self.health_box_image = None
        self.health_box_image = None
        self.restart_btn_image = None
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
    
    def get_sky_image(self):
        if self.sky_image == None:
            self.sky_image = pygame.image.load("public/graphics/background/sky_cloud.png").convert_alpha();
            print('sky_image img')
        return self.sky_image
    
    def get_mountain_image(self):
        if self.mountain_image == None:
            self.mountain_image = pygame.image.load("public/graphics/background/mountain.png").convert_alpha();
            print('mountain img')
        return self.mountain_image

    def get_pine1_image(self):
        if self.pine1_image == None:
            self.pine1_image = pygame.image.load("public/graphics/background/pine1.png").convert_alpha();
            print('pine1 img')
        return self.pine1_image

    def get_pine2_image(self):
        if self.pine2_image == None:
            self.pine2_image = pygame.image.load("public/graphics/background/pine2.png").convert_alpha();
            print('pine2 img')
        return self.pine2_image
    
    def get_start_btn_image(self):
        if self.start_btn_image == None:
            self.start_btn_image = pygame.image.load("public/graphics/start_btn.png").convert_alpha();
            print('start_btn_image img')
        return self.start_btn_image

    def get_restart_btn_image(self):
        if self.restart_btn_image == None:
            self.restart_btn_image = pygame.image.load("public/graphics/restart_btn.png").convert_alpha();
            print('re-start_btn_image img')
        return self.restart_btn_image

    def get_exit_btn_image(self):
        if self.exit_btn_image == None:
            self.exit_btn_image = pygame.image.load("public/graphics/exit_btn.png").convert_alpha();
            print('start_btn_image img')
        return self.exit_btn_image

    def get_world_images(self):
        if len(self.world_images) == 0:
            for img_id in range(TILE_TYPES):
                img = pygame.image.load(f"public/graphics/tile/{img_id}.png").convert_alpha()
                img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
                self.world_images.append(img)
            print('game world imgs')
        return self.world_images

GAME_IMAGES = GameImageLoader()