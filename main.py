import sys
import pygame
from states.menu import Menu
from states.gameplay import Gameplay
from states.shooting.shooter import Shooter
from states.game_over import GameOver
from states.splash import Splash
from game import Game
from collections import namedtuple

Size = namedtuple('Size',"width height")
ScreenSize = Size(800, int(800 * 0.8))

pygame.init()
screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption('Kylie Jumper')

states = {
    "MENU": Menu(),
    "SPLASH": Splash(),
    "GAMEPLAY": Gameplay(),
    "SHOOTER": Shooter(),
    "GAME_OVER": GameOver(),
}

game = Game(screen, states, "SPLASH")
game.run()

pygame.quit()
sys.exit()