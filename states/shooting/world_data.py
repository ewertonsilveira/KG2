import pygame

from states.settings import COLS

class WorldData(object):
    def __init__(self):        
        self.world_data = []

    def init(self):
        for _ in range(COLS):
            self.world_data.append([-1] * COLS)
