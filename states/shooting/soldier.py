from email.headerregistry import Group
import pygame
import os

from states.shooting.bullet import Bullet

from states.settings import *
from states.shooting.grenade import Grenade 

class Soldier(pygame.sprite.Sprite):
    def __init__(self, chart_type, x, y, health, scale, speed, direction, ammo, grenade):
        pygame.sprite.Sprite.__init__(self)
        # Variables
        self.alive = True
        self.char_type = chart_type
        self.speed = speed
        self.health = health
        self.max_health = self.health
        self.flip = False
        self.direction = direction
        self.vel_y = 0
        self.ammo = ammo
        self.shoot_cooldown = 0
        self.start_ammo = self.ammo
        self.grenade = grenade
        self.grenade_cooldown = 0
        self.grenade_ammo = self.grenade
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.jump = False
        self.in_air = True
        self.image_update_time = pygame.time.get_ticks()
        self.bullet_group = pygame.sprite.Group()
        self.grenade_group = pygame.sprite.Group()

        for animation in ['idle', 'run', 'jump', 'death']:
            tmp_list = []
            dir = f'public/graphics/{self.char_type}/{animation}'
            files = os.listdir(dir)
            files.sort()
            for filename in files:
                img = pygame.image.load(os.path.join(dir, filename)).convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale))) 
                tmp_list.append(img)
            self.animation_list.append(tmp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = img.get_rect()
        self.rect.center = (x, y - img.get_height()/2)

    def update(self, surface, enemies):
        self.update_animation()
        # keep checking if soldier is alive
        self.check_alive()

        # update shoot cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        # update grenade cooldown
        if self.grenade_cooldown > 0:
            self.grenade_cooldown -= 1

        self.bullet_group.update(enemies, self.bullet_group)
        self.bullet_group.draw(surface)

        self.grenade_group.update(enemies, self.grenade_group)
        self.grenade_group.draw(surface)

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
        # update only if is a new action 
        if self.action != new_action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.image_update_time = pygame.time.get_ticks()

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3) # Death

    def shoot(self, surface):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 10
            bullet = Bullet(surface, self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            self.bullet_group.add(bullet)
            self.ammo -= 1

    def throw_grenade(self, surface):
        if self.grenade_cooldown == 0 and self.grenade > 0:
            self.grenade_cooldown = 10
            grenade = Grenade(surface, self.rect.centerx, self.rect.centery, self.direction)
            self.grenade_group.add(grenade)
            self.grenade -= 1

    def update_animation(self):
        # update new image
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]

        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.image_update_time > COOLDOWN_PERIOD:
            self.image_update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def draw(self, surface):
        surface.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

