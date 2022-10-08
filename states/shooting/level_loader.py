import pygame

import csv
from states.settings import COLS
from states.shooting.world_data import WorldData

class LevelLoader(object):
    def __init__(self):        
        self.levels = {}

    def get_level(self, level):
        if level in self.levels:
            return self.levels[level]
        else:
            return self.load_level(level)
    
    def load_level(self, level):
        wd = WorldData()
        wd.init()
        with open(f'assets/level{level}_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    wd.world_data[x][y] = tile

            self.levels[level] = wd

        return self.levels[level]
        
    
LEVEL_LOADER = LevelLoader()

