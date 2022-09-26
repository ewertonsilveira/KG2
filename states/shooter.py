import pygame
from .base import BaseState

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        # Variables
        self.speed = speed

        img = pygame.image.load('public/graphics/player/idle/0.png').convert_alpha()
        self.image = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
        self.rect = img.get_rect()
        self.rect.center = (x, y)
    
    def move(self, moving_left, moving_right):
        # reset movement variables
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left:            
            dx = -self.speed
        if moving_right:
            dx = self.speed

        # update rectangle pos
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Shooter(BaseState):
    def __init__(self):
        super(Shooter, self).__init__()
        self.next_state = "MENU"
        self.bgColor = (144,201,120)

        self.moving_left = False
        self.moving_right = False

        print(self.moving_left)
        print(self.moving_right)

        self.players = [Soldier(200, 200, 3, 5)]


    def draw(self, surface):
        self.draw_bg(surface, self.bgColor)

        for _, player in enumerate(self.players):
            player.draw(surface)
            player.move(self.moving_left, self.moving_right)
        

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.moving_left = True
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.moving_left = False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.moving_right = False

            elif event.key == pygame.K_ESCAPE:
                self.done = True