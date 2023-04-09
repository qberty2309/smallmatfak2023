import random
from consts import *


class Fruit:
    block_size: int = 20
    color: tuple = FRUIT_COLOR
    x = 200
    y = 100
    bounds = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds

    def draw(self, game, window):
            game.draw.rect(window, self.color, (self.x , self.y , self.block_size, self.block_size))

    def respawn(self):
        blocks_in_x = (self.bounds[0])/self.block_size
        blocks_in_y = (self.bounds[1])/self.block_size
        self.x = random.randint(0, blocks_in_x - 1)*self.block_size
        self.y = random.randint(0, blocks_in_y - 1)*self.block_size

class RottenFruit:
    block_size: int = 20
    color: tuple = ROTTENFRUIT
    x = 400
    y = 500
    bounds = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds

    def draw(self, game, window):
            game.draw.rect(window, self.color, (self.x , self.y , self.block_size, self.block_size))

    def respawn(self):
        blocks_in_x = (self.bounds[0])/self.block_size
        blocks_in_y = (self.bounds[1])/self.block_size
        self.x = random.randint(0, blocks_in_x - 1)*self.block_size
        self.y = random.randint(0, blocks_in_y - 1)*self.block_size