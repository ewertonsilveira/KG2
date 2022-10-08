import sys
import pygame
from pygame import mixer
from states.fonts import FONTS
from states.menu import Menu
from states.gameplay import Gameplay
from states.shooting.shooter import Shooter
from states.game_over import GameOver
from states.splash import Splash
from game import Game
from collections import namedtuple

from states.settings import *

Size = namedtuple('Size',"width height")
ScreenSize = Size(SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
mixer.init()
screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption('Kylie Games')

FONTS.init()

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