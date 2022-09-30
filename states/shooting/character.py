from email.headerregistry import Group
import pygame
import os

from states.shooting.bullet import Bullet

from states.settings import * 

class Soldier(pygame.sprite.Sprite):
    def __init__(self, chart_type, x, y, health, scale, speed, ammo):
        pygame.sprite.Sprite.__init__(self)
        # Variables
        self.alive = True
        self.char_type = chart_type
        self.speed = speed
        self.shoot_cooldown = 0
        self.health = health
        self.max_health = self.health
        self.flip = False
        self.direction = 1
        self.vel_y = 0
        self.ammo = ammo
        self.start_ammo = self.ammo
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.jump = False
        self.in_air = True
        self.image_update_time = pygame.time.get_ticks()
        self.bullet_group = pygame.sprite.Group()

        for animation in ['Idle', 'Run', 'Jump']:
            tmp_list = []
            dir = f'public/graphics/{self.char_type}/{animation}'
            for filename in os.listdir(dir):
                img = pygame.image.load(os.path.join(dir, filename)).convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale))) 
                tmp_list.append(img)
            self.animation_list.append(tmp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = img.get_rect()
        self.rect.center = (x, y - img.get_height()/2)

    def update(self, surface, enemies):
        self.update_animation()

        # update shoot cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        self.bullet_group.update(enemies, self.bullet_group)
        self.bullet_group.draw(surface)


    def move(self, moving_left, moving_right):
        # reset movement variables
        dx = 0
        dy = 0
        # assign movement variables if moving left or right
        if moving_left:            
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # jump
        if self.jump == True and not self.in_air:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        # apply gravity 
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y

        dy += self.vel_y

        # check collition with floor
        if self.rect.bottom + dy > GROUND:
            dy = GROUND - self.rect.bottom
            self.in_air = False

        # update rectangle pos
        self.rect.x += dx
        self.rect.y += dy
    
    def update_action(self, new_action):
        # update only if is different one
        if self.action != new_action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.image_update_time = pygame.time.get_ticks()

    def shoot(self, surface):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 10
            bullet = Bullet(surface, self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            self.bullet_group.add(bullet)
            self.ammo -= 1

    def update_animation(self):
        # update new image
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough fime has passed
        if pygame.time.get_ticks() - self.image_update_time > COOLDOWN_PERIOD:
            self.image_update_time = pygame.time.get_ticks()
            self.frame_index += 1
        
        # if animation has run out of images, reset back to initial
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def draw(self, surface):
        surface.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


