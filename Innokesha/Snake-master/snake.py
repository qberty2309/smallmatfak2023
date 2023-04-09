from enum import Enum
from consts import *

class Cords:
    x = None
    y = None
    block_size = None

    def __init__(self, x, y, block_size=20):
        self.x = x
        self.y = y
        self.block_size = block_size

    def get_cords(self):
        return self.x, self.y, self.block_size, self.block_size


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Snake:
    speed: int = None
    length: int = None
    color: tuple = SNAKE_COLOR
    direction: Direction = None
    block_size: int = None
    body = None
    bounds = None


    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.spawn()

    def spawn(self):
        self.length = 3
        self.body = [Cords(20, 20), Cords(20, 40), Cords(20, 60)]
        self.direction = Direction.DOWN

    def draw(self, game, window):
        for segment in self.body:
            game.draw.rect(window, self.color, segment.get_cords())

    def move(self):
        currnent_head = self.body[-1]

        if self.direction == Direction.LEFT:
            next_head = Cords(currnent_head.x - currnent_head.block_size, currnent_head.y)
            self.body.append(next_head)

        elif self.direction == Direction.RIGHT:
            next_head = Cords(currnent_head.x + currnent_head.block_size, currnent_head.y)
            self.body.append(next_head)

        elif self.direction == Direction.UP:
            next_head = Cords(currnent_head.x, currnent_head.y - currnent_head.block_size)
            self.body.append(next_head)

        elif self.direction == Direction.DOWN:
            next_head = Cords(currnent_head.x, currnent_head.y + currnent_head.block_size)
            self.body.append(next_head)

        if self.length < len(self.body):
            self.body.pop(0)

    def steer(self, direction: Direction):
        if self.direction == Direction.DOWN and direction != Direction.UP:
            self.direction = direction
        if self.direction == Direction.UP and direction != Direction.DOWN:
            self.direction = direction
        if self.direction == Direction.RIGHT and direction != Direction.LEFT:
            self.direction = direction
        if self.direction == Direction.LEFT and direction != Direction.RIGHT:
            self.direction = direction

    def check_bounds_collision(self):
        head = self.body[-1]

        if head.x > self.bounds[0] or head.y > self.bounds[1]:
            return True

        if head.x < 0 or head.y < 0:
            return True

    def eat(self):
        self.length += 1

    def eat_rotten_fruit(self):
        self.length -= 1
        self.body.pop(1)
    def check_for_food(self, fruit, rottenfruit):
        head = self.body[-1]
        has_eaten_fruit = False
        has_eaten_rottenfruit = False
        if head.x == rottenfruit.x and head.y == rottenfruit.y:
            rottenfruit.respawn()
            self.eat_rotten_fruit()
            has_eaten_rottenfruit = True

        if head.x == fruit.x and head.y == fruit.y:
            self.eat()
            fruit.respawn()
            has_eaten_fruit = True

        return has_eaten_fruit, has_eaten_rottenfruit

    def suicide(self):
        tail = self.body[0]
        head = self.body[-1]
        has_eaten_body = False


        if head.x == tail.x and head.y == tail.y:
            self.length -= 1

        for ln in range(len(self.body) - 1):
            segment = self.body[ln]
            if head.x == segment.x and head.y == segment.y:
                has_eaten_body = True
        return has_eaten_body




