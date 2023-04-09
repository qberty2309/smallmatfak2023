import pygame
from consts import *
from fruit import Fruit, RottenFruit
from snake import Snake, Direction


def handle_moving(snake):

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.steer(Direction.LEFT)
    if keys[pygame.K_RIGHT]:
        snake.steer(Direction.RIGHT)
    if keys[pygame.K_UP]:
        snake.steer(Direction.UP)
    if keys[pygame.K_DOWN]:
        snake.steer(Direction.DOWN)


def main():
    pygame.init()
    font = pygame.font.SysFont('timesnewroman', 75, True)
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)
    rottenfruit = RottenFruit(block_size=BLOCK_SIZE,bounds=WINDOW_SIZE)
    fruit = Fruit(block_size=BLOCK_SIZE,bounds=WINDOW_SIZE)
    snake = Snake(block_size=BLOCK_SIZE, bounds=WINDOW_SIZE)

    is_run = True

    while is_run:

        pygame.time.delay(100)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                is_run = False


        if snake.check_bounds_collision() or snake.suicide():

            text = font.render('YOU DIED', True, (255, 0, 0))
            window.blit(text, (150 , 150))
            pygame.display.update()
            pygame.time.delay(3000)

            break


        handle_moving(snake)

        snake.move()
        snake.check_for_food(fruit,rottenfruit)

        window.fill(BACK_COLOR)
        rottenfruit.draw(game=pygame, window=window)
        snake.draw(game=pygame, window=window)
        fruit.draw(game=pygame,window=window)

        pygame.display.update()

main()
