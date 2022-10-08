from email.headerregistry import Group
import pygame
import os
from states.content_loader import LOADER

from states.shooting.bullet import Bullet

from states.settings import *
from states.shooting.grenade import Grenade 

ENEMY_TYPE='enemy'
PLAYER_TYPE='player'

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
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def ai(self, surface, obstacle_list, target):
        pass

    def update(self, surface, screen_scroll, obstacle_list, enemies):
        self.update_animation()
        # keep checking if soldier is alive
        self.check_alive()

        # update shoot cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        # update grenade cooldown
        if self.grenade_cooldown > 0:
            self.grenade_cooldown -= 1

        self.bullet_group.update(screen_scroll, obstacle_list, enemies, self.bullet_group)
        self.bullet_group.draw(surface)

        self.grenade_group.update(screen_scroll, obstacle_list, self, enemies)
        self.grenade_group.draw(surface)

    def move(self, bg_scroll, level_length, water_group, exit_group, obstacle_list, moving_left, moving_right):
        # reset movement variables
        dx = 0
        dy = 0
        scroll = 0
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
        if self.jump == True and self.in_air == False:
            self.vel_y = SOLDIER_JUMP_POWER
            self.jump = False
            self.in_air = True

        # apply gravity 
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y

        dy += self.vel_y

        #check for collision
        for tile in obstacle_list:
            #check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                #if the ai has hit a wall then make it turn around
                if self.char_type == ENEMY_TYPE:
                    self.direction *= -1
                    self.move_counter = 0
            #check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #check if below the ground, i.e. jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                #check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        #check for collision with water
        if pygame.sprite.spritecollide(self, water_group, False):
            self.health = 0

        #check for collision with exit
        level_complete = False
        if pygame.sprite.spritecollide(self, exit_group, False):
            level_complete = True

        # check if player fallen off the map
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0
        
        # check if going off the edge of screen
        if self.char_type == PLAYER_TYPE:
            if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
                dx = 0
        
        # update rectangle pos
        self.rect.x += dx
        self.rect.y += dy

        if self.char_type == PLAYER_TYPE:
            if (self.rect.right > SCREEN_WIDTH - SCROLL_THRESHOLD and bg_scroll < (level_length * TILE_SIZE) - SCREEN_WIDTH)\
                or (self.rect.left < SCROLL_THRESHOLD and bg_scroll > abs(dx)):
                self.rect.x -= dx
                scroll = -dx

        return scroll, level_complete

    
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
            LOADER.get_shot_sound().play()            
            self.shoot_cooldown = SHOOT_COOLDOWN_TIMER
            x = self.rect.centerx + (0.3 * self.rect.size[0] * self.direction)
            bullet = Bullet(surface, x, self.rect.centery, self.direction)
            self.bullet_group.add(bullet)
            self.ammo -= 1

    def throw_grenade(self, surface):
        if self.grenade_cooldown == 0 and self.grenade > 0:
            self.grenade_cooldown = GRENADE_COOLDOWN_TIMER
            x = self.rect.centerx + (0.3 * self.rect.size[0] * self.direction)
            grenade = Grenade(surface, x, self.rect.top, self.direction)
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

    def update_health(self, value):
        self.health += value
        if self.health > self.max_health:
            self.health = self.max_health
        print(self.health, self.max_health)

    def update_ammo(self, value):
        self.ammo += value
        print(self.ammo)
            
    def update_grenade(self, value): 
        self.grenade += value
        print(self.grenade)