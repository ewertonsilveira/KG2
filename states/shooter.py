import pygame
from .base import BaseState

# define game variables
GRAVITY = 0.75
COOLDOWN_PERIOD = 90
class Character(pygame.sprite.Sprite):
    def __init__(self, chart_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        # Variables
        self.alive = True
        self.char_type = chart_type
        self.speed = speed
        self.flip = False
        self.direction = 1
        self.vel_y = 0
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.jump = False
        self.image_update_time = pygame.time.get_ticks()

        tmp_list = []
        for i in range(5):
            img = pygame.image.load(f'public/graphics/{self.char_type}/idle/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale))) 
            tmp_list.append(img)
        self.animation_list.append(tmp_list)

        tmp_list = []
        for i in range(6):
            img = pygame.image.load(f'public/graphics/{self.char_type}/run/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
            tmp_list.append(img)
        self.animation_list.append(tmp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = img.get_rect()
        self.rect.center = (x, y)
    
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
        if self.jump:
            self.vel_y = -11

        dy += self.vel_y

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


class Shooter(BaseState):
    def __init__(self):
        super(Shooter, self).__init__()
        self.next_state = "MENU"
        self.bgColor = (144,201,120)

        # player action variables
        self.moving_left = False
        self.moving_right = False

        self.player = Character("player", 200, 200, 3, 5)
        self.enemies = [Character("enemy", 300, 200, 3, 5)]


    def draw(self, surface):
        self.draw_bg(surface, self.bgColor)

        for _, enemy in enumerate(self.enemies):
            enemy.draw(surface)
            
          
        self.player.draw(surface)
        self.player.update_animation()

        # update player action
        if self.player.alive:
            if self.moving_left or self.moving_right:
                self.player.update_action(1) #1 run
            else:
                self.player.update_action(0) #1 idle

            self.player.move(self.moving_left, self.moving_right)
        

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.moving_left = True
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.moving_right = True
            elif (event.key == pygame.K_w or event.key == pygame.K_UP) and self.player.alive:
                self.jump = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.moving_left = False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.moving_right = False

            elif event.key == pygame.K_ESCAPE:
                self.done = True