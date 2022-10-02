import pygame

from states.settings import GRENADE_EXPLOSION_SCALE

class GameImages(object):
    def __init__(self):
        self.bullet_image = None
        self.grenade_image = None
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

GAME_IMAGES = GameImages()